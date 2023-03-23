import sys; sys.stdin = open('123.txt', 'r')

arr = []
for i in range(10):
    arr.append(int(input()) % 42)

result = []
for i in arr:
    if i not in result:
        result.append(i)

print(len(result))