import sys; sys.stdin = open('123.txt', 'r')

n, m = list(map(int, input().split()))

arr = list(map(int, input().split()))

maxV = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sumV = arr[i] + arr[j] + arr[k]
            if sumV <= m and maxV < sumV:
                maxV = arr[i] + arr[j] + arr[k]

print(maxV)
