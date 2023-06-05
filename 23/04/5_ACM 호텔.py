import sys; sys.stdin = open('123.txt', 'r')

for tc in range(int(input())):
    a, b, c = list(map(int, input().split()))

    cnt = 0
    result = ''
    for i in range(1, b+1):
        for j in range(1, a+1):
            cnt += 1
            if cnt == c:
                if i < 10:
                    result = str(j) + '0' + str(i)
                    break
                else:
                    result = str(j) + str(i)
                    break

    print(result)