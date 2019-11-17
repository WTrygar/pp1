imiona = ["Janek", "Ania", "Wojtek", "Zosia"]
imie = "Tadeusz"

def jestImie(m,n):
    if m in n:
        print ("imię jest zawarte w wykazie imion")
    else:
        print ("imię nie jest zawarte w wykazie imion")

jestImie(imie, imiona)
