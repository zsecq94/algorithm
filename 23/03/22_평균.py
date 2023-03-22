import sys; sys.stdin = open('123.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))

M = max(arr)
result = []
for i in arr:
    a = i/M*100
    result.append(a)

print(sum(result)/N)
