numbers = [x for x in range(5)]
print(numbers)
#output: [0, 1, 2, 3, 4]
squares = [x ** 2 for x in range(5)]
print(squares)
#output:[0, 1, 4, 9, 16]
double_even = [x*2 for x in numbers if x%2==0]
print(double_even)
#output:[0, 4, 8]
matrix = [numbers for x in range(3)]
print(matrix)
#output: [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
# bohrium.com/sciencepedia
matrix2 = [[x for x in range(5)]for y in range(3)]
print(matrix2)
#output:[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]