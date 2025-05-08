"""************************************************
Einsendeaufgabe 3.3
***********************************************"""

# Einlesen des Wertes
zahl = 1


# Ausgabe des Wertes
while zahl <= 100:
    if zahl < 100:
        print(zahl * 2, end=", ")
    else:
        print(zahl * 2)
        
    zahl = zahl + 1