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
    inwestycja=int(input("Podaj ile masz pieniedzy "))
    print("GRASZ W LOTTO")
    print("Wygrywasz cos przy juz odgadnieciu 3 liczb!!!")
    print("Tak wygladaja mnozniki za 3 liczby 2 krotnie za 4 trzykrotnie za 5 czterokrotnie a za komplet az 10")
    print("Kupiles los na lotto za 10 zl")
    inwestycja += -10
    print(f"\nTo sa twoje obecne pieniadze: {inwestycja}")


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
        inwestycja += inwestycja
        print(f"\nTo sa twoje pieniadze po wygranej: {inwestycja}")
    elif trafione==4:
        print("Gratulacje wygrales cos ")
        inwestycja += inwestycja*2
        print(f"\nTo sa twoje pieniadze po wygranej: {inwestycja}")
    elif trafione==5:
        print("Gratulacje wygrales fajna sumke ")
        inwestycja += inwestycja*3
        print(f"\nTo sa twoje pieniadze po wygranej: {inwestycja}")
    elif trafione==6:
        print("Gratulacje wygrales Fortune ")
        inwestycja += inwestycja*9
        print(f"\nTo sa twoje pieniadze po wygranej: {inwestycja}")
    else:
        print("Nic nie wygrales unlucky")

if __name__ == "__main__":
    main()



 







    

