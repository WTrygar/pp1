x = int(input("podaj szerokość prostokąta: "))
y = int(input("podaj długość prostokąta: "))
if x < 0 or y < 0:
    print("Wymiary podaj w liczbach dodatnich")
for i in range(1,x+1):
    print(y*"*")