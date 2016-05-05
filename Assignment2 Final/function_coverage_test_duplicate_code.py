import display2DModue
import unittest


class FunctionCoverageTestDuplicationCode(unittest.TestCase):
    def setUp(self):
        print("A test case is called.")
        self.list_size = 10
        self.data_list = [['A001', 'M', '22', '083', 'Normal', '186\n'],
                          ['B002', 'F', '32', '099', 'Normal', '390\n'],
                          ['C003', 'M', '33', '090', 'Overweight', '290\n'],
                          ['D004', 'F', '29', '084', 'Overweight', '188\n'],
                          ['E005', 'M', '49', '107', 'Normal', '099\n'],
                          ['F006', 'F', '47', '225', 'Overweight', '360\n'],
                          ['G007', 'M', '51', '105', 'Obesity', '850\n'],
                          ['H008', 'F', '42', '180', 'Obesity', '720\n'],
                          ['I009', 'M', '23', '278', 'Underweight', '350\n'],
                          ['J010', 'F', '55', '379', 'Underweight', '299\n']]

    def test_1(self):
        self.assertEqual([724, 1859, 1149],
                         display2DModue.DisPlay2D.displayAgeGroupIncome)

    def test_2(self):
        self.assertEqual([1957, 1775],
                         display2DModue.DisPlay2D.displayIncomeByGender(self))

    def test_3(self):
        self.assertEqual([675, 838, 1570, 649],
                         display2DModue.DisPlay2D.displayBMIIncome)

    def tearDown(self):
        print("This test case is done!")


if __name__ == '__main__':
    unittest.main(exit=False)
