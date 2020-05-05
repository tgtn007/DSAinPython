def binary_search(arr, number, left):
    if len(arr) == 0:
        return None
    mid = (len(arr) - 1) // 2
    if arr[mid] == number:
        return mid + left
    elif arr[mid] < number:
        return binary_search(arr[mid + 1:], number, left + mid + 1)
    else:
        return binary_search(arr[:mid - 1], number, left)


def first_and_last_index(source, number):
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """

    # TODO: Write your first_and_last function here
    # Note that you may want to write helper functions to find the start
    # index and the end index
    index = binary_search(source, number, 0)
    res = list()
    if index == None:
        return [-1, -1]

    left = index
    while source[left] == number:
        if left == 0:
            res.append(left)
            break
        if source[left - 1] == number:
            left -= 1
        else:
            res.append(left)
            break

    right = index
    while source[right] == number:
        if right == len(source) - 1:
            res.append(right)
            break
        if source[right + 1] == number:
            right += 1
        else:
            res.append(right)
            break
    return res
    pass

arr = [1]
number = 1
index = binary_search(arr, number, 0)
print(index)
res = first_and_last_index(arr, number)
print(res)