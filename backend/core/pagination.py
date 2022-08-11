from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param


class BasePagination(pagination.LimitOffsetPagination):

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'count': self.count,
            'results': data,
        })

    # def get_next_link(self):

    #     url = self.request.build_absolute_uri()
    #     url = replace_query_param(url, self.limit_query_param, self.limit)

    #     offset = self.offset + self.limit
    #     return replace_query_param(url, self.offset_query_param, offset)
