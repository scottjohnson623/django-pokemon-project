from rest_framework import serializers
from .models import Pokemon, Type

class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ("id", "name")

class PokemonSerializer(serializers.ModelSerializer):
    types = TypeSerializer(read_only=True, many=True)
    class Meta:
        model = Pokemon
        fields = ("id", "name", "image_url", "types", "pokedex_number")
