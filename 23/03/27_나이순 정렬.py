import sys; sys.stdin = open('123.txt', 'r')

arr = []
for tc in range(int(input())):
    a, b = input().split()
    arr.append([int(a), b])

arr.sort(key=lambda x:x[0])
for i in arr:
    print(i[0], i[1])