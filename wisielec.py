import random

haslo=["skok", "piekny", "ksiezyc", "kot", "samolot", "drzewo", "woda", "latarnia", "ksiazka", "kwiat", "deszcz", "pies", "dom", "slonce", "dzwiek", "kawa", "trawa", "serce", "okno", "milosc", "czas", "tecza", "motyl", "chmura", "muzyka", "lampa", "fala", "snieg", "ocean", "ptak", "ryba", "marzenie", "cieplo", "zima", "lato", "podroz", "stacja", "noc", "dzien", "tajemnica", "zamek", "klucz", "radosc", "tlum", "gora", "las", "tkanina", "miasto", "historia", "szept", "smiech", "zloto", "klos", "kamien", "duma", "krew", "mleko", "kaktus", "most", "pustynia", "kurz", "pociag", "latarka", "metal", "braz", "ruda", "rog", "kolor", "plomien", "strzala", "wiatr", "czaszka", "uscisk", "oblok", "blysk", "dzwonek", "kwadrofonik", "troska", "fikcja", "skrzynia", "blad", "kwadrat", "przycisk", "szklanka", "kosmos", "koniec", "poczatek", "strona", "rytm", "rama", "nowy", "stary", "brama", "torba", "pierscionek", "obraz", "roszlina", "gwiazda", "kula", "poziom", "szczyt", "noga", "para", "swiadek", "rzeka", "kraina", "zwierze", "cien", "slon", "lampka", "kosz", "olowek", "wzor", "czasopismo", "okulary", "piers", "koktajl", "deska", "krewetka", "plot", "flaga", "slowo", "ksztalt", "roza", "punkt", "kubek", "droga", "sciezka", "lza", "piesek", "balon", "placz", "rekaw", "murowany", "szyna", "okap", "oddech", "mlot", "skrzydlo", "beben", "lawa", "sfera", "lza", "miara", "szept", "muzyka", "strach", "iluzja", "piasek", "struna", "kierunek", "cien", "wieza", "duch", "sen", "szansa", "chwila", "wizja", "granica", "brzeg", "krzyk", "promien", "kurz", "lustro", "ksztalt", "tlo", "korzen", "szczescie", "ton", "lisc", "rog", "zegar", "punkt", "przewod", "dach", "most", "rama", "skok", "gest", "prad", "wir", "lsnienie", "strzala", "napiecie", "ramka", "zwyciestwo", "stopa", "pierscien", "nieskonczonosc", "balans", "deszcz", "papier", "skarb", "tron", "strzal", "gra", "impuls", "fontanna", "plomien", "olowek", "snop", "kolo", "czas", "luk", "strzala", "mgla", "krajobraz", "pamiec", "harmonia", "sfera", "pajak", "roza", "kurz", "jaskolka", "uscisk", "pomost", "kropla", "lsnienie", "eksplozja", "kula", "kometa", "linia", "odbicie", "zbiornik", "maska", "oko", "odkrycie", "rekaw", "polaczenie", "punkt", "sciana", "skala", "luska", "wiatrak", "zegar", "krok", "lza", "lustro", "ruch", "skrzydlo", "slad", "laskotanie", "dreszcz", "luk", "gwiazda"]
zgadniete_litery=set()
bledy=0
maksymalne_bledy=15
ukrytehaslo=random.choice(haslo)

while bledy < maksymalne_bledy:
    
    ukryte_haslo = "".join(literka if literka in zgadniete_litery else "_" for literka in ukrytehaslo)

    print("\nHasło:", ukryte_haslo)
    print(f"Masz juz {bledy} bledy/ow z {maksymalne_bledy}")

    if ukryte_haslo == haslo:
        print("Wygrales")
        print(f"To jest twoja liczba zyc po zgadnieciu hasla {bledy}")
        break

    litera = input("Podaj literę: ").lower()

    if litera.isalpha() and len(litera) == 1:
        if litera in zgadniete_litery:
            print("Juz zgadywales ta litere ")
        elif litera in haslo:
            zgadniete_litery.add(litera)
            print("Ta litera jest w hasle")
        else:
            bledy += 1
            print("Nie ma tej litery w hasle")
    else:
        print("Masz wprowadzic tylko jedna litere panie kolego")

else:
    print(f"Nie udalo ci sie haslo to: {ukrytehaslo}")