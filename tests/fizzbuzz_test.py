
import unittest
from src.my_package.fizzbuzz import fizzbuzz2

class FizzBuzzTest(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz2(0,"fizz", "buzz", "fizzbuzz"), [])
        self.assertEqual(fizzbuzz2(1,"fizz", "buzz", "fizzbuzz"), ['1'])
        #self.assertEqual(fizzbuzz2(15, "fizz", "buzz", "fizzbuzz"), "fizzbuzz")