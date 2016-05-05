def countGender(gender):
    """
    >>> countGender('Female')
    5
    >>> countGender('Male')
    5
    """
    from readFile import LocalData
    the_data = LocalData.local_data
    male_count = 0
    female_count = 0
    length = len(the_data)

    for element in range(0, length):
        if the_data[element][1] == "F":
            female_count += 1
        elif the_data[element][1] == "M":
            male_count += 1
    if (gender == 'Female'):
        print(female_count)
    elif (gender == 'Male'):
        print(male_count)


def totalIncome(gender):
    """
    >>> totalIncome('Female')
    1957
    >>> totalIncome('Male')
    1775
    """
    from readFile import LocalData
    the_data = LocalData.local_data
    male_income = 0
    female_income = 0
    length = len(the_data)

    for element in range(0, length):
        if the_data[element][1] == "F":
            female_income += int(the_data[element][5])
        elif the_data[element][1] == "M":
            male_income += int(the_data[element][5])

    if (gender == 'Female'):
        print(female_income)
    elif (gender == 'Male'):
        print(male_income)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
