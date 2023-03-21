import sys; sys.stdin = open('123.txt', 'r')

str = input().lower()

lst = []
for i in range(26):
    lst.append(0)

for i in str:
    a = ord(i)-97
    lst[a] += 1

print(lst)