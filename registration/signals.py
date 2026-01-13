# accounts/signals.py
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def send_new_user_notification(sender, instance, created, **kwargs):
    if created:  # Check if a new user was created
        subject = "New User Registration Alert"
        message = (
            f"Hello Team,\n\n"
            f"A new user has just registered for the first time on the FINFIRE application, and their user account has been successfully created.\n\n"
            f"Registration details:\n"
            f"Username: {instance.username}\n"
            f"Email: {instance.email}\n\n"
            f"---\nThis is an automated email from the FINFIRE system. Please do not reply to this message."
        )
        recipient_email = "sam@finfire.com"  # Replace with the staff email
        send_mail(
            subject,
            message,
            'romin@finfire.com',  # Replace with your "from" email
            ["tony@tonydrexelsmith.com","sam@finfire.com","romin@finfire.com","leslye@tonydrexelsmith.com","leslye@finfire.com","nick@finfire.com","ronald@finfire.com"],
            fail_silently=False,
        )
