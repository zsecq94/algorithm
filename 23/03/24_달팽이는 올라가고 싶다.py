import sys; sys.stdin = open('123.txt', 'r')

# a, b, c = list(map(int, input().split()))
#
# goal = 0
# num = 0
# while goal < c:
#     goal += a
#     num += 1
# if goal - b > c:
#     print(num)
# else:
#     print(num+1)

a, b, c = list(map(int, input().split()))

goal = 1
day = 0
while goal != c:
    goal -= b
    day += 1
    for i in range(a):
        goal += 1
        if goal == c:
            break

print(day)