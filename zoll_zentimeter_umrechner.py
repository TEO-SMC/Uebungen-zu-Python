# -*- coding: cp1252 -*-
# Zoll zu Zentimeter Umrechner (C) Tom Eschment

#Var. definition 1
fehler = 1

#While-Schleife 1
while fehler == 1:

#Ausgabe
    print("Zoll zu Zentimeter Umrechner (C) Tom Eschment")
    fehler = 2

#While-Schleife 2
    while fehler == 2:

#Vorauswahl
        print("Wollen Sie Zentimeter in Zoll[1] oder Zoll in Zentimeter[2] umwandeln? Bitte geben sie den passenden Wert an. Um was Programm zu beenden geben Sie bitte den Wert 0 an.")
        vorauswahl = input()

#Versuch Eingabe in Zahl umzuwandeln 1
        try:
            vorauswahlz = int(vorauswahl)

#Fehlermeldung 1
        except:
            print("Sie haben keinen passenden Wert eingegeben, bitte versuchen Sie es erneut.")
            continue
    
#Verzweigung 1 
        if vorauswahlz == 1:
            print("Bitte geben Sie den Zentimeter-Wert an, welcher in Zoll umgewandelt werden soll, um das Programm zu beenden geben Sie bitte den Wert 0 an.")
            z = input()
        elif vorauswahlz == 2:
            print("Bitte geben Sie den Zoll-Wert an, welcher in Zentimeter umgewandelt werden soll, um das Programm zu beenden geben Sie bitte den Wert 0 an.")
            z = input()

#Ende 1
        elif vorauswahlz == 0:
            print("Sie haben das Programm beendet.")
            fehler = 0
            break

#Fehlermeldung 1
        else:
            print("Sie haben keinen passenden Wert angegeben bitte versuchen Sie es erneut.")
            fehler = 2
            continue

#Versuch Eingabe in Zahl umzuwandeln 2
        try:
            zahl = float(z)

#Ende 2
            if zahl == 0:
                print("Sie haben das Programm beendet.")
                fehler = 0
                break
    
#Verzweigung 2
            elif vorauswahlz == 1:

#Ausgabe des Umgewandelten Wertes 1
                umgewandelt = zahl/2.54
                print(zahl, "cm =", umgewandelt, "Zoll.")
                fehler = 3
                cmzoll = 1
        
#Ausgabe des Umgewandeltes Wertes 2
            else:
                umgewandelt = zahl*2.54
                print(zahl, "Zoll =", umgewandelt, "cm.")
                fehler = 3
                cmzoll = 2
        
#Fehlermeldung 2
        except:
            print("Sie haben keine Zahl eingegeben, bitte versuchen sie es erneut.")

#While-Schleife 3
    while fehler == 3:

#Rundungsabfrage 1
        print("Wollen Sie diesen Wert runden? Um zu runden drücken Sie bitte die 1, um eine weitere Zahl umzuwandeln die 2, ansonsten die 0.")
        runden = input()

#Versuch Eingabe in Zahl umzuwandeln 3
        try:
            rundenz = int(runden)

#Fehlermeldung 3
        except:
             print("Sie haben keinen passenden Wert eingegeben.")
             fehler = 3
             continue
        if rundenz == 2:
            fehler = 1
            continue

#Rundungsabfrage 2
        print("Auf welche Nachkommastelle wollen sie ihren Wert runden?")
        x = input()
        try:
            xz = int(x)

#Fehlermeldung 4
        except:
            print("Sie haben keinen passenden Wert eingegeben, bitte versuchen Sie es erneut.")
            fehler = 3
            continue
        if xz == 0:
            print("Sie haben das Programm beendet.")
            fehler = 0
            break

#Verzweigung
        if rundenz == 1 and cmzoll == 1:
            print("Ihr gerundeter Wert berägt", round(umgewandelt,xz), "Zoll.")
            fehler = 1
            continue
        elif rundenz == 1 and cmzoll == 2:
            print("Ihr gerundeter Wert beträgt", round(umgewandelt,xz), "cm.")
            fehler = 1
            continue
        elif rundenz == 0:
            print("Sie haben das Programm beendet,")
            fehler = 0
            break

#Fehlermeldung 5
        else:
            print("Sie haben keinen passenden Wert eingegeben, bitte versuchen Sie es erneut.")
            fehler = 3
            continue