import sys;sys.stdin = open('123.txt', 'r')

arr = []
for tc in range(int(input())):
    a, b = list(map(int, input().split()))
    arr.append([a, b])
arr.sort()
for i in arr:
    print(i[0], i[1])