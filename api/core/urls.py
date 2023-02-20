from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"pokemon", PokemonViewSet)
router.register(r"types", TypeViewset)
urlpatterns = [
    path("", include(router.urls)),
    path("me", logged_in_user_view, name="me"),
    path(f"pokemon/favorite", favorite_pokemon, name="favorite_pokemon"),
    path(f"pokemon/unfavorite", unfavorite_pokemon, name="unfavorite_pokemon"),
    path(f"favorites", user_favorite_pokemon_view, name="favorites"),
]
