from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import PokemonSerializer, TypeSerializer, UserSerializer
from .models import Pokemon, Type, UserFavoritePokemon


class PokemonViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()


class TypeViewset(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()


@api_view(["GET"])
@renderer_classes((JSONRenderer,))
def logged_in_user_view(request):
    if request.user.is_authenticated:
        return Response(UserSerializer(request.user).data)
    return Response()


@api_view(["GET"])
@renderer_classes((JSONRenderer,))
@permission_classes((IsAuthenticated,))
def user_favorite_pokemon_view(request):
    pokemon = Pokemon.objects.filter(favorited_users=request.user)
    return Response(PokemonSerializer(pokemon, many=True).data)


@api_view(["POST"])
@renderer_classes((JSONRenderer,))
@permission_classes((IsAuthenticated,))
def favorite_pokemon(request):
    data = request.data
    UserFavoritePokemon.objects.get_or_create(
        user=request.user, pokemon=Pokemon.objects.get(id=data["pokemon_id"])
    )
    return Response(status=status.HTTP_200_OK)


@api_view(["POST"])
@renderer_classes((JSONRenderer,))
@permission_classes((IsAuthenticated,))
def unfavorite_pokemon(request):
    data = request.data
    UserFavoritePokemon.objects.filter(
        user=request.user, pokemon=Pokemon.objects.get(id=data["pokemon_id"])
    ).delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
