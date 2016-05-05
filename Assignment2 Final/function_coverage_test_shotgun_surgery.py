import fileController
import unittest

class functionCoverageTestShotgunSurgery(unittest.TestCase):

    def setUp(self):
        print("A test case is called.")
        fileController.Controller.do_readFile(self)


    def test_1(self):
        result = '''+------+--------+-----+-------+-------------+--------+
|  ID  | Gender | Age | Sales |     BMI     | Income |
+======+========+=====+=======+=============+========+
| A001 | M      | 22  | 83    | Normal      | 186    |
+------+--------+-----+-------+-------------+--------+
| B002 | F      | 32  | 99    | Normal      | 390    |
+------+--------+-----+-------+-------------+--------+
| C003 | M      | 33  | 90    | Overweight  | 290    |
+------+--------+-----+-------+-------------+--------+
| D004 | F      | 29  | 84    | Overweight  | 188    |
+------+--------+-----+-------+-------------+--------+
| E005 | M      | 49  | 107   | Normal      | 99     |
+------+--------+-----+-------+-------------+--------+
| F006 | F      | 47  | 225   | Overweight  | 360    |
+------+--------+-----+-------+-------------+--------+
| G007 | M      | 51  | 105   | Obesity     | 850    |
+------+--------+-----+-------+-------------+--------+
| H008 | F      | 42  | 180   | Obesity     | 720    |
+------+--------+-----+-------+-------------+--------+
| I009 | M      | 23  | 278   | Underweight | 350    |
+------+--------+-----+-------+-------------+--------+
| J010 | F      | 55  | 379   | Underweight | 299    |
+------+--------+-----+-------+-------------+--------+'''
        self.assertEqual(result, fileController.Controller.do_display(self))



    def tearDown(self):
        print("This test case is done!")

if __name__ == '__main__':
    unittest.main(exit = False)