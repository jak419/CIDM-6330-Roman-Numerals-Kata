import unittest
# First define the test to test for converting numbers to roman numerals

'''
class RomanNumeralsTest(unittest.TestCase):
    def test_convert_1_to_roman(self):
        self.assertEqual(convert_to_roman(1), "I")


if __name__ == '__main__':
    unittest.main()'''

# function convert_to_roman is not defined so test will fail
# define function convert_to_roman

'''
def convert_to_roman(number):
    return "I"
'''

# Running the test again should pass the test
# Next step is to add more tests

'''
class RomanNumeralsTest(unittest.TestCase):
    def test_convert_1_to_roman(self):
        self.assertEqual(convert_to_roman(1), "I")

    def test_convert_2_to_roman(self):
        self.assertEqual(convert_to_roman(2), "II")

    def test_convert_3_to_roman(self):
        self.assertEqual(convert_to_roman(3), "III")

    def test_convert_4_to_roman(self):
        self.assertEqual(convert_to_roman(4), "IV")


if __name__ == '__main__':
    unittest.main()
'''

# after running the tests again, the tests for converting 2, 3, and 4 to Roman numerals have failed.
# this is because the function 'convert_to_roman' only returns I regardless of the input.
# We can modify the function 'convert_to_roman' to add the new cases of 2, 3, and 4
# However, the final goal of the 'convert_to_roman' function should be able to handle the complexities and full range of the roman numerals
# I =1, V =5, X =10, L =50, C=100, D=500, M=1000


def convert_to_roman(num):
    # To check if the input 'num' is a positive integer
    if not isinstance(num, int) or num <= 0:
        raise ValueError("Input must be a positive integer")

    # Listing the Roman numerals signs and thier corresponding numeric value
    roman_numerals = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
    ]

    roman_numeral = ""
    for numeral, value in roman_numerals:
        # Append the numeral while reducing the number
        while num >= value:
            roman_numeral += numeral
            num -= value

    return roman_numeral


# Examples
try:
    print(convert_to_roman(2022))  # Should print "MMXXII"
    print(convert_to_roman(1))     # Should print "I"
    print(convert_to_roman(10))    # Should print "X"
    print(convert_to_roman(-1))    # Should raise an error
except ValueError as e:
    print(e)
