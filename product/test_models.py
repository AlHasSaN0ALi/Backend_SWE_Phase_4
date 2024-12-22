from django.test import TestCase
from .models import Product, Category

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics", slug="electronics")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Electronics")
        self.assertEqual(self.category.slug, "electronics")

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Clothing", slug="clothing")
        self.product = Product.objects.create(
            category=self.category,
            name="T-shirt",
            slug="t-shirt",
            description="A comfortable cotton t-shirt",
            price=25.00,
        )

    def test_product_fields(self):
        self.assertEqual(self.product.name, "T-shirt")
        self.assertEqual(self.product.description, "A comfortable cotton t-shirt")
        self.assertEqual(float(self.product.price), 25.00)

    def test_category_association(self):
        self.assertEqual(self.product.category.name, "Clothing")
