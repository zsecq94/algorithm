
result = []
for i in list(map(int, input().split())):
    a = list(str(i))
    resultV = ''
    for j in range(len(a)-1, -1,  -1):
        resultV += a[j]

    result.append(int(resultV))

print(max(result))