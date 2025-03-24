from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuItemTest(TestCase):
     def test_get_item(self):
        item = Menu.objects.create(id=79,title="IceCream", price="3.20", inventory=100)
        self.assertEqual(str(item), "IceCream : 3.20")