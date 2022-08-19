from django_filters.rest_framework import (
    filters,
    FilterSet,
)

from post.models import Post


class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = ('is_draft', 'is_deleted', 'category')

    # tags = filters.ModelMultipleChoiceFilter(
    #     queryset=Tag.objects.all(),
    #     method='filter_tags'
    # )

    category = filters.CharFilter(
        field_name='category__title__in', method='filter_by_category'
    )

    @staticmethod
    def filter_by_category(queryset, field_name: str, value: str):
        """ Фильтрация по тегу
        """
        if value:
            queryset = queryset.filter(**{field_name: value.split(',')})
        return queryset.distinct()
