from rest_framework import serializers

from core.models import KeyValue


class KeyValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = KeyValue
        fields = '__all__'
