import sys; sys.stdin=open('123.txt', 'r')

for t in range(int(input())):
    a = int(input())
    b = int(input())

    arr = [0] * b
    for i in range(a):
        for j in range(b):
            if i == 0:
                arr[j] = j+1
            else:
                if j != 0:
                    arr[j] = arr[j-1] + arr[j]
    print(sum(arr))

