import matplotlib.pyplot as plt

class DisPlay2D(object):
    def __init__(self, data_list=None, list_size=None):
        from fileValidation import Validation
        self.data_list = Validation().fileValidation()
        self.list_size = len(self.data_list)
        print (self.data_list)


    def displayIncomeByGender(self):
        female_income = 0
        male_income = 0
        incomes = []

        for element in range(0, self.list_size):
            if self.data_list[element][1] == "F":
                female_income += int(self.data_list[element][5])
            elif self.data_list[element][1] == "M":
                male_income += int(self.data_list[element][5])

        incomes.append(female_income)
        incomes.append(male_income)

        plt.title("Male and Female Income Ratio")
        labels = 'Female Income', 'Male Income'
        sizes = incomes
        colors = ['pink', 'blue']
        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.show()


    def displayAgeGroupIncome(self):
        incomes = []
        under_30_income = 0
        between30_50_income = 0
        above50_income = 0

        for element in range(0, self.list_size):
            if int(self.data_list[element][2]) > 0 \
                    and int(self.data_list[element][2]) <= 30:
                under_30_income += int(self.data_list[element][5])
            elif int(self.data_list[element][2]) > 30 \
                    and int(self.data_list[element][2]) <= 50:
                between30_50_income += int(self.data_list[element][5])
            elif int(self.data_list[element][2]) > 50:
                above50_income += int(self.data_list[element][5])

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


    def displayBMIIncome(self):
        incomes = []
        count = []
        normal_income = 0
        overweight_income = 0
        obesity_income = 0
        underweight_income = 0

        n_groups = 4

        for element in range(0, self.list_size):
            if self.data_list[element][4] == 'Normal':
                normal_income += int(self.data_list[element][5])
            elif self.data_list[element][4] == 'Overweight':
                overweight_income += int(self.data_list[element][5])
            elif self.data_list[element][4] == 'Obesity':
                obesity_income += int(self.data_list[element][5])
            elif self.data_list[element][4] == 'Underweight':
                underweight_income += int(self.data_list[element][5])

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
