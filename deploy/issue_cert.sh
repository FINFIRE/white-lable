#!/usr/bin/env bash
# Issue a wildcard cert for appfinfire.com using Let's Encrypt's DNS-01
# challenge against Route 53. DNS-01 is required because *.appfinfire.com
# cannot be proven via HTTP-01.
#
# The certbot-dns-route53 plugin uses the AWS SDK's default credential
# chain, so any of these will work — in order of preference:
#   1) IAM role attached to the EC2 instance (recommended, no secrets)
#   2) ~/.aws/credentials on the box
#   3) AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY env vars
#
# Required IAM permissions (see deploy/route53-iam-policy.json):
#   route53:ListHostedZones
#   route53:GetChange
#   route53:ChangeResourceRecordSets (scoped to the appfinfire.com zone)
#
# Run as root (or with sudo). After this runs once, the systemd
# `snap.certbot.renew` timer (installed with snap certbot) will auto-renew.

set -euo pipefail

DOMAIN="appfinfire.com"
EMAIL="${LETSENCRYPT_EMAIL:-ops@appfinfire.com}"

# Ensure the route53 DNS plugin is installed in certbot's snap.
if ! sudo certbot plugins 2>/dev/null | grep -q 'dns-route53'; then
    sudo snap set certbot trust-plugin-with-root=ok
    sudo snap install certbot-dns-route53
fi

sudo certbot certonly \
    --dns-route53 \
    --agree-tos \
    --email "$EMAIL" \
    --no-eff-email \
    --non-interactive \
    -d "$DOMAIN" \
    -d "*.$DOMAIN"

echo
echo "Cert installed at /etc/letsencrypt/live/${DOMAIN}/"
echo "Auto-renewal:  systemctl status snap.certbot.renew.timer"
echo "Reload nginx:  sudo systemctl reload nginx"
