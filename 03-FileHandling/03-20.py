plik = open('numbers.txt','r')
plik_2 = open('evennumbers.txt','w')
for line in plik:
    a = int(line)
    if a%2 == 0:
        plik_2.write(line)
plik.close()
plik_2.close()