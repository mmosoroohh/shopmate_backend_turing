from rest_framework import viewsets

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