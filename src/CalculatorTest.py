import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_addition(self):
        self.assertEqual(self.calculator.add(1, 1), 2)
        self.assertEqual(self.calculator.result, 2)

        test_data = CsvReader("src/Test/Addition.cs9v").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(1, 1), 0)
        self.assertEqual(self.calculator.result, 0)

        test_data = CsvReader("src/Test/Subtraction.csv").data
        for row in test_data:
            pprint(row)
            result = int(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.result, 6)

        test_data = CsvReader("src/Test/Multiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_division(self):
        self.assertEqual(self.calculator.divide(6, 2), 3)
        self.assertEqual(self.calculator.result, 3)

        test_data = CsvReader("src/Test/Division.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square(self):
        self.assertEqual(self.calculator.square(3))
        self.assertEqual(self.calculator.result, 9)

        test_data = CsvReader("src/Test/Square.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(9), 3)
        self.assertEqual(self.calculator.result, 3)

        test_data = CsvReader("src/Test/Square Root.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.sqrt(row['Value 1'] ** 0.5), result)
            self.assertEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
