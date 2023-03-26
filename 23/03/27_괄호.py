import sys; sys.stdin = open('123.txt', 'r')


for tc in range(int(input())):
    a = list(input())
    st = []
    for i in a:
        if i == "(":
            st.append(i)
        else:
            if st:
                if st[-1] == '(':
                    st.pop(-1)
            else:
                st.append(i)

    if len(st) == 0:
        print('YES')
    else:
        print('NO')
