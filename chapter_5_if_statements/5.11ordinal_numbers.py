numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

ordinal_number = []

for number in numbers:
    if number == '1':
        number = number + 'st' + ' '
        ordinal_number.append(number)
        print(number)
    elif number == '2':
        number = number + 'nd' + ' '
        ordinal_number.append(number)
        print(number)
    elif number == '3':
        number = number + 'rd' + ' '
        ordinal_number.append(number)
        print(number)
    else:
        number = number + 'th' + ' '
        ordinal_number.append(number)
        print(number)


