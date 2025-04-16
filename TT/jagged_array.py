
jagged_array = [
    [1, 2, 3],          # Row 1 with 3 elements
    [4, 5],             # Row 2 with 2 ele
    [6, 7, 8, 9],       # Row 3 with 4 eleme
    [10]              
]

for row in jagged_array:
    for element in row:
        print(element, end=" ")
    print()