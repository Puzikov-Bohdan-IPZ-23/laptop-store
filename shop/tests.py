from django.test import TestCase
from .models import Laptop

class LaptopModelTest(TestCase):
    def setUp(self):
        Laptop.objects.create(
            brand="Lenovo",
            model="ThinkPad X1",
            processor="Intel Core i7",
            ram_gb=16,
            storage_gb=512,
            price=45999.00,
            stock=5
        )

    def test_laptop_str(self):
        laptop = Laptop.objects.get(model="ThinkPad X1")
        expected_str = f"{laptop.brand} {laptop.model}"
        self.assertEqual(str(laptop), expected_str)

    def test_laptop_price(self):
        laptop = Laptop.objects.get(model="ThinkPad X1")
        self.assertEqual(laptop.price, 45999.00)
