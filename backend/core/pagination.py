from rest_framework import pagination
from rest_framework.response import Response


class BasePagination(pagination.LimitOffsetPagination):

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'lims': self.limit,
            'count': self.count,
            'results': data,
        })
