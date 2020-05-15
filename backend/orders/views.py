from django.shortcuts import render
from .forms import *
from backend.cart.models import Cart
from django.views.generic import *


class CheckoutView(FormView):
    form_class = OrderForm
    template_name = 'order/checkout.html'

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        form = self.form_class(self.request.POST or None)
        context['form'] = form
        return context


class CreateOrder(CreateView):
    form_class = OrderForm
    success_url = 'order/thanks.html'

    def form_valid(self, form):
        form.save()
        return super(CreateOrder, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        super(CreateOrder, self).get(request)
        form = self.form_class()
        context = {
            'form': form,
        }
        return render(request, self.success_url, context)

    def post(self, request, *args, **kwargs):
        super(CreateOrder, self).post(request)

        if 'cart_id' not in self.request.session:
            return render(self.request, 'shop/shop.html')
        cart = Cart.objects.prefetch_related('items__product').get(id=request.session['cart_id'])

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
        context = {
            'cart': cart,
            'order': order,
        }
        del request.session['cart_id']
        return render(request, self.success_url, context)


'''  
# реализация через функцию
  
def checkout(request):
    form = OrderForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'order/checkout.html', context)

def make_order(request):
    if 'cart_id' not in request.session:
        return render(request, 'shop/shop.html')
    cart = Cart.objects.prefetch_related('items__product').get(id=request.session['cart_id'])

    if request.method == "POST":
        form = OrderForm(request.POST or None)
        if form.is_valid():
            form.save()
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
            context = {
                'cart': cart,
                'order': order,
            }
            del request.session['cart_id']
            return render(request, 'order/thanks.html', context)

    else:
        form = OrderForm()
        context = {
            'form': form,
        }
        return render(request, 'order/thanks.html', context)
'''


