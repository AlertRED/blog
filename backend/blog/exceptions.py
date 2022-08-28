from rest_framework.views import exception_handler
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    if isinstance(exc, NotAuthenticated):
        return Response(
            {'detail': 'Не были переданы данные для аутентификации'},
            status=401,
        )
    return exception_handler(exc, context)
