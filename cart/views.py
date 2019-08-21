from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from discount.forms import *
from . models import *


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


@csrf_exempt
def cart_view(request):
    if 'cart_id' in request.session:
        cart = Cart.objects.prefetch_related('items').get(id=request.session['cart_id'])
        form = DiscountForm(request.POST or None)
        context = {
            'cart': cart,
            'form': form
        }
        return render(request, 'cart/cart.html', context)
    return render(request, 'cart/cart.html')


@csrf_exempt
def add_to_cart(request):
    cart = initialize_cart(request)
    product_id = request.POST.get("product_id")
    product = Product.objects.select_related('type').get(id=product_id)
    qty = int(request.POST.get("quantity"))
    new_item, _ = CartItem.objects.select_related('product').get_or_create(product=product,
                                                                           number_of_product=qty)
    new_item.save()

    if new_item not in cart.items.all():
        cart.items.add(new_item)
        cart.cart_total_price += new_item.total_item_price
        cart.save()
    return JsonResponse({
        'cart_total': cart.items.count(),
        'cart_total_sum': cart.cart_total_price,
        'cart_total_summ': cart.cart_total_price
        })


@csrf_exempt
def remove_from_cart(request):
    cart = Cart.objects.prefetch_related('items').get(id=request.session['cart_id'])
    product_id = request.GET.get("product_id")
    product = Product.objects.select_related('type').get(id=product_id)

    for cart_item in cart.items.all():
        if cart_item.product == product:
            cart.items.remove(cart_item)
            cart.cart_total_price -= cart_item.total_item_price
            cart.save()
    return JsonResponse({
        'cart_total': cart.items.count(),
        'cart_total_sum': cart.cart_total_price,
        'cart_sum': cart.cart_total_price,
        'cart_total_summ': cart.cart_total_price
    })


