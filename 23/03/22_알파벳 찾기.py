import sys; sys.stdin = open('123.txt', 'r')

arr = list(input())
result = [-1] * 26
num = 0
for i in arr:
    a = ord(i) - 97
    result[a] = num
    num += 1

print(result)