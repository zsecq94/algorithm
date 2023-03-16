import sys; sys.stdin = open('123.txt', 'r')

a, b = list(map(int, input().split()))

lst = []
for i in range(1, a+1):
    lst.append(i)

result = []
a = 0
b = -1
while len(lst) > 0:
    if a == 3:
        result.append(lst[b])
        lst.remove(lst[b])
        b -= 1
        a = 0
    if b > len(lst):
        b = 0
    a += 1
    b += 1
