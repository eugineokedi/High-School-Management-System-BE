from flask_mail import Message
from app import mail

def send_email(subject, recipients, body):
    """Send an email using Flask-Mail."""
    msg = Message(subject, recipients=recipients, body=body)
    mail.send(msg)

def send_password_reset_email(user_email, token):
    """Send a password reset email with a token."""
    subject = "Password Reset Request"
    body = f"To reset your password, click the following link: https://example.com/reset-password/{token}"
    send_email(subject, [user_email], body)
