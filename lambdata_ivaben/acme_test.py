
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        
        prod = Product('Test Product_1')
        self.assertEqual(prod.weight, 20)

    def test_explode_method(self):
       
        prod = Product('Test Product Bomb')
        self.assertIsNotNone(prod.explode)

    def test_stealability_method(self):
       
        prod = Product('Test Product Stolen')
        self.assertIsNotNone(prod.stealability)

class AcmeReportTest(unittest.TestCase):
   
    def test_default_num_products(self):
        
        products = generate_products()
        self.assertEqual(len(products), 30)


    def test_legal_names(self):
        
        products = generate_products()
        for _ in products:
            self.assertIn(_.name.split()[0], ADJECTIVES)
            self.assertIn(_.name.split()[1], NOUNS)


if __name__ == '__main__':
    unittest.main()


