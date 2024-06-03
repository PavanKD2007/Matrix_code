#Matrix Addition
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(len(X)):
    for col in range(len(X[0])):
        result[row][col] = X[row][col] + Y[row][col]
print(result)

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#subtraction

for row in range(len(X)):
    for col in range(len(X[0])):
        result[row][col] = X[row][col] - Y[row][col]
print(result)

#multiplication

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
 
for row in range(len(X)):
    for col in range(len(X[0])):
        result[row][col] = X[row][col] * Y[row][col]
print(result)

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#division

for row in range(len(X)):
    for col in range(len(X[0])):
        result[row][col] = X[row][col] / Y[row][col]
print(result)
