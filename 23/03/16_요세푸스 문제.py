import sys; sys.stdin = open('123.txt', 'r')

a, q = list(map(int, input().split()))

lst = []
for i in range(1, a+1):
    lst.append([i, 0])
result = []
a = -1
b = -1
c = 0
while c != len(lst):
    a += 1
    b += 1
    if b > len(lst)-1:
        b = 0
    if lst[b][1] == 0:
        if a == q-1:
            result.append(lst[b][0])
            lst[b][1] = 1
            c += 1
            a = -1
            if a > len(lst):
                a = -1
    else:
        a -= 1

a = ", ".join(map(str, result))
print(f'<{a}>')