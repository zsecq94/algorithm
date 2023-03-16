import sys; sys.stdin = open('123.txt', 'r')

a, b = list(map(int, input().split()))

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')