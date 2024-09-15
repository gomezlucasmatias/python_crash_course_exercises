cube = []
for number in range(1,11):
	number = number ** 3
	cube.append(number)
print(cube)

squares = []
for square in range(1, 11):
	squares.append(square ** 2)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

squares = [value ** 2 for value in range(1, 11)]
print(squares)
