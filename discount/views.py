from .forms import *
from django.contrib import messages
from cart.views import initialize_cart
from django.shortcuts import render
import requests
import os
from django.views.generic import *


class DiscountView(FormView):
    form_class = DiscountForm
    success_url = 'cart/cart.html'

    def post_request(self, cart, code, amount_cart, cookie):
        url = "http://127.0.0.1:8080/api/v1/discount_cart"
        body = {"cart": cart, "code": code, "amount_cart": float(amount_cart)}
        headers = {'Content-Type': 'application/json',
                   # 'Authorization': os.environ['TOKEN_AUTH'],
                   'Authorization': 'Token 07237f5ec1bb992f273e8f12db5f9c6924b86476',
                   'Connection': 'keep-alive'
                   }
        response = requests.post(url, json=body, headers=headers, cookies=cookie)
        return response

    def form_valid(self, form):
        cart = initialize_cart(self.request)
        code = form.cleaned_data['code']
        try:
            response = self.post_request(cart.id, code, cart.cart_total_price, self.request.COOKIES)
            response_data = response.json()

            if response.status_code == 200:
                if cart.id == response_data['cart']:
                    cart.cart_total_price = response_data['amount_cart']
                    cart.save(update_fields=["cart_total_price"])
                else:
                    messages.error(self.request, 'Ошибка с корзиной')
            elif response.status_code == 403:
                messages.error(self.request, 'Код уже недействителен или использован')
            elif response.status_code == 400:
                messages.error(self.request, 'Промокод не корректен')
            elif response.status_code == 404:
                messages.error(self.request, 'Такого промокода не существует')
            elif response.status_code == 500:
                messages.error(self.request, 'Сервис временно недоступен')
        except:
            messages.error(self.request, 'Сервис временно недоступен')

        context = {
            'cart': cart,
            'form': form,
        }
        return render(self.request, 'cart/cart.html', context)


'''
# реализация с помощью функции
def discount_view(request):
    cart = initialize_cart(request)
    form = DiscountForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():

            code = form.cleaned_data['code']
            response = post_request(cart.id, code, cart.cart_total_price, request.COOKIES)

            if 'status' not in response:
                if cart.id == response['cart']:
                    cart.cart_total_price = response['amount_cart']
                    cart.save(update_fields=["cart_total_price"])
            elif response['status'] == 'Error':
                messages.error(request, 'Код уже недействителен или использован')
            elif response['status'] == 'Not Valid':
                messages.error(request, 'Промокод не корректен')
            elif response['status'] == 'Code does not exist':
                messages.error(request, 'Такого промокода не существует')
    else:
        form = DiscountForm()

    context = {
        'cart': cart,
        'form': form,
    }
    return render(request, 'cart/cart.html', context)
'''