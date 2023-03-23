import sys; sys.stdin = open('123.txt', 'r')

a, b, c, d = list(map(int, input().split()))

result = 99999
if d - b < result:
    result = d - b
if c - a < result:
    result = c - a
if a < result:
    result = a
if b < result:
    result = b

print(result)