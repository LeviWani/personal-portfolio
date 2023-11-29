from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from twilio.rest import Client
from django.contrib import messages
from django.shortcuts import render, redirect


import os

def homepage(request):
    return render(request, 'index.html')

def aboutme(request):
    return render(request, 'aboutme.html')

def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_message = request.POST.get('message')
        try:
            account_sid = 'twilio-sid'
            auth_token = 'twilio-authentication-token'
            client = Client(account_sid, auth_token)

            message = client.messages \
                    .create(
                        body="from user : " +user_name + ''' 
                    
                        ''' + user_message,

                        from_=user_email, 
                        to='your-twilio-number'
                    )
            messages.success(request, 'Your message was successfully submitted.')
            return render(request, 'contact.html')
        except:
             messages.success(request, 'invalid number please try again.')
             return render(request, 'contact.html')

    # Render the contact.html template for GET requests
    return render(request, 'contact.html')
