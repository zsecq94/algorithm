import sys; sys.stdin = open('123.txt', 'r')

str = input().lower()

lst = []
for i in range(30):
    lst.append(0)

for i in str:
    a = ord(i)-97
    # b = chr(a+97)
    lst[a] += 1


for j in lst:
    print(j)