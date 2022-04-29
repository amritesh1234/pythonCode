def left_rotate(arr):
    if not arr:
        return arr

    left_most_element = arr[0]
    length = len(arr)

    for i in range(length - 1):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # arr[length - 1] = left_most_element
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
print(left_rotate(arr))