from rest_framework import serializers
from .models import Post, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = (
            'id', 'title', 'created', 'updated',
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


class PostSerializer(serializers.ModelSerializer):

    tags = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'body', 'created',
            'updated', 'is_deleted', 'is_draft', 'tags',
        )
        read_only_fields = ('created', 'updated',)

    def get_tags(self, obj):
        return obj.tags.values_list('title', flat=True)

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



