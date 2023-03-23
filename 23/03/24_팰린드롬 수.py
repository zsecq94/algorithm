import sys; sys.stdin=open('123.txt', 'r')
input=sys.stdin.readline

a = int(sys.stdin.readline())

b = list(reversed(a))
c = ''.join(b)
if int(a[0]) > 0:
    if a == c:
        print('yes')
    else:
        print('no')
