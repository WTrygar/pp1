a = 4
b = 15

for i in range(a):
    if i==0 or i==a-1:
        x = ""
        for j in range(b):
            x = x + "*"
        print(x)
    else:
        x = "*"
        for j in range(b-2):
            x = x + " "
        x = x + "*"
        print(x)