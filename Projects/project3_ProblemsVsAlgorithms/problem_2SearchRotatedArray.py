def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Check for blank list
    if len(input_list) == 0:
        return -1

    # Finding the pivot where from the array is rotated
    left = 0
    right = len(input_list) - 1
    while left < right:
        midpoint = left + (right - left) // 2
        if input_list[midpoint] > input_list[right]:
            left = midpoint + 1
        else:
            right = midpoint

    start = left
    left = 0
    right = len(input_list) - 1

    # Checking in which side the target will lie
    if input_list[start] <= number <= input_list[right]:
        left = start
    else:
        right = start

    # Normal Binary Search to find the element
    while left <= right:
        mid = left + (right - left) // 2
        if input_list[mid] == number:
            return mid
        elif input_list[mid] > number:
            right = mid - 1
        else:
            left = mid + 1

    return -1

    pass


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])    # Passes
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])    # Passes
test_function([[6, 7, 8, 1, 2, 3, 4], 8])           # Passes
test_function([[6, 7, 8, 1, 2, 3, 4], 1])           # Passes
test_function([[6, 7, 8, 1, 2, 3, 4], 10])          # Passes
