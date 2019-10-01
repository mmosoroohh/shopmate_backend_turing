from rest_framework import viewsets
from rest_framework.response import Response

from api.models import ShippingRegion
from api.serializers import ShippingRegionSerializer, ShippingSerializer
import logging

logger = logging.getLogger(__name__)


class ShippingRegionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list: Get All ShippingRegions
    retrieve: Get ShippingRegion by ID
    """
    queryset = ShippingRegion.objects.all()
    serializer_class = ShippingRegionSerializer

    def get(self, request, shopping_region_id):
        """
        Get a list of shipping for a region
        """
        # TODO: place the code here
        query = request.query_params.get(shopping_region_id)
        return Response(ShippingSerializer(query).data)
