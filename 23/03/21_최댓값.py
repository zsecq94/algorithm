import sys; sys.stdin = open('123.txt', 'r')


result = [0, 0]
for i in range(9):
    n = int(input())
    if result[0] < n:
        result[0] = n
        result[1] = i+1

for i in result:
    print(i)