def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    start = 0
    end = 1000000
    while start <= end:
        mid = start + (end - start) // 2
        if (mid * mid) == number:
            return mid
        elif (mid * mid) > number:
            end = mid - 1
        else:
            start = mid + 1
    return end
    pass


print ("Pass" if  (3 == sqrt(9)) else "Fail")   # Passes the test case
print ("Pass" if  (0 == sqrt(0)) else "Fail")   # Passes the test case
print ("Pass" if  (4 == sqrt(16)) else "Fail")  # Passes the test case
print ("Pass" if  (1 == sqrt(1)) else "Fail")   # Passes the test case
print ("Pass" if  (6 == sqrt(37)) else "Fail")  # Passes the test case
print ("Pass" if  (5 == sqrt(27)) else "Fail")  # Passes the test case
print ("Pass" if  (1 == sqrt(1)) else "Fail")   # Passes the test case
print ("Pass" if  (3 == sqrt(12)) else "Fail")  # Passes the test case
print ("Pass" if  (56 == sqrt(3136)) else "Fail")   # Passes the test case