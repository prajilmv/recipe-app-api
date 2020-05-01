from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerailizer, AuthTokenSerializer

class CreateUserView(generics.CreateAPIView):

    serializer_class = UserSerailizer


class CreateToeknView(ObtainAuthToken):

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
