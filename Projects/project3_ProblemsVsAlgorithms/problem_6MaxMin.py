def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return (None, None)

    maax = float('-inf')  # Initializing the max value with lowest possible value
    miin = float('inf')  # Initializing the  min value with highest possible value

    # Traversing the list once to check all the elements.
    for i in range(len(ints)):
        if ints[i] > maax:
            maax = ints[i]
        if ints[i] < miin:
            miin = ints[i]
    return (miin, maax)


## Example Test Case of Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")  # Passes

l = [i for i in range(344, 1000)]  # a list containing 344 - 999
random.shuffle(l)
print("Pass" if ((344, 999) == get_min_max(l)) else "Fail")  # Passes

l = []
print("Pass" if ((None, None) == get_min_max(l)) else "Fail")  # Passes
