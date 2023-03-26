import sys

input = sys.stdin.readline
st = []
for i in range(int(input())):
    a = input().split()
    if a[0] == 'push':
        st.append(int(a[1]))
    elif a[0] == 'top':
        if st:
            print(st[-1])
        else:
            print(-1)
    elif a[0] == 'pop':
        if st:
            p = st.pop(-1)
            print(p)
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(st))
    else:
        if len(st) > 0:
            print(0)
        else:
            print(1)