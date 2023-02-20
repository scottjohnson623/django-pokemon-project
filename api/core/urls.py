from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PokemonViewSet,
    TypeViewset,
    logged_in_user_view,
    favorite_pokemon,
    unfavorite_pokemon,
    user_favorite_pokemon_view,
)

router = DefaultRouter()
router.register(r"pokemon", PokemonViewSet)
router.register(r"types", TypeViewset)
urlpatterns = [
    path("", include(router.urls)),
    path("me", logged_in_user_view),
    path(f"favorite_pokemon", favorite_pokemon),
    path(f"unfavorite_pokemon", unfavorite_pokemon),
    path(f"favorites", user_favorite_pokemon_view),
]
