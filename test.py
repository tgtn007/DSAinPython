initial = input().split('|')
after = input()
diff = abs(len(initial[0]) - len(initial[1]))
ans = True
if len(after) < diff:
    print("Impossible")
    exit(0)

temp = len(after) - diff
alpha = temp // 2
if temp & 1:
    print("Impossible")
    exit(0)

if len(initial[0]) < len(initial[1]):
    initial[0] += after[:diff]
else:
    initial[1] += after[:diff]

if alpha:
    initial[0] += after[diff:alpha + diff]
    initial[1] += after[alpha + diff:]

print('|'.join(initial))