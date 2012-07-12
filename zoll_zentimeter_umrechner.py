# -*- coding: cp1252 -*-
# Zoll zu Zentimeter Umrechnere (R) Tom Eschment

#Ausgabe
print("Zoll zu Zentimeter Umrechner (R) Tom Eschment")

#Var. definition
z = 1
fehler = 1

#While-Schleife
while fehler == 1:
    print("Bitte geben Sie den Zoll-Wert an, welcher in Zentimeter umgewandelt werden soll, um das Programm zu beenden geben Sie bitte den Wert 0 an.")
    z = input()

#Versuch Eingabe in Zahl umzuwandeln
    try:
        zahl = float(z)

#Ende
        if zahl == 0:
            print ("Sie haben das Programm beendet")
            fehler = 0

#Ausgabe des umgewandelten Wertes
        else:
            print(zahl, "Zoll =", zahl*2.54, "cm")

#Fehlermeldung
    except:
        print("Sie haben keine Zahl eingegeben, bitte versuchen sie es erneut.")




