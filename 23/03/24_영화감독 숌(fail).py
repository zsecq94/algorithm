import sys; sys.stdin = open('123.txt', 'r')

n = int(input())

a = 0
for i in range(n):
    if i == 1:
        a += 666
    else:
        a += 1000

print(a)