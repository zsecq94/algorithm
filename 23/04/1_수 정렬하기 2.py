import sys; sys.stdin=open('123.txt', 'r')

arr = []
for i in range(int(input())):
    arr.append(int(input()))

for j in sorted(arr):
    print(j)