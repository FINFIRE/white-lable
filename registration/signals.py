# accounts/signals.py
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from tenants.utils import tenant_notification_recipients


@receiver(post_save, sender=User)
def send_new_user_notification(sender, instance, created, **kwargs):
    if not created:
        return

    # Notify the active tenant's support team — not the legacy FINFIRE
    # team list. If no tenant is resolved (public-schema admin work) or
    # the tenant hasn't set a support email yet, skip silently.
    recipients = tenant_notification_recipients()
    if not recipients:
        return

    subject = "New User Registration Alert"
    message = (
        f"Hello Team,\n\n"
        f"A new user has just registered for the first time, and their "
        f"user account has been successfully created.\n\n"
        f"Registration details:\n"
        f"Username: {instance.username}\n"
        f"Email: {instance.email}\n\n"
        f"---\nThis is an automated email. Please do not reply to this message."
    )
    send_mail(
        subject,
        message,
        getattr(settings, 'DEFAULT_FROM_EMAIL', None) or settings.EMAIL_HOST_USER,
        recipients,
        fail_silently=False,
    )
