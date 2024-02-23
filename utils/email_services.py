# email_services.py
# email_tasks.py

import os
from django.core.mail import send_mail
from django.template.loader import render_to_string
from celery import shared_task

FROM_EMAIL = os.environ.get("FROM_EMAIL")

@shared_task(name='send_verification_email')
def send_verification(user, verification_url):
    """
    Send verification email asynchronously using Celery.
    
    Args:
        user (User): The user object.
        verification_url (str): The URL for email verification.
    """
    subject = 'Activate your account'
    message = render_to_string('authentications/verification_email.txt', {'user': user, 'verification_url': verification_url})
    send_mail(subject, message, FROM_EMAIL, [user.email])
