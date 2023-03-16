import sys; sys.stdin = open('123.txt', 'r')

x, y = list(map(int, input().split()))
if y >= 45:
    print(x, y-45)
elif x == 0 and y < 45:
    print(23, 60-(45-y))
else:
    print(x-1, 60-(45-y))