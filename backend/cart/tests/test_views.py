import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from backend.cart.models import *
from backend.products.models import *
from django.urls import reverse


class CartViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        """Создание тестового пользователя"""
        test_user1 = User.objects.create_user(username='testuser', password='12345')
        test_user1.save()

        number_of_products = 2

        """Создаем 2 продукта"""
        for product in range(number_of_products):
            Product.objects.create(
                name='test %s' % product,
                price=10.00,
                create=datetime.datetime.now(),
                update=datetime.datetime.now()
            )

        """Создаем 2 позиции в корзину"""
        for cart_item in range(1, 3):
            item = CartItem.objects.create(
                product=Product.objects.get(id=cart_item),
                number_of_product=2
            )
            item.save()  # сохраняю, чтобы сумма пересчиталась за позицию
            item.cart_set.all()

        """Создаю саму корзину"""
        cart = Cart.objects.create()
        cart.cartitem_set.set(CartItem.objects.all())  # необходимо для поля ManyToMany
        cart.save()

    """Общее отображение урла"""
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/cart/')

        self.assertEqual(response.status_code, 200)

    """Отображение урла по имени"""
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('cart_view'))

        self.assertEqual(response.status_code, 200)

    """Корректное отображение темплэйта"""
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('cart_view'))

        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_count_items_in_cart(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('cart_view'))
        print(response.context)


'''
    def test_count_orders_for_user(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('account'))

        self.assertEqual(str(response.context['user']), 'testuser')

        get_user = User.objects.get(username=str(response.context['user']))
        get_orders = Order.objects.filter(user=get_user)

        self.assertEqual(len(get_orders), 10)
        
'''

