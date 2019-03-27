from cart.views import initialize_cart


def cart(request):
    cart = initialize_cart(request)
    return {'cart': cart,
            'cart_total': cart.items.count(),
            'cart_total_sum': cart.cart_total_price
            }
