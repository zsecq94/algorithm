import sys; sys.stdin = open('123.txt', 'r')

a = int(input())
num = a
result = 999999999999
while a != 0:
    a -= 1
    b = list(str(a))
    sumV = 0
    for i in b:
        sumV += int(i)
    if sumV + a == num and result > a:
        result = a


if result == 999999999999:
    print(0)
else:
    print(result)


