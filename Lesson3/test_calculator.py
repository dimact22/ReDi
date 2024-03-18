import unittest
from calculate import sum_two_variables

class Testcalculator(unittest.TestCase):

    def test_sum_two_variables_result_11(self):
        sum = sum_two_variables(5,6)
        self.assertEqual(sum,11)

if __name__ == "__main__":
    unittest.main()