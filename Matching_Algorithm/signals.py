from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os
from django.conf import settings
from datetime import datetime
from .views import word
from django.http import HttpRequest
from django.contrib.auth.models import AnonymousUser
from connections.models import Match_Data
from truth_in_capital.views import excel_template_download_view 

@receiver(post_save, sender=Match_Data)
def send_match_notification(sender, instance, created, **kwargs):
    if created:  # Only send email when a new match is created
        subject = "New Match Alert: User Matched to Capital Markets"
        message = (
            f"Hello Team,\n\n"
            f"We are excited to inform you that a new user, {instance.user.username}, has successfully registered an account, completed the required survey, and has now been matched to relevant capital markets through the FINFIRE platform. The user is yet to view their personalized one-page letter.\n\n"
            f"Attached to this email, you will find the automatically generated $499 FINFIRE report (Word file) for this user. This document is provided so you can review, edit, and send it to the user if they request it.\n\n"
            f"Until our process is fully automated, your assistance in preparing and finalizing the FINFIRE report is greatly appreciated.\n\n"
            f"Thank you for your continued support!\n\n"
            f"Best regards,\n"
            f"\n---\nThis is an automated email from the FINFIRE system. Please do not reply to this message."
        )
        # Create a mock request object for the word function
        request = HttpRequest()
        request.user = instance.user
        
        # Generate Word document using the existing word function
        response = word(request)
        try:
            excel_response = excel_template_download_view(request, instance.user.id)
        except:
            pass
        
        # Create email with attachment
        email = EmailMessage(
            subject,
            message,
            'romin@finfire.com',  # From email
            ["tony@tonydrexelsmith.com","sam@finfire.com","leslye@tonydrexelsmith.com","leslye@finfire.com","nick@finfire.com","ronald@finfire.com"],  # To email
        )
        
        # Attach the Word document from the response
        email.attach(f"match_report_{instance.user.username}.docx", response.content, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        
        # Attach the Excel document from the excel response
        if excel_response:
            email.attach(f"truth_in_capital_{instance.user.username}.xlsx", excel_response.content, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        else:
            pass
        # Send the email
        email.send(fail_silently=False) 