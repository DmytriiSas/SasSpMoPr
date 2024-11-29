import unittest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        """Ініціалізація об'єкта калькулятора для кожного тесту."""
        self.calc = Calculator()

    # Завдання 1: Тестування додавання
    def test_addition(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-3, 5), 2)
        self.assertEqual(self.calc.add(-3, -5), -8)
    
    # Завдання 2: Тестування віднімання
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-3, 5), -8)
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    # Завдання 3: Тестування множення
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-3, 5), -15)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-3, -5), 15)

    # Завдання 4: Тестування ділення
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333, places=4)

    # Завдання 5: Тестування обробки помилок
    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()
