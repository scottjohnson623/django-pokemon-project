from rest_framework import viewsets
from ..serializers import PokemonSerializer
from ..models import Pokemon


class PokemonViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()
