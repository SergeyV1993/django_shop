from django.test import TestCase
from django.shortcuts import *


class AccountListViewTest(TestCase):

    def test_view_url_accessible(self):
        resp = self.client.get(reverse('account'))
        self.assertEqual(resp.status_code, 200)


