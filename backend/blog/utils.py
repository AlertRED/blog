from datetime import datetime, timedelta
import pytz

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from blog import settings


class ExpiringTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise AuthenticationFailed('Invalid token.')

        if not token.user.is_active:
            raise AuthenticationFailed('User inactive or deleted.')

        # Time comparison
        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)

        if token.created < (utc_now - timedelta(hours=settings.TOKEN_LIFETIME)):
            raise AuthenticationFailed('Token has expired')

        return token.user, token


class BasicAPITestCase(APITestCase):

    def _auth(self, user):
        token_key = Token.objects.get_or_create(user=user)[0].key
        self.client.logout()
        self.client.force_authenticate(user, token_key)
        self._current_auth_user = user
        return token_key
