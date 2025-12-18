# Base stage
FROM --platform=amd64 python:3.11-slim AS base

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libssl-dev \
    zlib1g-dev \
    libjpeg-dev \
    tzdata \
    ffmpeg \
    python3-dev \
    bash \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install gunicorn

WORKDIR /app

# Copy requirements and install dependencies
COPY ./requirements.txt /app/
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Runner stage
FROM --platform=amd64 python:3.11-slim AS runner

WORKDIR /app

# Copy dependencies from base image
COPY --from=base /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=base /bin /bin
COPY --from=base /usr/bin /usr/bin
COPY --from=base /usr/local/bin /usr/local/bin

COPY . .

# Create log directories and set environment variables for logging
RUN mkdir -p /app/logs/ && touch /app/logs/application.log
RUN mkdir -p /var/log/gunicorn
RUN mkdir -p /var/log/django/
RUN touch /var/log/django/django.log

ENV DJANGO_LOG_FILE=/var/log/django/django.log

# Make entrypoint script executable
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000
ENV PORT=8000

ENTRYPOINT [ "bash", "/app/entrypoint.sh" ]
CMD ["gunicorn", "finfire_whitelable.wsgi:application", "--bind", "0.0.0.0:8000", "--access-logfile", "/var/log/gunicorn/access.log", "--error-logfile", "/var/log/gunicorn/error.log"]

