from core.pagination import BasePagination


class PostPagination(BasePagination):
    default_limit = 10


class TagPagination(BasePagination):
    default_limit = 9999
