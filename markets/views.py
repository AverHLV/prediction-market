from rest_framework import viewsets, mixins, permissions

from .models import Market, Asset, Order
from .serializers import MarketSerializer, AssetSerializer, OrderSerializer


class MarketViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = [permissions.IsAuthenticated]


class AssetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
