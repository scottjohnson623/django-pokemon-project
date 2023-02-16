from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import PokemonSerializer, TypeSerializer
from .models import Pokemon, Type
from django.contrib.auth.models import User
class PokemonViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

class TypeViewset(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()

def logged_in_user(request):
    print(f'User {request.user}')
    print(f'User {request.user.is_authenticated}')
    return HttpResponse(request.user)
    return HttpResponse(None)