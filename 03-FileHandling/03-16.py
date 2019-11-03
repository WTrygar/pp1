import re

komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
print(cyfry)
print("średnia prognozowana pogoda: ")
x = float(cyfry[0] + cyfry[1] + cyfry[2])/3
print(x)