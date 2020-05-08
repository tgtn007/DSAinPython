a, b = map(int, input().split())
# a = int(a)
# b = int(b)
temp = a - b

ans = []
for i in range(b):
    ans.append(a)
    a -= 1

add = 1
for i in range(temp):
    ans.append(add)
    add += 1

for item in ans:
    print(item, end = " ")