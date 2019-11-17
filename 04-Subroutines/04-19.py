N = 500 #int(input("Podaj liczbę: "))

def Suma(N):
  if(N > 0):
    result = N + Suma(N - 1)
    #print(result)
  else:
    result = 0
  return result


print(Suma(N))

