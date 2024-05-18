"""
Samle Tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)
    
    def test_subtract_numbers(self):
        """Test subtracting numbers together"""
        res = calc.subtract(29, 23)

        self.assertEqual(res, 6)