# Tets for equality and inequality with strings
name = 'matias'
print('Is name == "matias"?')
print(name == 'matias')

print('\nIs name != "matias"?')
print(name != 'matias')

#Test using the lower() method

name = 'Ame'
print('\nIs name "Ame"?')
print(name == 'ame')
print('\nIs name "ame"?')
print(name.lower() == 'ame')

# Numerical tests involving equality and inequality, greater than and less than,
# greater or equal to, less or equal to.

number_1 = 7
number_2 = 3

print('\nIs number_1 == number_2?')
print(number_1 == number_2)

print('\nIs number_1 == 7?')
print(number_1 == 7)
    
print('\n Is number_1 > number_2?')
print(number_1 > number_2)

print('\n Is number_2 < number_1')
print(number_2 < number_1)

print('\n Is number_1 >= 7?')
print(number_1 >= 7)

print('\n Is number2 <= 4?')
print(number_2 >= 4)

# Tests using the 'and' keyword and the 'or' keyword

print('\n If number_1 > 6 and number_2 < 8 then number_1 is equal to 7')
print(number_1 > 6 and number_1 < 8)

print('\n If number_2 % 2 == 0 or number_2 % 4 == 0 Then number_2 is an even number')
print(number_2 % 2 == 0 or number_2 % 4 == 0)

#Test Whether an itmen is in a list

list = [number_1, number_2]

if 7 in list:
    print('\nOne of your favourite numbers is in this list')
else:
    print("\n:'/")

#Test Whether an item is not in a list

if 'Mate' is not list:
    print('\nThis is not a favourite drinks list')



