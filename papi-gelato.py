def snapNiet():
    print("Denkie dat ik dat snap joh, mooie kloothommel die je d'r bent!")

def alles():
    print()
    print("Welkom bij 't Ijsschuurtie je mag alle smaken lopen te kiezen zolang het maar vanille is.")
    print()

    
    def bolletjes():

        def nogmeer():
            nogmeervraag = input("Mot je nog wat anders vreten? (JA of NEE) ").lower()
            if nogmeervraag == "ja":
                bolletjes()
                print()
            if nogmeervraag == "nee":
                print("Danku! En nou opvliegen uit m'n tent!")
                
            else:
                snapNiet()
                print()
                nogmeer()

        
        try:
            aantalbolletjes = int(input("Hoeveel bolleties ijs willie? "))

            def stap2():
                hoorn_bak = input(f"Willie deze {aantalbolletjes} bolleties op (A) een hoorntie of (B) een bakkie? ").lower()

                def stap3_1():
                    print(f"Hiero! Je hoorntie met {aantalbolletjes} bolleties!")
                    nogmeer()
                
                def stap3_2():
                    print(f"Hiero! Je bakkie met {aantalbolletjes} bolleties!")
                    nogmeer()

                if hoorn_bak == "a":
                    stap3_1()
                elif hoorn_bak == "b":
                    stap3_2()
                else: 
                    snapNiet()
                    print()
                    stap2()

            if aantalbolletjes <= 8 and aantalbolletjes >= 4:
                print(f"Toppie! Dan krijgie van mij een bakkie met {aantalbolletjes} bolleties, anders wordt 't een beetje veel op zo'n hoorntie snappie?")
                
                
            elif aantalbolletjes <= 0:
                print("Rot dan maar op uit onze prachtige ijssalon, ouwe geepekop! Wie denkie nou dat je ben!")
                bolletjes()
            elif aantalbolletjes > 8:
                print("Wa denkie nou? Dat je alleen ben op deze aardkloot, andere mensen willen ook ijsie naar achter schuiven!")
                bolletjes()
                print()
            elif aantalbolletjes > 0 and aantalbolletjes <= 3:
                print("")
                stap2()
            else:
                snapNiet() 
            
        except:
            snapNiet()
            bolletjes()
            print()
            
        
    bolletjes()
alles()