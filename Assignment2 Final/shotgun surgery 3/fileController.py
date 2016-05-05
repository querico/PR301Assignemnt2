import cmd
import pickle
import os
from texttable import Texttable
from display2DModue import DisPlay2D
from fileValidation import Validation

__author__ = 'Rui Zheng'


# -------------------------------------------------------------------------------
# Name:        Assignment 1 data import and analysis
# Purpose:     PR301 - Assignment 1
# Author:      Rui Zheng
# Created:     10/03/2016
# -------------------------------------------------------------------------------

# this is the Controller Class

class Controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "Please Enter Your Command"

    print("Welcome to the data collecting app \n"
          "Need Help please >>>help<<< command \n"
          "it will bring you useful information ")

    def do_help(self, command):
        print(
            '============================================================='
            '==================\n'
            "+--->'help' command: shows all command for this app          "
            "                 +\n"
            "+     Help user to recognize all the different commands      "
            "                 +\n"
            '============================================================='
            '==================\n'
            "+--->'readFile' command: for user to select a file and store "
            "in memory        +\n"
            "+     Simply  type in command 'readFile' and select the file "
            "                 +\n"
            '=============================================================='
            '=================\n'
            "+--->'display' command: for user to display the row data      "
            "                +\n"
            "+     Simply  enter the 'display' command in the dialog box   "
            "                +\n"
            '=============================================================='
            '=================\n'
            "+--->'validate' command: for user to validate the inputted "
            "data               +\n"
            "+     Simply  enter the 'validate' command in the dialog box  "
            "                +\n"
            '==============================================================='
            '================\n'
            "+--->'chart' command: for user to display the 2D chart         "
            "               +\n"
            "+     enter 'chart' fellow by 'Age' will sort income by Age    "
            "               +\n"
            "+     enter 'chart' fellow by 'Gender' will sort income by "
            "Gender             +\n"
            "+     enter 'chart' fellow by 'BMI' will sort income by BMI     "
            "              +\n"
            '================================================================'
            '===============\n'
            "+--->'saveObject' Command: is used for save a pickle file       "
            "              +\n"
            "+     Enter 'saveObject' fellow by file name example:'saveObject"
            " new'         +\n"
            '================================================================='
            '==============\n'
            "+--->'loadObject' Command: is used for load a pickle file       "
            "              +\n"
            "+     Enter 'loadObject' fellow by file name example:'loadObject"
            " new'         +\n"
            '================================================================='
            '==============\n'
            "+--->'quit' Command: is used to quit the program                 "
            "             +\n"
            "+     Simply   enter the 'quit' command in the dialog box        "
            "             +\n"
            '================================================================='
            '==============\n'
        )
    @staticmethod
    def readFileFromInport(self):
        from readFile import LocalData
        file = LocalData.local_data
        return(file)

    @staticmethod
    def do_readFile(self):
        Controller.readFileFromInport(self)

    @staticmethod
    def do_display(self):
        record = Controller.readFileFromInport(self)
        recode_size = len(record)
        t = Texttable()

        for element in range(0, recode_size):
            t.add_row(record[element])
            t.header(['ID', 'Gender', 'Age', 'Sales', 'BMI', 'Income'])
        print(t.draw())

    @staticmethod
    def do_validate(self):
        a = Validation()
        a.fileValidation()
        print('Done')

    def do_saveObject(self, file_name):
        try:
            if file_name == "":
                raise InvalidActionError(
                    "Please Enter a File Name"
                )
            else:
                file_data = Validation().fileValidation()
                with open(file_name + ".pickle", 'wb')as save_file:
                    pickle.dump(file_data, save_file)
                print(
                    "Verified file saved as " + file_name + ".pickle"
                )
        except InvalidActionError as err:
            print(err)

    def do_chart(self, command):
        try:
            if command != "Age" and command != "Gender" and command != "BMI":
                raise InvalidActionError(
                    "please Enter a valid command which Age, Gender or BMI"
                )
            elif command == "Age":
                module2D = DisPlay2D().displayAgeGroupIncome
                print("the Pie Chart has been displayed ")
            elif command == "Gender":
                module2D = DisPlay2D().displayIncomeByGender()
                print("the Pie Chart has been displayed ")
            elif command == "BMI":
                module2D = DisPlay2D().displayBMIIncome
                print("the bar Chart has been displayed ")

        except InvalidActionError as err:
            print(err)

    def do_loadObject(self, command):
        try:
            if command == "":
                raise InvalidActionError(
                    "file name can not be empty"
                )
            if not os.path.exists(command + ".pickle"):
                raise InvalidActionError(
                    "file " + command + " does not exist )"
                )
            with open(command + ".pickle", "rb") as load_data:
                data = pickle.load(load_data)

            Validation.theFile = data[0]
            print(
                "(File loaded from " + command + ".pickle"
            )
        except InvalidActionError as err:
            print(err)

    @staticmethod
    def do_quit(self):

        print("Quitting ......")
        return True

    def do_saveRecord(self, file_name):
        try:
            if file_name == "":
                raise InvalidActionError(
                    "Please Enter a File Name"
                )
            else:
                file_data = Validation.theFile
                with open(file_name + ".pickle", 'wb')as save_file:
                    pickle.dump(file_data, save_file)
                print(
                    "Verified file saved as " + file_name + ".pickle"
                )
        except InvalidActionError as err:
            print(err)




class InvalidActionError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr("Invalid Action: " + self.value)



if __name__ == '__main__':
    quitter = Controller()
    quitter.cmdloop()


