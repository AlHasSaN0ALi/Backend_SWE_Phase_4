from django.test import TestCase
from product.models import Product, Category

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category", slug="test-category")
        self.product = Product.objects.create(
            category=self.category,
            name="Test Product",
            slug="test-product",
            description="Test Description",
            price=99.99,
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.category.name, "Test Category")
        self.assertEqual(float(self.product.price), 99.99)


    def test_unique_slug(self):
        with self.assertRaises(Exception):
            Product.objects.create(
                category=self.category,
                name="Duplicate Product",
                slug="test-product",
                description="Another Description",
                price=50.00,
            )

    def test_price_boundary(self):
        with self.assertRaises(Exception):
            Product.objects.create(
                category=self.category,
                name="Invalid Price Product",
                slug="invalid-price-product",
                description="Negative Price",
                price=-10.00,
            )


    def test_category_relationship(self):
        self.assertEqual(self.product.category.name, "Test Category")
        self.assertIn(self.product, self.category.products.all())
