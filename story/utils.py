from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    max_page_size = 10
    page_size = 10