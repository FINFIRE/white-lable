#!/usr/bin/env bash
# One-shot bootstrap for a fresh Ubuntu 22.04/24.04 EC2 instance.
# Run as the default 'ubuntu' user with passwordless sudo:
#   curl -fsSL https://raw.githubusercontent.com/<you>/white-lable/<branch>/deploy/bootstrap_ec2.sh | bash
# or, if the repo is already cloned:
#   bash deploy/bootstrap_ec2.sh

set -euo pipefail

# --- 0. Sanity checks -------------------------------------------------------
if [[ $EUID -eq 0 ]]; then
    echo "Run as the 'ubuntu' user, not root. sudo is invoked per-command." >&2
    exit 1
fi

# --- 1. Base packages ------------------------------------------------------
sudo apt-get update -y
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
    ca-certificates curl git ufw nginx \
    python3-pip software-properties-common gnupg lsb-release \
    rsync unzip

# --- 2. Swap (helps npm build on small boxes) ------------------------------
if ! swapon --show | grep -q '/swapfile'; then
    sudo fallocate -l 2G /swapfile
    sudo chmod 600 /swapfile
    sudo mkswap /swapfile
    sudo swapon /swapfile
    echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
fi

# --- 3. Node.js 20 (for `npm run build` on the box) -----------------------
if ! command -v node >/dev/null 2>&1; then
    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
    sudo apt-get install -y nodejs
fi

# --- 4. Docker Engine + compose plugin -------------------------------------
if ! command -v docker >/dev/null 2>&1; then
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
        sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list >/dev/null
    sudo apt-get update -y
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io \
        docker-buildx-plugin docker-compose-plugin
    sudo usermod -aG docker "$USER"
fi

# --- 5. Certbot (snap is the upstream-recommended path on Ubuntu) ----------
if ! command -v certbot >/dev/null 2>&1; then
    sudo snap install core
    sudo snap refresh core
    sudo snap install --classic certbot
    sudo ln -sf /snap/bin/certbot /usr/bin/certbot
fi

# --- 6. Directory layout ---------------------------------------------------
sudo mkdir -p \
    /var/www/finfire/dist \
    /var/www/finfire/static \
    /var/www/finfire/media \
    /var/www/certbot \
    /var/log/finfire/django \
    /var/log/finfire/gunicorn \
    /srv/finfire
sudo chown -R "$USER:$USER" /var/www/finfire /var/log/finfire /srv/finfire

# Postgres data directory. The official postgres image runs initdb as
# UID 999 / GID 999 inside the container; the bind mount on the host must
# be owned by that UID or initdb refuses to write ("data directory has
# wrong ownership"). We don't add a 'postgres' user on the host — just
# chown to the numeric IDs directly, which is what the container cares
# about.
sudo mkdir -p /var/lib/finfire-postgres
sudo chown -R 999:999 /var/lib/finfire-postgres
sudo chmod 700 /var/lib/finfire-postgres

# Backup target — pg_dump output ends up here if you wire up the cron in
# deploy/backup_db.sh (out of scope for this script, but the dir is
# pre-created so the cron job doesn't have to be root just to mkdir).
sudo mkdir -p /var/backups/finfire
sudo chown -R "$USER:$USER" /var/backups/finfire

# --- 7. Firewall -----------------------------------------------------------
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw --force enable

# --- 8. Disable nginx default site so our config can own the server ------
sudo rm -f /etc/nginx/sites-enabled/default

cat <<MSG

================================================================
Bootstrap complete.

Next:
  1) Log out and back in so the docker group takes effect:
        exit
        ssh ubuntu@<host>

  2) Clone the repo:
        git clone https://github.com/FINFIRE/white-lable.git /srv/finfire
        cd /srv/finfire
        git checkout <your-branch>

  3) Create /srv/finfire/.env from .env.production.example and fill in RDS,
     Stripe, SMTP, SECRET_KEY.

  4) Drop the nginx config in place:
        sudo cp deploy/nginx/appfinfire.conf /etc/nginx/sites-available/appfinfire
        sudo ln -sf /etc/nginx/sites-available/appfinfire \
                    /etc/nginx/sites-enabled/appfinfire

  5) Issue the wildcard cert via Route 53 (fully automated; requires an
     IAM role attached to this EC2 with the perms in
     deploy/route53-iam-policy.json):
        sudo bash deploy/issue_cert.sh

  6) Reload nginx and run the first deploy:
        sudo nginx -t && sudo systemctl reload nginx
        bash deploy/deploy.sh
================================================================
MSG
