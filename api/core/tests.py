from django.test import TestCase, Client
from django.contrib.auth.models import User

from .models import Pokemon

class PokemonModelTests(TestCase):

    def test_add_favorite_succeeds(self):
        pokemon = Pokemon.objects.create_pokemon(name="test", image_url="test_url", pokedex_number=1)
        user = User.objects.create(username='Scott', password='testtest', email='testemail@testdomain.com')
        pokemon.favorited_users.add(user)
        self.assertEqual(pokemon.favorited_users.get(), user)

