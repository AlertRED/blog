from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
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

    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='title',
    )

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'body', 'created',
            'updated', 'is_deleted', 'is_draft', 'category',
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
