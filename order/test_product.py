from django.test import TestCase
from product.models import Product, Category

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Winter", slug="winter")
        self.product = Product.objects.create(
            category=self.category,
            name="Warm Jacket",
            slug="warm-jacket",
            description="",
            price=500.00,
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Warm Jacket")
        self.assertEqual(self.product.category.name, "Winter")
        self.assertEqual(float(self.product.price), 500.00)


    def test_category_relationship(self):
        self.assertEqual(self.product.category.name, "Winter")
        self.assertIn(self.product, self.category.products.all())
