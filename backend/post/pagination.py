from core.pagination import BasePagination


class PostPagination(BasePagination):
    default_limit = 10


class CategoryPagination(BasePagination):
    default_limit = 9999
