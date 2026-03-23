def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        for j in range(i - 1, -2, -1):
            if j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
            else:
                arr[j + 1] = key
                break

    return arr


print(insertionsort(arr=[9, 5, 1, 2, 4]))
