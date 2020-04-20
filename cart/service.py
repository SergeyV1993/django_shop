from cart.models import Cart


def initialize_cart(request):
    if 'cart_id' in request.session:
        cart_id = request.session['cart_id']
        cart = Cart.objects.prefetch_related('items').get(id=cart_id)
        cart.save()
        request.session['total'] = cart.items.count()
    else:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.prefetch_related('items').get(id=cart_id)
    return cart
