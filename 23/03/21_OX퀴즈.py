import sys; sys.stdin = open('123.txt', 'r')

for i in range(int(input())):
    str = list(input())

    num = 0
    result = 0
    for j in str:
        if j == 'O':
            result += num+1
            num += 1
        else:
            num = 0
    print(result)