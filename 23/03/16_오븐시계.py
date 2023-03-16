import sys; sys.stdin = open('123.txt', 'r')

a, b = list(map(int, input().split()))
c = int(input())

A = 0
B = 0
if b + c > 60:
    A = (b+c)//60
    B = (b+c) - (A * 60)
    if B == 60:
        B = 0
    for i in range(1, A+1):
        a += 1
        if a > 23:
            a = 0

    print(a, B)
else:
    q = b + c
    if q == 60:
        q = 0
        a += 1
    if a == 24:
        a = 0
    print(a, q)

