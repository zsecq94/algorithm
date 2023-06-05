import sys;sys.stdin = open('123.txt', 'r')

result = []
for tc in range(int(input())):
    a = int(input())
    if a != 0:
        result.append(a)
    else:
        result.pop(-1)

if len(result) == 0:
    print(0)
else:
    print(sum(result))