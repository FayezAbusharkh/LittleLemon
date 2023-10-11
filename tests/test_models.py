from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        # Create some test Menu instances.
        self.menu1 = Menu.objects.create(title="Pizza", price=100.50, inventory=50)
        self.menu2 = Menu.objects.create(title="Burger", price=50.00, inventory=30)

    def test_getall(self):
        # Get all Menu objects.
        menus = Menu.objects.all()
        
        # Serialize the data
        serialized_data = MenuSerializer(menus, many=True).data

        # List of expected serialized data
        expected_data = [
            {'id': self.menu1.id, 'title': 'Pizza', 'price': '100.50', 'inventory': 50},
            {'id': self.menu2.id, 'title': 'Burger', 'price': '50.00', 'inventory': 30}
        ]
        
        # Check if the serialized data matches the expected data.
        self.assertEqual(serialized_data, expected_data)
