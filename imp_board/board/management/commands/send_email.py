from django.core.management.base import BaseCommand
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        send_mail(
        'Запрошення до оціцнювання',
        'Вітаємо. Це тестове повідомлення для перевірки роботи',
        'volodymyrpetriv2207@gmail.com',
        ['volodymyrpetriv2207@gmail.com'],
    )
