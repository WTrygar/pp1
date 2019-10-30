x = float(input("Wprowadź liczbę: "))
y = float(input("Wprowadź liczbę: "))
z = float(input("Wprowadź liczbę: "))
tab = [x,y,z]
tab.sort()
print("Liczby w kolejności rosnącej:",end=" ")
for i in tab:
    print(i,end=" ")