import unittest

# Correct implementation of calculate_power
def calculate_power(base, exponent):
    result = base ^ exponent
    return result

# Unit Test class for the calculate_power function
class TestCalculatePower(unittest.TestCase):

    def test_positive_numbers(self):
        # Test 3^2 which should return 9
        self.assertEqual(calculate_power(3, 2), 9)

if __name__ == '__main__':
    unittest.main()