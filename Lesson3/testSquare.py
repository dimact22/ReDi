import unittest
from ClassSquare import Square

class Testcalculator(unittest.TestCase):

    def test_square_area_result_25(self):
        a = Square(5)
        area = a.get_area()
        self.assertEqual(area,25)

    def test_sum_all_the_sides_result_20(self):
        a = Square(5)
        area = a.get_sum_all_the_sides()
        self.assertEqual(area,20)

if __name__ == "__main__":
    unittest.main()