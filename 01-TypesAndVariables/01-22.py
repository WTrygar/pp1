import math

a = int(input("Podaj długość boku a: "))
b = int(input("Podaj długość boku b: "))
c = int(input("Podaj długość boku c: "))
p = (a + b + c)/2

Pole_trójkąta = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(Pole_trójkąta)