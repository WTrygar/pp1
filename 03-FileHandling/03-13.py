a = [32, 16, 5, 8, 24, 7]
with open('Liczby','w') as file:

    for x in range (len(a)):
        d=str(a[x])+('\n')  
   
        file.write(d)
