from django.conf import settings
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpRequest

from connections.models import Match_Data
from tenants.utils import tenant_notification_recipients
from truth_in_capital.views import excel_template_download_view

from .views import word


@receiver(post_save, sender=Match_Data)
def send_match_notification(sender, instance, created, **kwargs):
    if not created:  # only fire on initial match creation
        return

    # Email goes to the active tenant's support team. No tenant or no
    # support_email -> skip silently (the legacy hardcoded FINFIRE
    # distribution list no longer applies in the white-label install).
    recipients = tenant_notification_recipients()
    if not recipients:
        return

    subject = "New Match Alert: User Matched to Capital Markets"
    message = (
        f"Hello Team,\n\n"
        f"A new user, {instance.user.username}, has successfully registered, "
        f"completed the survey, and been matched to relevant capital markets. "
        f"The user has not yet viewed their personalized one-page letter.\n\n"
        f"Attached:\n"
        f"  - Word document ($499 follow-up report) for review/edit before "
        f"sending to the user on request.\n"
        f"  - Excel template ('Truth in Capital') for this user.\n\n"
        f"Thank you for your continued support!\n"
        f"\n---\nThis is an automated email. Please do not reply to this message."
    )

    # Build a mock request so the existing view-based generators can run
    # outside an HTTP request cycle (these helpers were written for views).
    request = HttpRequest()
    request.user = instance.user

    word_response = word(request)
    try:
        excel_response = excel_template_download_view(request, instance.user.id)
    except Exception:
        excel_response = None

    email = EmailMessage(
        subject,
        message,
        getattr(settings, 'DEFAULT_FROM_EMAIL', None) or settings.EMAIL_HOST_USER,
        recipients,
    )

    email.attach(
        f"match_report_{instance.user.username}.docx",
        word_response.content,
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    )

    if excel_response is not None:
        email.attach(
            f"truth_in_capital_{instance.user.username}.xlsx",
            excel_response.content,
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )

    email.send(fail_silently=False)
