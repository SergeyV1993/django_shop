import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from orders.models import *
from django.urls import reverse


class AccountListViewTest(TestCase):

    def setUp(self):
        """Создание тестового пользователя"""
        test_user1 = User.objects.create_user(username='testuser', password='12345')
        test_user1.save()

        """Создание тестового статуса для заказа"""
        Status.objects.create(
            name='New',
            create=datetime.datetime.now(),
            update=datetime.datetime.now()
        )

        """Создание 10 заказов"""
        number_of_orders_copies = 10
        for order in range(number_of_orders_copies):
            Order.objects.create(
                user=test_user1,
                customer_email='test@test.qw',
                customer_name='test',
                customer_phone='1234567',
                total_price='1000',
                create=datetime.datetime.now(),
                update=datetime.datetime.now()
            )

    def test_logged_user(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('account'))

        # Проверка что пользователь залогинился
        self.assertEqual(str(response.context['user']), 'testuser')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'account/account.html')

    def test_count_orders_for_user(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('account'))

        get_user = User.objects.get(username=str(response.context['user']))
        get_orders = Order.objects.filter(user=get_user)

        self.assertEqual(len(get_orders), 10)















