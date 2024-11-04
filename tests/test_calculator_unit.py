import unittest
from calculator import Calculator

class TestCalculatorUnit(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(1, 2), 3)

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(5, 3), 2)

if __name__ == '__main__':
    unittest.main()