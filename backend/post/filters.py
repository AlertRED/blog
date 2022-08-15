from django_filters.rest_framework import (
    filters,
    FilterSet,
)

from post.models import Post


class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = ('is_draft', 'is_deleted', 'tag')

    # tags = filters.ModelMultipleChoiceFilter(
    #     queryset=Tag.objects.all(),
    #     method='filter_tags'
    # )

    tag = filters.CharFilter(
        field_name='tags__title__in', method='filter_by_tag'
    )

    @staticmethod
    def filter_by_tag(queryset, field_name: str, value: str):
        """ Фильтрация по тегу
        """
        if value:
            queryset = queryset.filter(**{field_name: value.split(',')})
        return queryset.distinct()
