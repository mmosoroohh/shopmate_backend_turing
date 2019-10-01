import uuid

from django.utils import timezone
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from api import errors
from api.models import ShoppingCart
from api.serializers import ShoppingcartSerializer, ProductSerializer
import logging

logger = logging.getLogger(__name__)


@api_view(['GET'])
def generate_cart_id(request):
    """
    Generate the unique CART ID 
    """
    logger.debug("Generating cart ID")
    return Response({"cart_id": uuid.uuid4()})


@swagger_auto_schema(method='POST', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'cart_id': openapi.Schema(type=openapi.TYPE_STRING, description='Cart ID.', required=['true']),
        'product_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Product ID.', required=['true']),
        'attributes': openapi.Schema(type=openapi.TYPE_STRING, description='Attributes of Product.', required=['true']),
    }
))
@api_view(['POST'])
def add_products(request):
    """
    Add a Product in the cart
    """
    # TODO: place the code here
    logger.debug("Add Product to Shopping Cart")
    serializer = ShoppingcartSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['GET'])
def get_products(request, cart_id):
    """
    Get List of Products in Shopping Cart
    """
    # TODO: place the code here
    query = request.query_params.get(str(cart_id))
    return Response(ShoppingcartSerializer(query).data)


@swagger_auto_schema(method='PUT', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description='Item Quantity.', required=['true'])
    }
))
@api_view(['PUT'])
def update_quantity(request, item_id):
    """
    Update the cart by item
    """
    logger.debug("Updating quantity")
    # TODO: place the code here
    item = request.data.get(item_id)
    serializer = ShoppingcartSerializer(
        item, data=request.data, partial=True
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def empty_cart(request, cart_id):
    """
    Empty cart
    """
    # TODO: place the code here
    cart = ShoppingCart.objects.get(cart_id=cart_id)
    cart.delete()
    return Response({'message': 'Shopping cart with id `{}` has been delete'.format(cart_id)})


@api_view(['DELETE'])
def remove_product(request, item_id):
    """
    Remove a product in the cart
    """
    # TODO: place the code here
    cart = ShoppingCart.objects.get(item_id=item_id)
    cart.delete()
    return Response({'message': 'Shopping cart with id `{}` has been delete'.format(item_id)})



@api_view(['GET'])
def move_to_cart(request, item_id):
    """
    Move a product to cart
    """
    # TODO: place the code here
    query = request.query_params.get(item_id=item_id)
    return Response(ShoppingcartSerializer(query).data)



@api_view(['GET'])
def total_amount(request, cart_id):
    """
    Return a total Amount from Cart
    """
    # TODO: place the code here


@api_view(['GET'])
def save_for_later(request, item_id):
    """
    Save a Product for latter
    """
    # TODO: place the code here



@api_view(['GET'])
def get_saved_products(request, cart_id):
    """
    Get saved Products 
    """
    # TODO: place the code here
