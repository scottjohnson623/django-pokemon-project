from rest_framework import viewsets
from ..serializers import TypeSerializer
from ..models import Type


class TypeViewset(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
