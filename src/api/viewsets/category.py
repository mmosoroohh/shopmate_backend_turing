from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Category
from api.serializers import CategorySerializer
import logging

logger = logging.getLogger(__name__)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list: Return a list of categories
    retrieve: Return a category by ID.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_category_by_product(self, request, product_id):
        """
        Get the category of a particular product
        """
        # TODO: place the code here
        query = request.query_params.get(product_id)
        return Response(CategorySerializer(query).data)

    def get_categories_by_department(self, request, department_id):
        """
        Get a list of Categories of Department
        """
        # TODO: place the code here
        query = request.query_params.get(department_id)
        return Response(CategorySerializer(query).data)