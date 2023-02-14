from django.core.management.base import BaseCommand
import requests
from core.models import Type

class Command(BaseCommand):
    help = 'Import pokemon types from the API'

    def handle(self, *args, **options):
            self.stdout.write(self.style.SUCCESS('Started'))
            url = 'https://pokeapi.co/api/v2/type'

            self.stdout.write(self.style.SUCCESS(url))
            request = requests.get(url).json()
            for type in request['results']:
                name = type['name']
                Type.objects.create_type(name=name)
                self.stdout.write(self.style.SUCCESS(f'Added type {name}'))

            
