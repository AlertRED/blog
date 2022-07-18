from rest_framework import serializers
from .models import (Post, Tag)


class PostSerializer(serializers.ModelSerializer):

    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True,
    )

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'body', 'created',
            'updated', 'is_deleted', 'is_draft', 'tags',
        )
        read_only_fields = ('created', 'updated',)

    created = serializers.DateTimeField(
        input_formats='%d-%m-%Y',
        format='%d-%m-%Y',
        read_only=True,
    )
    updated = serializers.DateTimeField(
        input_formats='%d-%m-%Y',
        format='%d-%m-%Y',
        read_only=True,
    )
