n = int(input('wprowdź liczbę całkowitą: '))
x = 0
y = 1
print(x, end=" ")
print(y, end=" ")
for i in range(1,n-1):
    z = y
    y = y + x
    print(y, end=" ")
    x = z