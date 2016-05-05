import fileValidation
import unittest

class functionCoverageTestLongMethod(unittest.TestCase):

    def setUp(self):
        print("A test case is called.")

        self.theFile = [['A001', 'M', '22', '083', 'Normal', '186\n']]
        self.length = 1


    def test_1(self):
        self.assertEqual([['A001', 'M', '22', '083', 'Normal', '186\n']],
                         fileValidation.Validation.fileValidation(self))

    def tearDown(self):
        print("This test case is done!")

if __name__ == '__main__':
    unittest.main(exit = False)