from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from datetime import datetime
from .models import *

@shared_task(name='email_notification')
def send_email_task(subject, body, emailaddress):        
    email = EmailMessage(subject, body, to=[emailaddress])
    email.send()
    return emailaddress