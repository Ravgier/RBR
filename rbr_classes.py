#Turnier
class AlleTurniere:
    def __init__(self, turnier):
        self.turnier = turnier
nt1 = AlleTurniere("RetroBros Rampage 2019")

#Spiele
class AlleSpiele:
    def __init__(self, titel, plattform, art):
        self.titel = titel
        self.plattform = plattform
        self.art = art
st1 = AlleSpiele("Spieltitel 1","Konsole 1","solo")
st2 = AlleSpiele("Spieltitel 2","Konsole 2","team")
st3 = AlleSpiele("Spieltitel 3","Konsole 1","both")
st4 = AlleSpiele("Spieltitel 4","Konsole 2","solo")
st5 = AlleSpiele("Spieltitel 5","Konsole 3","both")
st6 = AlleSpiele("Spieltitel 6","Konsole 1","team")
st7 = AlleSpiele("Spieltitel 7","Konsole 4","team")
st8 = AlleSpiele("Spieltitel 8","Konsole 2","both")
st9 = AlleSpiele("Spieltitel 9","Konsole 4","solo")

#Spielrunde
class AlleSpielrunden:
    def __init__(self, runde):
        self.runde = runde
sr1 = AlleSpielrunden("Spielrunde 1")
sr2 = AlleSpielrunden("Spielrunde 2")
sr3 = AlleSpielrunden("Spielrunde 3")
sr4 = AlleSpielrunden("Spielrunde 4")
sr5 = AlleSpielrunden("Spielrunde 5")
sr6 = AlleSpielrunden("Spielrunde 6")
sr7 = AlleSpielrunden("Spielrunde 7")
sr8 = AlleSpielrunden("Spielrunde 8")
sr9 = AlleSpielrunden("optionale Spielrunde 9")

#Spieltabelle
class AlleTabellen:
    def __init__(self, tabelle):
        self.tabelle = tabelle
        #Spieler
        #Punkte
        #Runde

#Teilnehmer
class AlleTeilnehmer:
    def __init__(self, vorname):
        self.vorname = vorname
   #self.istChampion = istChampion