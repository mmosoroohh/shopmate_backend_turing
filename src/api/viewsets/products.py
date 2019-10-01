import logging

from django.contrib.auth.models import AnonymousUser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from api.helpers.pagination import SetUserLimitOffsetPagination


from rest_framework.response import Response
from rest_framework.views import status

from api import errors
from api.models import Category, Product, Review
from api.serializers import ProductSerializer, ReviewSerializer

logger = logging.getLogger(__name__)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list: Return a list of products
    retrieve: Return a product by ID.
    """
    queryset = Product.objects.all().order_by('product_id')
    serializer_class = ProductSerializer
    pagination_class = SetUserLimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'description')

    @action(methods=['GET'], detail=False, url_path='search', url_name='Search products')
    def search(self, request, *args, **kwargs):
        """        
        Search products
        """
        return super().list(request, *args, **kwargs)

    def get_products_by_category(self, request, category_id):
        """
        Get a list of Products by Categories
        """
        # TODO: place the code here
        query = request.query_params.get(category_id)
        return Response(ProductSerializer(query).data)

    def get_products_by_department(self, request, department_id):
        """
        Get a list of Products of Departments
        """
        # TODO: place the code here
        query = request.query_params.get(department_id)
        return Response(ProductSerializer(query).data)

    @action(methods=['GET'], detail=True, url_path='details')
    def details(self, request, pk):
        """
        Get details of a Product
        """
        # TODO: place the code here
        query = request.query_params.get(pk)
        return Response(ProductSerializer(query).data)

    @action(methods=['GET'], detail=True, url_path='locations')
    def locations(self, request, pk):
        """
        Get locations of a Product
        """
        # TODO: place the code here
        query_list = Product.objects.all()
        query = request.query_params.get(pk)
        query_list = query_list.filter(location__icontains=query)
        return query_list

    @action(methods=['GET'], detail=True, url_path='reviews', url_name='List reviews')
    def reviews(self, request, pk):
        """
        Return a list of reviews
        """
        # TODO: place the code here
        query = request.query_params.get(pk)
        return Response(ReviewSerializer(query).data)


    @swagger_auto_schema(method='POST', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'review': openapi.Schema(type=openapi.TYPE_STRING, description='Review Text of Product', required=['true']),
            'rating': openapi.Schema(type=openapi.TYPE_INTEGER, description='Rating of Product', required=['true']),
        }
    ))
    @action(methods=['POST'], detail=True, url_path='review', url_name='Create review')
    def review(self, request, pk):
        """
        Create a new review
        """
        # TODO: place the code here
        data = request.data
        product_id = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(
            product_id, data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
