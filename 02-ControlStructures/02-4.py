wiek = int(input("podaj wiek: "))

if wiek > 10:
    print("Więcej jak 10 lat")
elif wiek < 10 and wiek > 0:
    print("Mniej jak 10 lat")
else:
    print("Nie można mieć ujemnej lcizby lat")