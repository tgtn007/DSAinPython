ans = 0
for _ in range(int(input())):
    a = list(map(int, input().split()))
    if a[1] - a[0] >= 2:
        ans+=1
print(ans)