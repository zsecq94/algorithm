import sys; sys.stdin =open('123.txt', 'r')

arr = [0] * 10001
n = int(input())
for i in range(n):
    b = int(input())
    arr[b] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
