import sys; sys.stdin = open('123.txt', 'r')

for i in range(1, int(input())+1):
    a = input().split(' ')
    num = int(a[0])
    str = a[1]
    a = 0
    result = ''
    for i in str:
        while a != num:
            a += 1
            result += i
        if a == num:
            a = 0

    print(result)
