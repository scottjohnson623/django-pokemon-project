from django.db import models
from django.contrib.auth.models import User
from .pokemon import Pokemon


class UserFavoritePokemonManager(models.Manager):
    def create_pokemon(self, name, image_url, pokedex_number):
        pokemon = self.create(
            name=name, image_url=image_url, pokedex_number=pokedex_number
        )

        return pokemon


class UserFavoritePokemon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    date_favorited = models.DateField(auto_now_add=True)
    objects = UserFavoritePokemonManager()
