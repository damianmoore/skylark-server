from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    help = 'Sent a test message via the live server'

    def handle(self, *args, **options):
        params = {
            'title':    'This is a test!',
            'body':     'Hope you can see it',
            'color':    '#333333',
        }
        requests.post('https://skylark.epixstudios.co.uk/webhook/test/', params=params)
