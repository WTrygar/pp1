import math

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = (b**2) - 4 * a * c

if delta > 0:
    print("Są dwa miejsca zerowe")
    x1 = ((-b) - (math.sqrt(delta))) / 2 * a 
    print("Pierwsze miejsce zerowe: ", x1)
    x2 = ((-b) + (math.sqrt(delta))) / 2 * a
    print("Drugie miejsce zerowe: ", x2)

elif delta == 0:
    x0 = b / 2 * a
    print("Jest jedno miejsce zerowe: ", x0)
else:
    print("Równanie nie ma miejsc zerowych")