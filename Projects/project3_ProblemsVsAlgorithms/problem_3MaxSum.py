def partition(input_list, begin, end):
    left = begin
    pivot_index = end
    pivot_value = input_list[pivot_index]

    while pivot_index != left:
        temp = input_list[left]
        if temp <= pivot_value:
            left += 1
            continue

        input_list[left] = input_list[pivot_index - 1]
        input_list[pivot_index - 1] = pivot_value
        input_list[pivot_index] = temp
        pivot_index -= 1
    return pivot_index


def quick_sort(input_list, begin, end):
    if end <= begin:
        return

    pivot = partition(input_list, begin, end)
    quick_sort(input_list, begin, pivot - 1)
    quick_sort(input_list, pivot + 1, end)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    first_num = ""
    second_num = ""

    # We will use quick sort to sort the array.
    quick_sort(input_list, 0, len(input_list) - 1)
    # We are appending the elements from the end of list
    for i in range(len(input_list) - 1, -1, -1):
        if i & 1:
            second_num += str(input_list[i])
        else:
            first_num += str(input_list[i])

    first_num = int(first_num)
    second_num = int(second_num)
    # print(first_num)
    # print(second_num)
    return [first_num, second_num]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])         # Passes
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])     # Passes