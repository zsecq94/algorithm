import sys; sys.stdin = open('123.txt', 'r')

str = input().lower()

lst = []
for i in range(30):
    lst.append(0)

for i in str:
    a = ord(i)-97
    b = chr(a+97)
    print(a, b)
    lst[a] += 1

print(lst)