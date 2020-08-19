a = int(input())
b = int(input())


def prime(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


for i in range(a, b + 1):
    if prime(i):
        print(i)
