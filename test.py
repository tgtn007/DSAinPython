for _ in range(int(input())):
    para = list(map(int, input().split()))
    equal = list()
    not_equal = list()
    ans = True
    for i in range(para[1]):
        string = input()
        if len(string) == 5:
            add = [string[0], string[-1]]
            if add in not_equal:
                ans = False
            else:
                equal.append(add)
        else:
            add = [string[0], string[-1]]
            if add in equal:
                ans = False
            else:
                not_equal.append(add)
    if ans:
        print("YES")
    else:
        print("NO")