import time


aantalbolletjes = 0
totaalbolletjes = 0
totaalhoornties = 0
aantalhoornties = 0
totaalbakkies = 0
aantalbakkies = 0
prijsbolletjes = 1.10
prijshoorn = 1.25
prijsbak = 0.25

i = 0 


def snapNiet():
    time.sleep(2)
    print()
    print("Denkie dat ik dat snap joh, mooie kloothommel die je d'r bent!")
    time.sleep(2)
    print()

def bonnetje():

    totaalPrijsBollen = round(totaalbolletjes * prijsbolletjes,2)
    totaalPrijsHoorn = round(totaalhoornties * prijshoorn,2)
    totaalPrijsBak = round(totaalbakkies * prijsbak,2)
    totaalPrijs = round(totaalPrijsBollen + totaalPrijsHoorn + totaalPrijsBak, 2)

    print("------------['t Ijsschuurtie']------------")
    print(f"Bolleties:     {totaalbolletjes} X {prijsbolletjes}   =   € {totaalPrijsBollen}")
    if totaalhoornties > 0:
        print(f"Hoornties:     {totaalhoornties} X {prijshoorn}   =   € {totaalPrijsHoorn}")
    if totaalbakkies > 0:
        print(f"Bakkies:       {totaalbakkies} X {prijsbak}   =   € {totaalPrijsBak}")
    print("------------------------------------------")
    print(f"Totaal: € {totaalPrijs} ")
    print("------------------------------------------")
    print("----['De ballen, laat ze niet vallen']----")
    print("------------------------------------------") 
    print()                         
        
    


def doorbestellen():
    nogmeer = input("Willie nog meer zooi bestellen? (J) Ja of (N) Nee? ").lower()
    if nogmeer == "j":
        time.sleep(2)
        print()
        bolletjes()
    elif nogmeer == "n":
        print()
        time.sleep(2)
        print("Hier je bonnetje! Kom van de week maar weer een keer terug als je uit gekotst bent van dit vieze ijs!")
        print()
        time.sleep(2)
        bonnetje()
    else:
        snapNiet()
        doorbestellen()

def bak():
    global aantalbolletjes
    global aantalbakkies
    global totaalbakkies

    time.sleep(2)
    print(f"Daar is ie hoor, hier pak aan je bakkie met {aantalbolletjes} bolleties! ")
    print()
    totaalbakkies += 1
    time.sleep(2)
    doorbestellen()
    


def hoorn():
    global aantalbolletjes
    global aantalhoornties
    global totaalhoornties

    time.sleep(2)
    print(f"Daar is ie hoor, hier pak aan je hoorntie met {aantalbolletjes} bolleties! ")
    print()
    totaalhoornties += 1
    time.sleep(2)
    doorbestellen()


def bakjehoorn():
    global aantalbolletjes
    bakofhoorn = input(f"Willie deze {aantalbolletjes} bolleties in een (B) bakkie of een (H) hoorntie? ").lower()
    if bakofhoorn == "b":
        print()
        bak()
    elif bakofhoorn == "h":
        print()
        hoorn()
    else:
        snapNiet()
        bakjehoorn()

def smaken():
    for i in range(1, aantalbolletjes + 1):
         welkesmaak = input(f"Wat voor smaak mot je hebben voor bolletie nummer {i} (A) Aardbei, (C) Chocolade, (V) Vanille? of (M) Munt? ").upper()
         print()
    if welkesmaak == "A" or welkesmaak == "C" or welkesmaak == "M" or welkesmaak == "V":
        print()
        bakjehoorn()
    else:
        snapNiet()
        smaken()

def smakenGroot():
    for i in range(1, aantalbolletjes + 1):
         welkesmaak = input(f"Wat voor smaak mot je hebben voor bolletie nummer {i} (A) Aardbei, (C) Chocolade, (V) Vanille? of (M) Munt? ").upper()
         print()
    if welkesmaak == "A" or welkesmaak == "C" or welkesmaak == "M" or welkesmaak == "V":
        bak()
    else:
        snapNiet()
        smakenGroot()
        
    

def bolletjes():

    global aantalbolletjes
    global totaalbolletjes
 
    aantalbolletjes = input("Hoeveel bolleties ijs mot je hebben? ")

    if aantalbolletjes.isnumeric():
        aantalbolletjes = int(aantalbolletjes)

        if aantalbolletjes <= 8 and aantalbolletjes >= 4:
            print()
            time.sleep(2)
            totaalbolletjes += aantalbolletjes
            smakenGroot()
        elif aantalbolletjes <= 0:
            print()
            print("Rot dan maar op uit onze prachtige ijssalon, ouwe geepekop! Wie denkie nou dat je ben!")
            time.sleep(2)
            print()
            bolletjes()
        elif aantalbolletjes > 8:
            print()
            print("Wa denkie nou? Dat je alleen ben op deze aardkloot, andere mensen willen ook ijsie naar achter schuiven!")
            time.sleep(2)
            print()
            bolletjes()
        elif aantalbolletjes > 0 and aantalbolletjes <= 3:
            print()
            totaalbolletjes += aantalbolletjes
            smaken()

    else:
        snapNiet()
        bolletjes()


def main():
    print()
    print("Welkom bij 't Ijsschuurtie, je mag alle smaken lopen te kiezen zolang het maar voor je snuffert in die vrieskist leg!")
    print()
    time.sleep(2)
    bolletjes()

main()

