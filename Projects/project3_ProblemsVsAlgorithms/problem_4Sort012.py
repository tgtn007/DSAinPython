def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next0 = 0
    next2 = len(input_list) - 1
    index = 0
    while index <= next2:
        # Condition to put zero at right position
        if input_list[index] == 0:
            input_list[index] = input_list[next0]
            input_list[next0] = 0
            next0 += 1
            index += 1
        # Condition to put two at right position
        elif input_list[index] == 2:
            input_list[index] = input_list[next2]
            input_list[next2] = 2
            next2 -= 1

        else:
            index += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])    # Passes
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])   # Passes
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])    # Passes