from rest_framework.mixins import DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from rest_framework.response import Response

from backend.account.models import Account
from .serializers import AccountViewSerializer


class AccountViewSet(ModelViewSet):
    serializer_class = AccountViewSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Account.objects.prefetch_related('order_set__productinorder_set__product') \
            .prefetch_related('order_set__status') \
            .get_or_create(user=self.request.user)


class AccountDeleteViewSet(DestroyModelMixin, GenericViewSet):
    serializer_class = AccountViewSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        account_object = Account.objects.get(user=self.request.user)
        return account_object

    def destroy(self, request, *args, **kwargs):
        orders_obj = self.get_object()
        user = self.request.user
        orders_obj.delete()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
