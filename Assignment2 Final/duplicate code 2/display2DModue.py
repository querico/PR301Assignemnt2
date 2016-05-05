import matplotlib.pyplot as plt
from fileValidation import Validation


class DisPlay2D(object):
    def __init__(self):
        data_list = Validation().fileValidation()
        list_size = len(self.data_list)
        incomes = []

    @staticmethod
    def displayIncomeByGender():
        female_income = 0
        male_income = 0

        for element in range(0, self.list_size):
            if self.data_list[element][1] == "F":
                female_income += int(self.data_list[element][5])
            elif self.data_list[element][1] == "M":
                male_income += int(self.data_list[element][5])

        self.incomes.append(female_income)
        self.incomes.append(male_income)

        plt.title("Male and Female Income Ratio")
        labels = 'Female Income', 'Male Income'
        sizes = self.incomes
        colors = ['pink', 'blue']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.show()

    @staticmethod
    def displayAgeGroupIncome():
        data_list = Validation().fileValidation()
        list_size = len(data_list)
        incomes = []
        under_30_income = 0
        between30_50_income = 0
        above50_income = 0

        for element in range(0, list_size):
            if int(data_list[element][2]) > 0 \
                    and int(data_list[element][2]) <= 30:
                under_30_income += int(data_list[element][5])
            elif int(data_list[element][2]) > 30 \
                    and int(data_list[element][2]) <= 50:
                between30_50_income += int(data_list[element][5])
            elif int(data_list[element][2]) > 50:
                above50_income += int(data_list[element][5])

        incomes.append(under_30_income)
        incomes.append(between30_50_income)
        incomes.append(above50_income)

        plt.title("Age Group and Income Ratio")
        labels = 'Age under 30', 'Age between 31-50', 'Age above 50'
        sizes = incomes
        colors = ['Blue', 'Green', 'Orange']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.show()

    @staticmethod
    def displayBMIIncome():
        data_list = Validation().fileValidation()
        list_size = len(data_list)
        incomes = []
        count = []
        normal_income = 0
        overweight_income = 0
        obesity_income = 0
        underweight_income = 0

        n_groups = 4

        for element in range(0, list_size):
            if data_list[element][4] == 'Normal':
                normal_income += int(data_list[element][5])
            elif data_list[element][4] == 'Overweight':
                overweight_income += int(data_list[element][5])
            elif data_list[element][4] == 'Obesity':
                obesity_income += int(data_list[element][5])
            elif data_list[element][4] == 'Underweight':
                underweight_income += int(data_list[element][5])

        incomes.append(normal_income)
        incomes.append(overweight_income)
        incomes.append(obesity_income)
        incomes.append(underweight_income)
        plt.title("BMI Group and Income Ratio")
        fig, ax = plt.subplots()
        bar_width = 0.35
        opacity = 0.4
        error_config = {'ecolor': '0.3'}

        rects = plt.bar([index + bar_width for index in range(n_groups)],
                        incomes, bar_width,
                        alpha=opacity,
                        color='r',
                        yerr=incomes,
                        error_kw=error_config,
                        label='Income')

        plt.xlabel('BMI')
        plt.ylabel('Income')
        plt.xticks([index + bar_width for index in range(n_groups)],
                   ('Normal', 'Overweight', 'Obesity', 'Underweight'))
        plt.show()
