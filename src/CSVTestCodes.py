from pprint import pprint
import unittest
from CsvReader import CsvReader
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:

test_data_add = CsvReader('src/Test/Addition.csv').data
pprint(test_data_add)

for row in test_data_add:
    self.assertEqual(self.calculator.add(row['Value 2'], row['Value 1']), int(row['Result']))
    self.assertEqual(self.calculator.result, int(row['Result']))

test_data_subtract = CsvReader('src/Test/Subtraction.csv').data
pprint(test_data_subtract)

for row in test_data_subtract:
    self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), int(row['Result']))
    self.assertEqual(self.calculator.result, int(row['Result']))

test_data_multiply = CsvReader('src/Test/Multiplication.csv').data
pprint(test_data_multiply)

for row in test_data_multiply:
    self.assertEqual(self.calculator.multiply(row['Value 2'], row['Value 1']), int(row['Result']))
    self.assertEqual(self.calculator.result, int(row['Result']))

test_data_divide = CsvReader('src/Test/Division.csv').data
pprint(test_data_divide)

for row in test_data_divide:
    self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), round(float(row['Result']))
    self.assertEqual(self.calculator.result, float(row['Result']))

test_data_square = CsvReader('src/Test/Square.csv').data
pprint(test_data_square)

for row in test_data_square:
    self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
    self.assertEqual(self.calculator.result, int(row['Result']))

test_data_squareroot = CsvReader('src/Test/Square Root.csv').data
pprint(test_data_square)

for row in test_data_square:
    self.assertEqual(self.calculator.squareroot(row['Value 1']), int(row['Result']))
    self.assertEqual(self.calculator.result, int(row['Result']))