x = float(input("Podaj swój wzrost w cm: "))
y = float(input("Podaj masę ciała w kg: "))

BMI = y / (x**2) * 10000
print("{0:.{1}f}".format(y / (x**2) * 10000,2))