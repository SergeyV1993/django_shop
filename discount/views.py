from .forms import *
from django.contrib import messages
from cart.views import initialize_cart
from django.shortcuts import render
import requests
import ast
import os


def post_request(cart, code, amount_cart, cookie):
    url = "http://127.0.0.1:8080/api/v1/discount_cart"
    body = {"cart": cart, "code": code, "amount_cart": float(amount_cart)}
    headers = {'Content-Type': 'application/json',
               # 'Authorization': os.environ['TOKEN_AUTH'],
               'Authorization': 'Token 07237f5ec1bb992f273e8f12db5f9c6924b86476',
               'Connection': 'keep-alive'
               }
    response = requests.post(url, json=body, headers=headers, cookies=cookie)
    result = ast.literal_eval(response.json())
    return result


def discount_view(request):
    cart = initialize_cart(request)
    form = DiscountForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():

            code = form.cleaned_data['code']
            cookies = request.COOKIES
            response = post_request(cart.id, code, cart.cart_total_price, cookies)

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
