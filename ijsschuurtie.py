import time

aantalbolletjes = 0

def snapNiet():
    time.sleep(2)
    print()
    print("Denkie dat ik dat snap joh, mooie kloothommel die je d'r bent!")
    time.sleep(2)
    print()


def doorbestellen():
    nogmeer = input("Willie nog meer zooi bestellen? (J) Ja of (N) Nee? ").lower()
    if nogmeer == "j":
        time.sleep(2)
        print()
        bolletjes()
    if nogmeer == "n":
        print()
        print("Hey, de mazzels! Kom van de week maar weer een keer terug als je uit gekotst bent van dit vieze ijs!")
    else:
        snapNiet()

def bak():
    global aantalbolletjes
    time.sleep(2)
    print(f"Daar is ie hoor, hier pak aan je bakkie met {aantalbolletjes} bolleties! ")
    print()
    time.sleep(2)
    doorbestellen()
    


def hoorn():
    global aantalbolletjes
    time.sleep(2)
    print(f"Daar is ie hoor, hier pak aan je hoorntie met {aantalbolletjes} bolleties! ")
    print()
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


def bolletjes():

    global aantalbolletjes 
    aantalbolletjes = input("Hoeveel bolleties ijs mot je hebben? ")

    if aantalbolletjes.isnumeric():
        aantalbolletjes = int(aantalbolletjes)

        if aantalbolletjes <= 8 and aantalbolletjes >= 4:
            print()
            bak()
        elif aantalbolletjes <= 0:
            print("Rot dan maar op uit onze prachtige ijssalon, ouwe geepekop! Wie denkie nou dat je ben!")
            time.sleep(2)
            print()
            bolletjes()
        elif aantalbolletjes > 8:
            print("Wa denkie nou? Dat je alleen ben op deze aardkloot, andere mensen willen ook ijsie naar achter schuiven!")
            time.sleep(2)
            print()
            bolletjes()
        elif aantalbolletjes > 0 and aantalbolletjes <= 3:
            print()
            bakjehoorn()

    else:
        snapNiet()
        bolletjes()


def main():
    print()
    print("Welkom bij 't Ijsschuurtie, je mag alle smaken lopen te kiezen zolang het maar vanille ijs is!")
    print()
    time.sleep(2)
    bolletjes()

main()

