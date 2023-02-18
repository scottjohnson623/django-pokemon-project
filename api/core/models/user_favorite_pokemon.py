from django.db import models
from django.contrib.auth.models import User
from .pokemon import Pokemon

class UserFavoritePokemon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    date_favorited = models.DateField(auto_now_add=True)
