from django.http import JsonResponse
from .service import initialize_cart
from discount.forms import *
from .models import *
from django.views.generic import *


class CartView(FormView):
    form_class = DiscountForm
    template_name = 'cart/cart.html'

    def get_context_data(self):
        context = super(CartView, self).get_context_data()
        if 'cart_id' in self.request.session:
            form = self.form_class(self.request.POST or None)
            context['form'] = form
        return context


class AddToCartView(View):

    def post(self, request):
        cart = initialize_cart(request)
        product_id = request.POST.get("product_id")
        qty = int(request.POST.get("quantity"))
        product = Product.objects.select_related('type').get(id=product_id)

        new_item, _ = CartItem.objects.select_related('product').get_or_create(product=product,
                                                                               number_of_product=qty)
        new_item.save()

        if new_item not in cart.items.all():
            cart.items.add(new_item)
            cart.cart_total_price += new_item.total_item_price
            cart.save()

        if request.is_ajax():
            return JsonResponse({
                'cart_total': cart.items.count(),
                'cart_total_sum': cart.cart_total_price,
                'cart_total_summ': cart.cart_total_price,  # для разных id в html, так как нельзя юзать сразу несколько

                # """инфа для шапки на странице"""

                'adding_cart_item': product.name,
                'quantity': qty,
                'price_items': product.price * qty,
                'cart_total_price': cart.cart_total_price
            })


class RemoveFromCartView(View):

    def post(self, request):
        cart = Cart.objects.prefetch_related('items__product').get(id=request.session['cart_id'])
        product_id = request.POST.get("product_id")
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


'''
# Реализация через функции
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def cart_view(request):
    if 'cart_id' in request.session:
        form = DiscountForm(request.POST or None)
        context = {
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
    cart = Cart.objects.prefetch_related('items__product').get(id=request.session['cart_id'])
    product_id = request.POST.get("product_id")
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
'''
