import sys; sys.stdin=open('123.txt', 'r')

a, b, c = list(map(int, input().split()))

if a == b == c:
    print(10000+(a*1000))
elif a != b and a != c and b != c:
    A = [a, b, c]
    A = sorted(A)
    print(A[-1]*100)
else:
    if a == b:
        print(1000+(a*100))
    elif a == c:
        print(1000 + (a * 100))
    else:
        print(1000 + (b * 100))