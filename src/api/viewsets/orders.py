from django.contrib.auth.models import AnonymousUser
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import render_to_string
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api import errors
from api.models import Orders, OrderDetail
from api.serializers import OrdersSaveSerializer, OrdersSerializer, OrdersDetailSerializer
import logging

from turing_backend import settings

logger = logging.getLogger(__name__)


@swagger_auto_schema(method='POST', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'cart_id': openapi.Schema(type=openapi.TYPE_STRING, description='Cart ID.', required=['true']),
        'shipping_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Shipping ID.', required=['true']),
        'tax_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Tax ID.', required=['true']),
    }
))
@api_view(['POST'])
def create_order(request):
    """
    Create a Order
    """
    # TODO: place the code here
    logger.debug("Creating a customer")
    order = Orders.objects.create()
    serializer = OrdersSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
            'order': serializer.data['order_id']
        }
        return Response(data)
    return Response(serializer.errors)


@api_view(['GET'])
def order(request, order_id):
    """
    Get Info about Order
    """
    # TODO: place the code here
    try:
        order_info = Orders.objects.get(order_id=order_id)
        serializer = OrdersSerializer(
            order_info, context={'request': request})
        return Response(serializer.data)
    except Orders.DoesNotExist:
        data = {
            'message': 'Order with that ID does not exist'
        }
        return Response(data)


@api_view(['GET'])
def order_details(request, order_id):
    """
    Get Info about Order
    """
    logger.debug("Getting detail info")
    # TODO: place the code here
    try:
        order = OrderDetail.objects.get(order_id=order_id)
        serializer = OrdersDetailSerializer(
            order, context={'request': request})
        return Response(serializer.data)
    except OrderDetail.DoesNotExist:
        data = {
            'message': 'Order ID passed does not exists.'
        }
        return Response(data)


@api_view(['GET'])
def orders(request):
    """
    Get orders by Customer
    """
    # TODO: place the code here
    if AnonymousUser:
        return Response({'message': "Please login to complete this action"})
    orders = Orders.objects.all()
    customer_orders = request.user.orders.all().values()
    serializer = OrdersSerializer(customer_orders, many=True)
    return Response({"orders": serializer.data})


@api_view(['GET'])
def test(request):
    context = {
        'order_id': 12334,
        'username': 'John Doe'
    }
    return render(request, 'notify_order.html', context)
