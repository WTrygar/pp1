suma = 0

with open('C:/Users/Strix/Desktop/numbers.txt','r') as file:
    for line in file:
        suma += int(line)
        #print(line, end='')
    print(suma)