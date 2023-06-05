file = open("123.txt", "r")
line = file.readline()

while line:
    line = file.readline()
    for i in line:
        print(i)