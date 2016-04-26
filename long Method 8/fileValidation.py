import re

__author__ = 'Rui Zheng'


class Validation(object):
    def __init__(self, theFile=None, length=None):
        from readFile import LocalData
        self.theFile = LocalData.local_data
        self.length = int(len(self.theFile))

    def fileValidation(self):
        Validation.id_validate(self)
        Validation.gender_validate(self)
        Validation.age_validate(self)
        Validation.sales_validate(self)
        Validation.bmi_validate(self)
        Validation.income_validate(self)
        return self.theFile

    def id_validate (self):
        for element in range(0, self.length):
            if re.match(r'[A-Z][0-9]{3}', self.theFile[element][0]):
                print(str(self.theFile[element][0]) + '----> ID Checked')
            else:
                newID = input(self.theFile[element][0] + " " +
                              'is incorrect ID, Please enter the Correct '
                              'ID which content, '
                              'a capital letter fellow by 3 digits  --->')
                self.theFile[element][0] = newI

    def gender_validate(self):
        for element in range(0, self.length):
            if self.theFile[element][1] == "F" or \
                            self.theFile[element][1] == "M":
                print(str(self.theFile[element][1]) + '----> Gender Checked')
            else:
                newGender = input(self.theFile[element][1] +
                                  " " + 'is incorrect Gender, Please enter '
                                        'the Correct Gender,'
                                        'M for Male and F for Female --->')
                self.theFile[element][1] = newGender

    def age_validate(self):
        for element in range(0, self.length):
            if re.match(r'[0-9]{2}', self.theFile[element][2]):
                print(str(self.theFile[element][2]) + '----> Age Checked')
            else:
                newAge = input(self.theFile[element][2] + " " +
                               ' is incorrect Age, Please enter the '
                               'Correct Age, 00 - 99 --->')
                self.theFile[element][2] = newAge

    def sales_validate(self):
        for element in range(0, self.length):
            if re.match(r'[0-9]{3}', self.theFile[element][3]):
                print(str(self.theFile[element][3]) + '----> Sales Checked')
            else:
                newSales = input(self.theFile[element][3] +
                                 " " + "is incorrect Sales, please Enter "
                                       "a correct number"
                                       " between 000 - 999 --->")
                self.theFile[element][3] = newSales

    def bmi_validate(self):
        for element in range(0, self.length):
            if self.theFile[element][4] == "Normal" or \
                            self.theFile[element][4] == "Overweight" or \
                            self.theFile[element][4] == "Obesity" or \
                            self.theFile[element][4] == "Underweight":
                print(str(self.theFile[element][4]) + '----> BMI Checked')
            else:
                newBMI = input(self.theFile[element][4] +
                               " " + 'is incorrect BMI, Please enter '
                                     'the Correct BMI,'
                                     'Normal, Overweight, Obesity or '
                                     'Underweight --->')
                self.theFile[element][4] = newBMI

    def income_validate(self):
        for element in range(0, self.length):
            if re.match(r'[0-9]{2,3}[\n]', self.theFile[element][5]):
                print(str(self.theFile[element][5]) + "----> Income "
                                                      "Checked")
            else:
                newIncome = input(self.theFile[element][5] +
                                  " " + "is incorrect Income, "
                                        "Please enter the correct "
                                        "Income between 00 - 999 ---> ")
                self.theFile[element][5] = newIncome + '\n'

