# --- Stage 1: Builder ---
FROM --platform=amd64 python:3.11-slim AS builder

WORKDIR /build

# Install build-essential if any requirements need compilation
RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt
RUN pip install --no-cache-dir --prefix=/install gunicorn

# --- Stage 2: Runner ---
FROM --platform=amd64 python:3.11-slim AS runner

# 1. Install ONLY the necessary runtime system libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libglib2.0-0 \
    shared-mime-info \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2. Copy ONLY the python packages from the builder
COPY --from=builder /install /usr/local
COPY . .

# Setup logs and permissions
RUN mkdir -p /app/logs/ /var/log/gunicorn /var/log/django/ && \
    touch /app/logs/application.log /var/log/django/django.log && \
    chmod +x /app/entrypoint.sh

ENV DJANGO_LOG_FILE=/var/log/django/django.log
EXPOSE 8000

ENTRYPOINT [ "bash", "/app/entrypoint.sh" ]
CMD ["gunicorn", "finfire_whitelable.wsgi:application", "--bind", "0.0.0.0:8000"]