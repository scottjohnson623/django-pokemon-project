from django.urls import path, include
from rest_framework.routers import DefaultRouter
import .views

router = DefaultRouter()
router.register(r"pokemon", PokemonViewSet)
router.register(r"types", TypeViewset)
urlpatterns = [
    path("", include(router.urls)),
    path("me", views.logged_in_user_view, name="me"),
    path(f"pokemon/favorite", views.favorite_pokemon, name="favorite_pokemon"),
    path(f"pokemon/unfavorite", views.unfavorite_pokemon, name="unfavorite_pokemon"),
    path(f"favorites", views.user_favorite_pokemon_view, name"favorites"),
]
