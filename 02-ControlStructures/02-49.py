dniTygodnia = ['PN', 'WT', 'SR', 'CZ', 'PT', 'SB', 'ND']
nrDniaTygodnia = 6
dlugoscMiesiaca = 30
kalendarz = []

# # 0 - PN 
# # 1 - WT
# # 2 - SR
# # 3 - CZ
# # 4 - PT
# # 5 - SB
# # 6 - ND

# DODAJEMY OFFSET - PRZÓD
for i in range( nrDniaTygodnia):
    kalendarz.append("  ")

# DODAJEMY DNI
for i in range(1 , 31):
    if i<10:
        kalendarz.append(" " + str(i))
    else:
        kalendarz.append(i)

for i in range(0, 7 - len(kalendarz)%7):
    kalendarz.append("  ")

# WYPISZ formatkę
for i in range(len(dniTygodnia)):
    print('| ', dniTygodnia[i], ' ', end = '')
print(' |')

# WYPISZ dni miesiąca
for i in range(int(len(kalendarz)/7)):
    for k in range(7):
        print('| ', kalendarz[(i * 7) + k], ' ', end = '')
    print(' |')
    