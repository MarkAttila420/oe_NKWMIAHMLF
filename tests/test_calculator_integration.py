import unittest
from calculator import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def test_add_and_subtract(self):
        calc = Calculator()
        result = calc.add(10, 5)
        result = calc.subtract(result, 3)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()