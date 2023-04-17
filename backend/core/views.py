from datetime import datetime
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.serisalizers import KeyValueSerializer
from core.models import KeyValue
from blog import settings


class AuthView(ObtainAuthToken):
    """ Получить токен авторизации
    """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        if not created:
            token.created = datetime.utcnow()
            token.save()

        return Response({
            'token': token.key,
            'lifetime': settings.TOKEN_LIFETIME,
        })


class KeyValueView(viewsets.ModelViewSet):
    """ Получить токен авторизации
    """
    serializer_class = KeyValueSerializer
    queryset = KeyValue.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
