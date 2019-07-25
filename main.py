"""**********************************
| RetroBros-Rampage Management Tool |
| Version 0.35                      |
| 25.07.2019                        |
**********************************"""

#Daten speichern & laden
import pickle
import json
import os

#Einbinden diverse rbr_*.py
from rbr_base import *
from rbr_classes import *
from rbr_functions import *
#from rbr_structure import *

#Einbinden von random
from random import randrange
from random import shuffle

print("\nWillkommen zum RetroBros-Rampage Management Tool")

################################### Administration #####################################
def AdminMenu():
    print(navpathAdminMenu)
    auflister(AdminMenuList)
    backtoMainMenu()
    while True:
        try:
            auswahl = input(choice).lower()
            if auswahl =='1': #Teilnehmerliste
                text1 = ("\nRBR > Hauptmenü > Administration > Teilnehmerliste")
                print(text1,"\n",len(text1)*"*")
                
                subMenuEntries("Teilnehmerliste")
                auswahl = input(choice).lower()

                if auswahl =='1': #Erstellen
                    print("\nBitte geben Sie die Vornamen an:")

                    TeilnehmerListe = [] #leere Liste erzeugen

                    for teilnehmer in range(maxAnzTeilnehmer):
                        TeilnehmerListe.append(input("Teilnehmer "+str(teilnehmer+1)+": "))
                    with open('rbr_teilnehmerliste.json', 'w') as file:
                        json.dump(TeilnehmerListe, file)

                    AdminMenu()

                elif auswahl =='2': #Editieren
                    print("\nTeilnehmerliste editieren: ")
                    print(26 * "*")

                    with open('rbr_teilnehmerliste.json', 'r') as TeilnehmerListe:
                        geladene_teilnehmer = json.load(TeilnehmerListe)
                        auflister(geladene_teilnehmer)

                elif auswahl =='3': #Löschen
                    break
                else:
                #print(invalid)              
                    break
            elif auswahl =='2':
                break
            elif auswahl =='3':
                break
            elif auswahl =='q':
                MainMenu()
                break
            else:
                print(invalid)
                AdminMenu()
        except ValueError:print(invalid)
    exit

################################### Turnier starten #####################################
def TournamentMenu():
    print(navpathTournamentMenu)
    auflister(TournamentMenuList)
    backtoMainMenu()
    while True:
        try:
            auswahl = input(choice).lower()
            if auswahl =='1':
                TournamentMenu()
            elif auswahl =='2':
                break
            elif auswahl =='3':
                break
            elif auswahl =='q':
                MainMenu()
            else:
                print(invalid)
                TournamentMenu()
        except ValueError:print(invalid)
    exit

#################################### Hauptmenü ##########################################
def MainMenu():
    print(navpathMainMenu)
    auflister(MainMenuList)
    #print("[X] RBR Tool beenden")
    while True:
        try:
            auswahl = input(choice).lower()
            if auswahl =='1':
                AdminMenu()
                #Spielliste initialisieren()
                break
            elif auswahl =='2':
                TournamentMenu()
                    #Tabelle anzeigen()
                    #Nächste Spielrunde starten()
                    #Ergebnis der aktuellen Spielrunde eintragen()
                break
            elif auswahl =='3':
                pass
            elif auswahl =='x':
                exit
            else:
                print(invalid)
                MainMenu()
        except ValueError:print(invalid)
    exit
MainMenu()