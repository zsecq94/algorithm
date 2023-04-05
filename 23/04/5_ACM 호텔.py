import sys; sys.stdin = open('123.txt', 'r')

for tc in range(int(input())):
    a, b, c = list(map(int, input().split()))
    print(a, b, c)