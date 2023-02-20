from django.core.management.base import BaseCommand
import requests
from core.models import Pokemon, Type


class Command(BaseCommand):
    help = "Import pokemon from the API"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Started"))
        more_pokemon_exist = True
        url = "https://pokeapi.co/api/v2/pokemon/"
        while more_pokemon_exist:
            request = requests.get(url).json()
            for pokemon in request["results"]:
                name = pokemon["name"]
                pokemon_request = requests.get(
                    f"https://pokeapi.co/api/v2/pokemon/{name}"
                ).json()
                new_pokemon = Pokemon.objects.create_pokemon(
                    pokemon["name"],
                    pokemon_request["sprites"]["front_default"],
                    pokedex_number=pokemon_request["id"],
                )
                for type in pokemon_request["types"]:
                    type_model = Type.objects.get(name=type["type"]["name"])
                    new_pokemon.types.add(type_model)
                self.stdout.write(self.style.SUCCESS(f"Added pokemon {name}"))
            if request["next"]:
                url = request["next"]
            else:
                more_pokemon_exist = False
