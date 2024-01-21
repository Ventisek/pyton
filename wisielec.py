import random

haslo = ["skok", "piekny", "ksiezyc", "kot", "samolot", "drzewo", "woda", "latarnia", "ksiazka", "kwiat", "deszcz", "pies", "dom", "slonce", "dzwiek", "kawa", "trawa", "serce", "okno", "milosc", "czas", "tecza", "motyl", "chmura", "muzyka", "lampa", "fala", "snieg", "ocean", "ptak", "ryba", "marzenie", "cieplo", "zima", "lato", "podroz", "stacja", "noc", "dzien", "tajemnica", "zamek", "klucz", "radosc", "tlum", "gora", "las", "tkanina", "miasto", "historia", "szept", "smiech", "zloto", "klos", "kamien", "duma", "krew", "mleko", "kaktus", "most", "pustynia", "kurz", "pociag", "latarka", "metal", "braz", "ruda", "rog", "kolor", "plomien", "strzala", "wiatr", "czaszka", "uscisk", "oblok", "blysk", "dzwonek", "kwadrofonik", "troska", "fikcja", "skrzynia", "blad", "kwadrat", "przycisk", "szklanka", "kosmos", "koniec", "poczatek", "strona", "rytm", "rama", "nowy", "stary", "brama", "torba", "pierscionek", "obraz", "roszlina", "gwiazda", "kula", "poziom", "szczyt", "noga", "para", "swiadek", "rzeka", "kraina", "zwierze", "cien", "slon", "lampka", "kosz", "olowek", "wzor", "czasopismo", "okulary", "piers", "koktajl", "deska", "krewetka", "plot", "flaga", "slowo", "ksztalt", "roza", "punkt", "kubek", "droga", "sciezka", "lza", "piesek", "balon", "placz", "rekaw", "murowany", "szyna", "okap", "oddech", "mlot", "skrzydlo", "beben", "lawa", "sfera", "lza", "miara", "szept", "muzyka", "strach", "iluzja", "piasek", "struna", "kierunek", "cien", "wieza", "duch", "sen", "szansa", "chwila", "wizja", "granica", "brzeg", "krzyk", "promien", "kurz", "lustro", "ksztalt", "tlo", "korzen", "szczescie", "ton", "lisc", "rog", "zegar", "punkt", "przewod", "dach", "most", "rama", "skok", "gest", "prad", "wir", "lsnienie", "strzala", "napiecie", "ramka", "zwyciestwo", "stopa", "pierscien", "nieskonczonosc", "balans", "deszcz", "papier", "skarb", "tron", "strzal", "gra", "impuls", "fontanna", "plomien", "olowek", "snop", "kolo", "czas", "luk", "strzala", "mgla", "krajobraz", "pamiec", "harmonia", "sfera", "pajak", "roza", "kurz", "jaskolka", "uscisk", "pomost", "kropla", "lsnienie", "eksplozja", "kula", "kometa", "linia", "odbicie", "zbiornik", "maska", "oko", "odkrycie", "rekaw", "polaczenie", "punkt", "sciana", "skala", "luska", "wiatrak", "zegar", "krok", "lza", "lustro", "ruch", "skrzydlo", "slad", "laskotanie", "dreszcz", "luk", "gwiazda"]
zgadniete_litery = set()
bledy = 0
maksymalne_bledy = 8
ukryte_haslo = random.choice(haslo)
haslo_do_odgadniecia = list(ukryte_haslo)

while bledy < maksymalne_bledy:
    if set(haslo_do_odgadniecia) == zgadniete_litery:
        print("Wygrales!")
        print(f"To jest Twoja liczba zyc po odgadnieciu hasla: {bledy}")
        break

    print("\nHaslo:", ''.join([litera if litera in zgadniete_litery else '_' for litera in haslo_do_odgadniecia]))
    print(f"Masz juz {bledy} błędy/ow z {maksymalne_bledy}")

    litera = input("Podaj litere: ").lower()

    if litera.isalpha() and len(litera) == 1:
        if litera in zgadniete_litery:
            print("Juz zgadywałes ta litere.")
        elif litera in haslo_do_odgadniecia:
            zgadniete_litery.add(litera)
            print("Ta litera jest w hasle.")
        else:
            bledy += 1
            print("Nie ma tej litery w hasle.")
    else:
        print("Musisz wprowadzic tylko jedna litere")

else:
    print(f"Przegrales. Hasło to: {ukryte_haslo}")