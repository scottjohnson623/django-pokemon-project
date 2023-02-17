from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import PokemonSerializer, TypeSerializer, UserSerializer
from .models import Pokemon, Type, UserFavoritePokemon


class PokemonViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()


class TypeViewset(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()

@api_view(['GET'])
def logged_in_user_view(request):
    if request.user.is_authenticated:
        return Response(UserSerializer(request.user).data)
    return Response()

@api_view(['POST'])
def favorite_pokemon(request):
    data = request.data
    print(data)
    UserFavoritePokemon.objects.get_or_create(user=request.user, pokemon=Pokemon.objects.get(id=data['pokemon_id']))
    
    return Response(status= status.HTTP_200_OK)