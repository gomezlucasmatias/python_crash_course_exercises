multiples_of_three = [value * 3 for value in range(1, 11)]
print(multiples_of_three)

the_other_list = []

for value in range(1, 11):
    value = value * 3
    the_other_list.append(value)

print(the_other_list)
