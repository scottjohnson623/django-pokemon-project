from django.shortcuts import render

from rest_framework import viewsets
from .serializers import PokemonSerializer, TypeSerializer
from .models import Pokemon, Type

class PokemonViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

class TypeViewset(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
