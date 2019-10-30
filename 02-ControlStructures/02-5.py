wiek = int(input("podaj wiek: "))

if wiek > 18:
    print("Osoba pełnoletnia")
elif wiek < 18 and wiek > 0:
    print("Osoba niepełnoletnia")
else:
    print("Nie można mieć ujemnej liczby lat")