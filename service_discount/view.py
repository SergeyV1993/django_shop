from rest_framework.views import APIView
from rest_framework.response import Response
from discount.models import *
from .serializers import DiscountSerializer


class Discounts(APIView):

    def post(self, request):
        code = DiscountSerializer(data=request.data)
        discount = DiscountCart.objects.select_related('cart').get(code=code)
        if discount.status and discount.valid_date_end > datetime.now(timezone.utc):
            discount.cart, discount.status = cart, False
            discount.save(update_fields=["cart", "status"])

            new_sum = discount.cart
            new_sum.cart_total_price -= discount.nominal
            new_sum.save(update_fields=["cart_total_price"])
        return Response({"status": "good"})