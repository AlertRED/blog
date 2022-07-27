from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from contact.serializers import ContactSerializer
from contact.models import Contact


class ContactView(viewsets.ModelViewSet):
    """ Получить токен авторизации
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
