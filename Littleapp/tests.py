from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuTest(TestCase):
    def test_book(self):
        item = Menu.objects.create(title='Bright', price=88, inventory=13)
        
        
        self.assertEqual(item, "Bright : 88")
