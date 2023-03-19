import sys; sys.stdin = open('123.txt', 'r')

a, b = list(map(int, input().split()))

lst = []
for i in range(1, a+1):
    lst.append([i, 0])

result = []
a = -1
b = 0
c = 0
while a != len(lst):
    a += 1
    if a == 2:
        if lst[a][1] == 0:
            result.append(lst[a][0])
            lst[a][1] = 1
            c += 1

            if a > len(lst):
                a = -1
        else:
            a -= 1