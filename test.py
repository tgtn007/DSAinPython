for _ in range(int(input())):
    alpha = list(map(int, input().split()))
    leen = dict()

    for _ in range(alpha[0]):
        s = input()
        if len(s) not in leen:
            leen[len(s)] = 0
        leen[len(s)] += 1

    # print(leen)
    count = 0
    ans = True
    for al, val, in leen.items():
        if val % alpha[1] :
            ans = False
    if ans:
        print("Possible")
    else:
        print("Not possible")

