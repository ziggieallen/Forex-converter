from unittest import TestCase
from app import app
from functions import currencies, check_if_valid_currency_code, calculate_conversion_and_check_amount 
from forex_python.converter import CurrencyRates
from decimal import Decimal

class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True 
    
    def test_html_appearance(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
        
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Forex Converter</h1>', html)  
            self.assertIn('<label>Converting from</label>', html)  
    
    def test_USD_to_USD(self):
        """Checks whether USD to USD is $1.00"""

        c = CurrencyRates()
        self.assertEqual(round(c.convert('USD', 'USD', Decimal(1)), 2), 1.00)

    def test_flash_message(self):
        """Checks whether success flash message appears when data passed through the form"""
        
        with app.test_client() as client:
            res = client.post('/', data={'currency_from': 'USD', 'currency_to': 'USD', 'amount': '1'}, follow_redirects=True)
            html = res.get_data(as_text=True) 

            self.assertEqual(res.status_code, 200) 
            self.assertIn('The result is $1.00', html)

    def test_flash_message(self):
        """Checks whether error flash message appears when data passed through the form"""

        with app.test_client() as client:
            res = client.post('/', data={'currency_from': 'YYY', 'currency_to': 'USD', 'amount': '1'}, follow_redirects=True)
            html = res.get_data(as_text=True) 

            self.assertEqual(res.status_code, 200) 
            self.assertIn('Not valid code: YYY.', html)