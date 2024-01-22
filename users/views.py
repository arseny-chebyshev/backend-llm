from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.models import User, DiscordUser
from users.serializers import UserSerializer, DiscordUserSerializer


class UserSerializer(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class DiscordUserViewSet(viewsets.ModelViewSet):
    queryset = DiscordUser.objects.all()
    serializer_class = DiscordUserSerializer
    permission_classes = [IsAuthenticated]
