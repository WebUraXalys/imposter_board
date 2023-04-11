from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        print(settings.EMAIL_HOST_USER)
        print(settings.EMAIL_HOST_PASSWORD)
        return send_mail(
        'Invitation',
        'Вітаємо. Це тестове повідомлення для перевірки роботи',
        'volodymyrpetriv2207@gmail.com',
        ['etrikodoku@gmail.com'],
    )
