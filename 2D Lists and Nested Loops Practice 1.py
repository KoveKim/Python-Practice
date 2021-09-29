# 2D lists and nested loops

# Here is a list made of lists to make a grid. 4 rows, 3 columns
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#print(number_grid[2][1])  # Row by columns. Remember that index starts at 0

for row in number_grid:
    for col in row:
        print(col)
