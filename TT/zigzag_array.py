def zigzag(arr):
    for i in range(len(arr) - 1):
        if (i % 2 == 0 and arr[i] > arr[i + 1]) or (i % 2 == 1 and arr[i] < arr[i + 1]):
            arr[i], arr[i + 1] = arr[i + 1], arr[i] 
    return arr

arr = [4, 3, 7, 8, 6, 2, 1]
print(zigzag(arr))  
