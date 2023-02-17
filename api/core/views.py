from django.http.response import JsonResponse
from rest_framework import viewsets
from .serializers import PokemonSerializer, TypeSerializer, UserSerializer
from .models import Pokemon, Type


class PokemonViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()


class TypeViewset(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()


def logged_in_user_view(request):
    if request.user.is_authenticated:
        return JsonResponse(UserSerializer(request.user).data)
    return JsonResponse()
