import sys; sys.stdin = open('123.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))

max = -999999999999
min = 99999999999

for i in arr:
    if max < i:
        max = i
    if min > i:
        min = i

print(min, max)