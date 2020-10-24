def consecutive(arr, a, b):
    if arr.index(b) == arr.index(a) + 1:
        return True
    elif arr.index(a) == arr.index(b) + 1:
        return True
    else:
        return False

consecutive([1, 3, 5, 7], 3, 7)
consecutive([1, 3, 5, 7], 3, 1)
consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4)