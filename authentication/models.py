from django.db import models
import os
from twilio.rest import Client

# Create your models here.

""" 
class Message(models.Model):
    user_name = models.CharField(max_length=100)
    user_Message = models.CharField(max_length=100)
    user_number = models.CharField(max_length=12)

    def __str__(self):
        return self.user_name   

    def save(self, *args, **kwargs):
        account_sid = os.environ['AC52fff2b98d65a436a69e02167c33d00c']
        auth_token = os.environ['fd28c200b94f3cf776104ee9e5fb8929']
        client = Client(account_sid, auth_token)

        message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+13524159819', 
                     to='+917880226510'
                 )
     
    
"""
