from django.shortcuts import render
from .forms import *
from cart.models import Cart


def checkout(request):
    form = OrderForm(request.POST or None)
    return render(request, 'order/checkout.html', locals())


def make_order(request):
    cart = Cart.objects.prefetch_related('items__product').get(id=request.session['cart_id'])

    if request.method == "POST":
        form = OrderForm(request.POST or None)
        if form.is_valid():
            new_form = form.save()
            order = Order.objects.select_related('user').latest('create')
            order.user = request.user
            products_in_cart = cart.items.all()
            for item in products_in_cart:
                ProductInOrder.objects.create(order=order,
                                              product=item.product,
                                              number_of_product=item.number_of_product,
                                              price_one_item=item.product.price,
                                              total_price=item.total_item_price,
                                              is_active=True)
            order.total_price = cart.cart_total_price
            order.save()
    else:
        form = OrderForm()

    del request.session['cart_id']
    del request.session['total']
    return render(request, 'order/thanks.html', locals())



