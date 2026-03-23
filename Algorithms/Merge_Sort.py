# mergesort
# inputs arr, start, end
def MergeSort(arr, start, end):
    # Base case: if there is only one element or less in the array, return it
    if end <= start:
        return None

    # Divide the array into two halves
    midpoint = (end + start) // 2
    MergeSort(arr, start, midpoint)
    MergeSort(arr, midpoint + 1, end)

    # Merge the two sorted halves
    Merge(arr, start, midpoint, end)


def Merge(arr, start, midpoint, end):
    left_len = (midpoint - start) + 1
    right_len = end - midpoint

    # Create new arrays to hold the left and right halves of the original array
    left_arr = [0] * left_len
    right_arr = [0] * right_len

    # Copy the left half of the original array into the left_array
    for i in range(left_len):
        left_arr[i] = arr[start + i]

    # Copy the right half of the original array into the right_array
    for j in range(right_len):
        right_arr[j] = arr[midpoint + 1 + j]

    # Merge the left and right halves into the original array
    i = j = 0
    k = start
    while i < left_len and j < right_len:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # Copy any remaining elements from the left or right halves into the original array
    while i < left_len:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < right_len:
        arr[k] = right_arr[j]
        j += 1
        k += 1


# Main function
if __name__ == "__main__":
    array = [8, 65, 9, 7, 3, 5, 54]

    print(array)
    MergeSort(array, 0, len(array) - 1)
    print(array)
