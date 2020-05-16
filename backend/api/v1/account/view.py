from rest_framework.mixins import DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from rest_framework.response import Response

from backend.orders.models import Order
from .serializers import AccountViewSerializer


class AccountViewSet(ModelViewSet):
    serializer_class = AccountViewSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Order.objects.select_related('status').filter(user=self.request.user).order_by(
            '-id').prefetch_related('productinorder_set__product')


class AccountDeleteViewSet(DestroyModelMixin, GenericViewSet):
    serializer_class = AccountViewSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        order_objects = self.model.objects.select_related('status').filter(user=self.request.user).all()
        return order_objects

    def destroy(self, request, *args, **kwargs):
        orders_obj = self.get_object()
        user = self.request.user
        orders_obj.delete()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
