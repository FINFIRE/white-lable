from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
import json
from django.conf import settings

class Match_Data(models.Model):
    class Meta:
        verbose_name = "HTML Doc for Automated pdf and word report"
        verbose_name_plural = "HTML Doc for Automated pdf and word report"
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=0)
    html = models.CharField(max_length=10000000)

    def __str__(self):
        return(f'{self.user} : {self.html[0]}')

class pay_load_string(models.Model):
    class Meta:
        verbose_name ="Automated JSON triger field for Click up and Front End (One API end point)"
        verbose_name_plural = "Automated JSON triger field for Click up and Front End (One API end point)"
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=0)
    payLoadString = models.JSONField()

    def __str__(self):
        return(f'{self.user}')


@receiver(post_save, sender=pay_load_string, dispatch_uid="send_payload_to_external_api_unique")
def send_payload_to_external_api(sender, instance, created, **kwargs):
    """
    Signal hook that automatically sends payLoadString data to external API
    when a pay_load_string object is saved.
    """
    # Only send on initial creation to avoid duplicate sends on updates
    if not created:
        return
    try:
        # Get configuration from settings
        target_url = getattr(settings, 'PAYLOAD_WEBHOOK_URL', 'https://your-api-endpoint.com/webhook')
        timeout = getattr(settings, 'PAYLOAD_WEBHOOK_TIMEOUT', 30)
        max_retries = getattr(settings, 'PAYLOAD_WEBHOOK_RETRY_ATTEMPTS', 3)
        
        # Prepare the data to send
        payload_data = {
            'user_id': instance.user.id,
            'username': instance.user.username,
            'email': instance.user.email,
            'payload': instance.payLoadString,
            'created_at': instance.pk,
            'timestamp': instance.pk  # Using primary key as a simple identifier
        }
        print(payload_data)
        # Retry logic for better reliability
        for attempt in range(max_retries):
            try:
                # Send POST request to the external API
                response = requests.post(
                    target_url,
                    json=payload_data,
                    headers={
                        'Content-Type': 'application/json',
                        'User-Agent': 'FINFIRE-Webhook/1.0',
                        'X-FINFIRE-Version': '1.0',
                        'X-FINFIRE-User-ID': str(instance.user.id)
                    },
                    timeout=timeout
                )
                
                # Check if the request was successful
                if response.status_code in [200, 201, 202]:
                    print(f"✅ Successfully sent payload for user {instance.user.username} to {target_url}")
                    break  # Exit retry loop on success
                else:
                    print(f"⚠️ Failed to send payload for user {instance.user.username}. Status: {response.status_code}, Response: {response.text}")
                    if attempt < max_retries - 1:  # Don't sleep on the last attempt
                        import time
                        time.sleep(2 ** attempt)  # Exponential backoff: 1s, 2s, 4s
                        
            except requests.exceptions.Timeout:
                print(f"⏰ Timeout sending payload for user {instance.user.username} (attempt {attempt + 1}/{max_retries})")
                if attempt < max_retries - 1:
                    import time
                    time.sleep(2 ** attempt)
                    
            except requests.exceptions.ConnectionError:
                print(f"🔌 Connection error sending payload for user {instance.user.username} (attempt {attempt + 1}/{max_retries})")
                if attempt < max_retries - 1:
                    import time
                    time.sleep(2 ** attempt)
                    
            except requests.exceptions.RequestException as e:
                print(f"❌ Request error sending payload for user {instance.user.username}: {str(e)} (attempt {attempt + 1}/{max_retries})")
                if attempt < max_retries - 1:
                    import time
                    time.sleep(2 ** attempt)
        else:
            print(f"❌ All {max_retries} attempts failed to send payload for user {instance.user.username}")
            
    except Exception as e:
        print(f"💥 Unexpected error sending payload for user {instance.user.username}: {str(e)}")