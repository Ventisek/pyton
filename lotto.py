import random


def losowanie_lotto():
    wylosowane_liczby = set()

    while len(wylosowane_liczby) < 6:
        liczba = random.randint(1, 49)
        wylosowane_liczby.add(liczba)

    return sorted(wylosowane_liczby)

def sprawdz_wynik(liczby_gracza, wylosowane):
    trafione = set(liczby_gracza) & set(wylosowane)
    return len(trafione)

def main():
    los=int(input("Podaj za ile chcesz kupic los na lotto"))
    print("GRASZ W LOTTO")
    print("Wygrywasz cos przy juz odgadnieciu 3 liczb!!!")
    print("Tak wygladaja mnozniki za 3 liczby 10 krotnie za 20 trzykrotnie za 30 czterokrotnie a za komplet az 50")

    
  


    liczby_gracza = []
    for _ in range(6):
        while True:
            try:
                liczba = int(input("Podaj liczbę od 1 do 49: "))
                if 1 <= liczba <= 49 and liczba not in liczby_gracza:
                    liczby_gracza.append(liczba)
                    break
                else:
                    print("Podana liczba musi byc z zakresu od 1 do 49")
            except ValueError:
                print("Dales niepoprawna liczbe kolezko")


    wylosowane = losowanie_lotto()


    trafione = sprawdz_wynik(liczby_gracza, wylosowane)


    print(f"\nWylosowane liczby Lotto: {wylosowane}")
    print(f"Twoje liczby: {liczby_gracza}")
    print(f"Liczba trafionych liczb: {trafione}")
    if trafione == 3:
        print("Gratulacje wygrales grosze ")
        los += los*9
        print(f"\nTo sa twoje pieniadze po wygranej: {los}")
    elif trafione==4:
        print("Gratulacje wygrales cos ")
        los += los*19
        print(f"\nTo sa twoje pieniadze po wygranej: {los}")
    elif trafione==5:
        print("Gratulacje wygrales fajna sumke ")
        los += los*29
        print(f"\nTo sa twoje pieniadze po wygranej: {los}")
    elif trafione==6:
        print("Gratulacje wygrales Fortune ")
        los += los*49
        print(f"\nTo sa twoje pieniadze po wygranej: {los}")
    else:
        print("Nic nie wygrales unlucky")

if __name__ == "__main__":
    main()



 







    

