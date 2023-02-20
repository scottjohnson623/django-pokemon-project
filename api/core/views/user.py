from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer
from ..serializers import UserSerializer

@api_view(["GET"])
@renderer_classes((JSONRenderer,))
def logged_in_user_view(request):
    if request.user.is_authenticated:
        return Response(UserSerializer(request.user).data)
    return Response()