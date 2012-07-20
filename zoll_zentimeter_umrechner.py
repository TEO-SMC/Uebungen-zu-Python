# -*- coding: cp1252 -*-
# Zoll zu Zentimeter Umrechner (C) Tom Eschment

#Ausgabe
print("Zoll zu Zentimeter Umrechner (C) Tom Eschment")

#Var. definition
fehler = 1

#While-Schleife 1
while fehler == 1:

#Vorauswahl
    print("Wollen Sie Zentimeter in Zoll[1] oder Zoll in Zentimeter[2] umwandeln? Bitte geben sie den passenden Wert an. Um was Programm zu beenden geben Sie bitte den Wert 0 an.")
    vorauswahl = input()

#Versuch Eingabe in Zahl umzuwandeln 1
    try:
        vorauswahlz = int(vorauswahl)

#Fehlermeldung 1
    except:
        print("Sie haben keinen passenden Wert eingegeben, bitte versuchen Sie es erneut.")
    

#Verzweigung 1 
    if vorauswahlz == 1:
        print("Bitte geben Sie den Zentimeter-Wert an, welcher in Zoll umgewandelt werden soll, um das Programm zu beenden geben Sie bitte den Wert 0 an.")
        z = input()
        fehler = 2
    elif vorauswahlz == 2:
        print("Bitte geben Sie den Zoll-Wert an, welcher in Zentimeter umgewandelt werden soll, um das Programm zu beenden geben Sie bitte den Wert 0 an.")
        z = input()
        fehler = 2

#Ende 1
    elif vorauswahlz == 0:
        print("Sie haben das Programm beendet")
        fehler = 0

#Fehlermeldung 1
    else:
        print("Sie haben keinen passenden Wert angegeben bitte versuchen Sie es erneut")
        fehler = 1

#Whiler-Schleife 2
while fehler == 2:

#Versuch Eingabe in Zahl umzuwandeln 2
    try:
        zahl = float(z)

#Ende 2
        if zahl == 0:
            print("Sie haben das Programm beendet")
            fehler = 0

#Verzweigung 2
        elif vorauswahlz == 1:

#Ausgabe des Umgewandelten Wertes 1
            print(zahl, "cm =", zahl/2.54, "Zoll")
            fehler = 1
            break
        
#Ausgabe des Umgewandeltes Wertes 2
        else:
            print(zahl, "Zoll =", zahl*2.54, "cm")
            fehler = 1
            break
            
#Fehlermeldung 2
    except:
        print("Sie haben keine Zahl eingegeben, bitte versuchen sie es erneut.")