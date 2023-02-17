from django.db import models
from .type import Type
from django.contrib.auth.models import User


class PokemonManager(models.Manager):
    def create_pokemon(self, name, image_url, pokedex_number):
        pokemon = self.create(
            name=name, image_url=image_url, pokedex_number=pokedex_number
        )

        return pokemon


class Pokemon(models.Model):
    name = models.CharField(max_length=120)
    image_url = models.CharField(max_length=120)
    pokedex_number = models.PositiveBigIntegerField()
    types = models.ManyToManyField(Type)
    favorited_users = models.ManyToManyField(
        User, related_name="favorites", through="UserFavoritePokemon"
    )
    objects = PokemonManager()

    def __str_(self):
        return self.name
