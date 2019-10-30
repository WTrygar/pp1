myNumb = 7 
while not (myNumb % 6 == 1 and myNumb % 5 == 1 and myNumb % 4 == 1 and myNumb % 3 == 1 and myNumb % 2 == 1):
    myNumb += 7

else:
    print('Pierwsza liczba która spełnia ten warunek, to: ', myNumb)