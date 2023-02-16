from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet, TypeViewset, logged_in_user_view

router = DefaultRouter()
router.register(r'pokemon', PokemonViewSet)
router.register(r'types', TypeViewset)
urlpatterns = [
    path("", include(router.urls)),
    path("me", logged_in_user_view)
]
