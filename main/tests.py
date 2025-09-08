from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):

    def setUp(self):
        # Membuat beberapa produk untuk testing
        self.product1 = Product.objects.create(
            name="Sepatu Bola Merah",
            price=500000,
            description="Sepatu bola premium",
            thumbnail="https://example.com/sepatu_merah.jpg",
            category="Sepatu",
            is_featured=True
        )
        self.product2 = Product.objects.create(
            name="Bola Omega",
            price=300000,
            description="Bola resmi liga",
            thumbnail="https://example.com/bola_omega.jpg",
            category="Bola",
            is_featured=False
        )

    def test_main_url_exists(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_uses_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/tidak_ada/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        product = Product.objects.create(
            name="Kaos Tim C",
            price=150000,
            description="Kaos tim favorit",
            thumbnail="https://example.com/kaos_c.jpg",
            category="Kaos",
            is_featured=True
        )
        self.assertTrue(product.is_featured)
        self.assertEqual(product.category, "Kaos")
        self.assertEqual(product.price, 150000)

    def test_default_is_featured_false(self):
        product = Product.objects.create(
            name="Syal D",
            price=50000,
            description="Syal tim",
            thumbnail="https://example.com/syal_d.jpg",
            category="Aksesoris"
        )
        self.assertFalse(product.is_featured)
