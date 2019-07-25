def backtoMainMenu():
    print("[Q] Zurück zum Hauptmenü")

def auflister(whatlist):
    for x in range(len(whatlist)):
        ++x
        print('['+str(x+1)+']', whatlist[x])

def subMenuEntries(whatmenu):
    print("[1] Erstellen")
    print("[2] Editieren")
    print("[3] Löschen")
    print("[Q] Zurück")

def whereami():
    pass

"""
Ziel ist es, hiermit subMenuEntries zu ersetzen: eine Kombination aus Listen für die Texte und auflister()
def subMenuEntry(menuname)
    submenulist = ['Erstellen','Editieren','Löschen']
"""

def soloMode(x,spieler):
    shuffle(spieler)
    print("\n" + spiele[x][0] + " in Solo-Mode")
    print(spieler[0] + "\t vs. \t" + spieler[1])
    print(spieler[2] + "\t vs. \t" + spieler[3])
    print(spieler[0] + "\t vs. \t" + spieler[2])
    print(spieler[1] + "\t vs. \t" + spieler[3])
    print(spieler[0] + "\t vs. \t" + spieler[3])
    print(spieler[1] + "\t vs. \t" + spieler[2])
    print("------------------------------")
    
def teamMode(x,spieler):
    shuffle(spieler)
    print("\n" + spiele[x][0] + " in Team-Mode")
    print(spieler[0] + " und " + spieler[1] + "\t vs. \t" + spieler[2] + " und " + spieler[3])
    print("------------------------------")
    
def plan(tnListe):
    
    spieler = tnListe
    shuffle(spiele)
     
    for x in range(len(spiele)):  
    
        if spiele[x][1] == "solo" :
            soloMode(x,spieler)
        elif spiele[x][1] == "team":
            teamMode(x,spieler)
        elif spiele[x][1] == "both":
            rnd = randrange(2)
            if rnd == 0:
                soloMode(x,spieler)
            else:
                teamMode(x,spieler)