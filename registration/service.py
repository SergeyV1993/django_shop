from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

account_activation_token = PasswordResetTokenGenerator()


def send_email_for_confirm_registration(user, current_site, email_address):
    mail_subject = 'Activate Your account.'
    message = render_to_string('registration/account_activate_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    to_email = email_address

    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()
