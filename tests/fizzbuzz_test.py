import unittest
from src.my_package.fizzbuzz import fizzbuzz2


class FizzBuzzTest(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz2(0, "fizz", "buzz", "fizzbuzz"), [])
        self.assertEqual(fizzbuzz2(1, "fizz", "buzz", "fizzbuzz"), ["1"])
        ###asserListEqual spesify more the diffrence between the expected input  and the input
        self.assertListEqual([1,2, 3,4], [1, 2,3, "4"])
        # self.assertEqual(fizzbuzz2(15, "fizz", "buzz", "fizzbuzz"), "fizzbuzz")

if __name__ == "__main__":
    unittest.main()
