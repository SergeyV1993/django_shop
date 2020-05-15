from project.celery import app
from django.core.mail import send_mail


@app.task(default_retry_delay=2 * 60)
def send_mail_login(username):
    subject = 'Авторизация на сайте'
    message = 'Выполнен вход под именем {}'.format(username)
    sender = send_mail(subject, message, 'example@gmail.com', ['example333@yandex.ru'])
    return sender


