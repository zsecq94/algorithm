import sys; sys.stdin = open('123.txt', 'r')

sumV = int(input())
for i in range(2):
    sumV *= int(input())

lst = list(str(sumV))
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in lst:
    result[int(i)] += 1

for i in result:
    print(i)