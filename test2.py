import random
sekret = random.randint(1, 99)
propozycja = 0
proba = 0
print "AHOJ! Jam jest pirat i mam dla ciebie zagadke"
print "Jest nia tajemna liczba od 1 do 99. Na odgadniecie jej masz 6 prob"
while propozycja != sekret and proba < 6:
    propozycja = input("Jaka to liczba?")
    if propozycja < sekret:
        print "Za mala, psubracie!"
    elif propozycja > sekret:
        print "Za duza, szczurze ladowy!"

    proba = proba + 1

    if propozycja == sekret:
        print "Stop! Udalo ci sie"
        exit();
print "Wykorzystales wszystkie proby! Powodzenia nastepnym razem!"
print "Tajemna liczba, to", sekret
        


        
