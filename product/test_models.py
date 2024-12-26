from django.test import TestCase
from .models import Product, Category

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Summer", slug="summer")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Summer")
        self.assertEqual(self.category.slug, "summer")

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Summer", slug="summer")
        self.product = Product.objects.create(
            category=self.category,
            name="t-shirt",
            slug="tshirt",
            description="",
            price=300.00,
        )

    def test_product_fields(self):
        self.assertEqual(self.product.name, "t-shirt")
        self.assertEqual(self.product.description, "")
        self.assertEqual(float(self.product.price), 300.00)

    def test_category_association(self):
        self.assertEqual(self.product.category.name, "Summer")
