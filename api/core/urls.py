from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet, TypeViewset

router = DefaultRouter()
router.register(r'pokemon', PokemonViewSet)
router.register(r'types', TypeViewset)

urlpatterns = [
    path("", include(router.urls))
]
