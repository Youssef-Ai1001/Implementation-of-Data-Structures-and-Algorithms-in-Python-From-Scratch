def BinarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if target == arr[mid]:
            return mid

        else:
            if target > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


test_arr = [9, 10, 12, 15, 17, 28]
print(BinarySearch(test_arr, target=88))
print(BinarySearch(test_arr, 15))
