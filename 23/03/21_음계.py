import sys; sys.stdin = open('123.txt', 'r')

lst = list(map(int, input().split()))
result = ''

if lst[0] + 1 == lst[1]:
    for i in range(len(lst) - 1):
        if lst[i] + 1 != lst[i + 1]:
            result = 'mixed'
            break
        else:
            continue
    if result == '':
        result = 'ascending'

elif lst[0]-1 == lst[1]:
    for i in range(len(lst) - 1):
        if lst[i] - 1 != lst[i + 1]:
            result = 'mixed'
            break
        else:
            continue
    if result == '':
        result = 'descending'

else:
    result = 'mixed'

print(result)