import math 

print("Obliczanie Pol Figur i ich Obwodow")
print("                     ")
print("to sa mozliwe figury z ktorych mozesz obliczyc pole i obwod lub samo pole jesli obwod jest niemozliwy lub ciezki do obliczenia:")
print("1-Kwadrat 2-Prostokat 3-Trojkat 4-Okrag 5-Rab")

figura=int(input("W takim razie podaj liczbe odpowiadajaca figurze ktorej chcesz obliczyc pole i obwod :"))
if figura==1:
    print("W takim razie obliczasz pole i obwod kwadratu")
    a=float(input("Podaj Bok kwadratu: "))
    while a<=0:
        print("Nie ma takiego boku podaj go jescze raz: ")
        a=float(input("Podaj liczbe a: "))
    print("a oto obwod kwadratu: ")
    print(4*a)
    print("A oto pole kwadratu")
    print(a*a)
elif figura==2:
    print("W takim razie obliczasz pole i obwod prostokata")
    a=float(input("Podaj liczbe a: "))
    while a<=0:
        print("Nie ma takiego boku podaj go jescze raz: ")
        a=float(input("Podaj liczbe a: "))
    b=float(input("A teraz podaj liczbe b: "))
    while b<=0:
        print("Nie ma takiego boku podaj go jescze raz: ")
        b=float(input("Podaj liczbe b: "))
    print("A oto obwod prostokata")
    print(2*a+2*b)
    print("a oto pole prostokata")
    print(a*b)
elif figura==3:
    wybor=int(input("Wybierz pole jakiego trojkata chcesz obliczyc 1-rownoboczny 2-zwykly: "))
    if wybor==1:
        a=float(input("Podaj podstawe trojkata: "))
        while a<=0:
           print("Nie ma takiego boku podaj go jescze raz: ")
           a=float(input("Podaj Podstawe: "))
        print("To jest pole trojkata rownobocznego: ")
        print(((a*a)*math.sqrt(3))/4)
    elif wybor==2:
        a=float(input("Podaj podstawe trojkata: "))
        while a<=0:
           print("Nie ma takiego boku podaj go jescze raz: ")
           a=float(input("Podaj liczbe a: "))
        h=float(input("Podaj wysokosc trojkata: "))
        while h<=0:
           print("Nie ma takiego boku podaj go jescze raz: ")
           h=float(input("Podaj wysokosc: "))
        print("To jest pole trojkata: ")
        print((a*h)/2)
    else:
        print("Nie podalem innego trojkata jaki mozesz obliczyc gluptasku")
elif figura==4:
    print("W takim razie obliczasz pole i obwod okragu: ")
    r=float(input("Podaj cieciwe okregu: "))
    while r<=0:
        print("Nie ma takiej cieciwy: ")
        r=float(input("Podaj cieciwe okregu: "))
    print("obwod kola wynosi:")
    print(2*(math.pi)*r)
    print("A pole okregu wynosi: ")
    print(math.pi*(r*r))
elif figura==5:
    print("Obliczasz pole rombu: ")
    wybor=int(input("z Jakich danych chcesz obliczyc pole 1-przekatynych 2-wysokosci i podstawy: "))
    if wybor==1:
        e=float(input("Podaj Pierwsza przekatna: "))
        while e<=0:
           print("Nie ma takiej przekatnej: ")
           e=float(input("Podaj pierwsza przekatna: "))
        f=float(input("Podaj druga przekatna: "))
        while f<=0:
           print("Nie ma takiej przekatnej: ")
           f=float(input("Podaj druga przekatna: "))
        print("to jest pole rombu z przekatynych")
        print((e*f)/2)
    elif wybor==2:
        a=float(input("Podaj podstawe: "))
        while a<=0:
           print("Nie ma takiego boku podaj go jescze raz: ")
           a=float(input("Podaj podstawe: "))
        h=float(input("Podaj wysoksoc: "))
        while a<=0:
           print("Nie ma takiego boku podaj go jescze raz: ")
           h=float(input("Podaj wysokosc: "))
        print("to jest pole rombu z wysokosci i podstawy")
        print(a*h)
else:
    print("Nie ma takiej figury w spisie kolezkoo")

    
    




        
    
    

    
    