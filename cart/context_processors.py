from .models import *


def cart(request):
    if 'cart_id' in request.session:
        cart = Cart.objects.prefetch_related('items__product').get(id=request.session['cart_id'])
        return {'cart': cart,
                'cart_total': cart.items.count(),
                'cart_total_sum': cart.cart_total_price
                }
    return {'cart': 0,
            'cart_total': 0,
            'cart_total_sum': 0,
            }
