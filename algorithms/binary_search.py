def binary_search(array, left, right, x):
    while left < right:
        mid = left + (right - left) / 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

        return -1