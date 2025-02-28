import numpy as np
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print('Our array is:')
print(a)
print("The items in the second column are:")
print(a[:,1])
print("After slicing")
print(a[::2])