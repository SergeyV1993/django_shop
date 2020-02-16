import datetime
from django.test import TestCase
from cart.models import *
from products.models import *


class CartModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

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
        cart.items.set(CartItem.objects.all())  # необходимо для поля ManyToMany
        cart.save()

    """Проверяем название поля cart_total_price"""
    def test_cart_total_price_label(self):
        cart = Cart.objects.get(id=1)
        field_label = cart._meta.get_field('cart_total_price').verbose_name

        self.assertEquals(field_label, 'Сумма')

    """Проверяем максимальную длину поля cart_total_price до дробной части"""
    def test_cart_total_price_max_digits(self):
        cart = Cart.objects.get(id=1)
        max_digits = cart._meta.get_field('cart_total_price').max_digits

        self.assertEquals(max_digits, 10)

    """Проверяем максимальную длину поля cart_total_price после дробной части"""
    def test_cart_total_price_decimal_places(self):
        cart = Cart.objects.get(id=1)
        decimal_places = cart._meta.get_field('cart_total_price').decimal_places

        self.assertEquals(decimal_places, 2)

    """Проверяем что выведет объект cart"""
    def test_object_name_is_cart_id(self):
        cart = Cart.objects.get(id=1)
        expected_object_name = str(cart.id)

        self.assertEquals(expected_object_name, str(cart))


class CartItemModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        number_of_products = 2

        """Создаем 2 продукта"""
        for product in range(number_of_products):
            Product.objects.create(
                name='test %s' % product,
                price=10.00,
                create=datetime.datetime.now(),
                update=datetime.datetime.now()
            )

    def setUp(self):

        """Создаем 2 позиции в корзину"""
        for cart_item in range(1, 3):
            item = CartItem.objects.create(
                product=Product.objects.get(id=cart_item),
                number_of_product=2
            )
            item.save()  # сохраняю, чтобы сумма пересчиталась за позицию
            item.cart_set.all()

    """Проверяем название поля number_of_product"""
    def test_number_of_product_label(self):
        cart_item = CartItem.objects.get(id=1)
        field_label = cart_item._meta.get_field('number_of_product').verbose_name

        self.assertEquals(field_label, 'Количество товара')

    """Проверяем название поля total_item_price"""
    def test_total_item_price_label(self):
        cart_item = CartItem.objects.get(id=1)
        field_label = cart_item._meta.get_field('total_item_price').verbose_name

        self.assertEquals(field_label, 'Общая сумма за товар')

    """Проверяем максимальную длину поля total_item_price до дробной части"""
    def test_total_item_price_max_digits(self):
        cart_item = CartItem.objects.get(id=1)
        max_digits = cart_item._meta.get_field('total_item_price').max_digits

        self.assertEquals(max_digits, 10)

    """Проверяем максимальную длину поля total_item_price после дробной части"""
    def test_total_item_price_decimal_places(self):
        cart_item = CartItem.objects.get(id=1)
        decimal_places = cart_item._meta.get_field('total_item_price').decimal_places

        self.assertEquals(decimal_places, 2)

    """Проверяем, что выведет объект cart_item"""
    def test_object_name_is_cart_id(self):
        cart_item = CartItem.objects.get(id=1)
        expected_object_name = cart_item.product.name

        self.assertEquals(expected_object_name, 'test 0')

    """Проверяем корректно ли работает метод save в классе CartItem"""
    def test_calculate_total_item_price(self):
        cart_item = CartItem.objects.get(id=1)
        total_item_price = cart_item.product.price * cart_item.number_of_product

        self.assertEquals(total_item_price, cart_item.total_item_price)
        self.assertEquals(total_item_price, 20.00)
