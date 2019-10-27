x = 5

for i in range(x):
    y = ""
    for j in range(i):
        y = y + "*"
    print(y)

for i in range(x):
    y = ""
    for j in range(x-i):
        y = y + "*"
    print(y)