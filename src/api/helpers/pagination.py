import math

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status


class SetUserLimitOffsetPagination(LimitOffsetPagination):
    """Define pagination limit."""

    default_limit = 20

    def get_paginated_response(self, data):
        """Create and return paginated response."""
        current_page = math.ceil((self.offset + self.limit) / self.limit)
        return Response({
            "currentPage": current_page,
            "currentPageSize": self.limit,
            "totalPages": math.ceil(self.count / self.limit),
            "totalRecords": self.count,
            "links": {
                "next_page": self.get_next_link(),
                "previous_page": self.get_previous_link()
            },
            "data": data
        }, status=status.HTTP_200_OK)