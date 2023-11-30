print("Konwertowanie liczb dzieistnych na rzymskie")
print("Maksymalnie do 5000")


liczbyrzymskie={
    1:"I",
    5:"V",
    9:"IX",
    10:"X",
    40:"XL",
    50:"L",
    90:"XC",
    100:"C",
    400:"CD",
    500:"D",
    900:"CM",
    1000:"M"}
liczba_dziesietna=int(input("Podaj liczbe dziesietna do 5000 tysiecy "))
while liczba_dziesietna<1 or liczba_dziesietna>=5000:
    print("Podales liczbe z poza zakresu")
    liczba_dziesietna=int(input("Podaj liczbe jesczer raz "))

liczba_rzymska = ""

for symbol, wartosc in liczbyrzymskie.items():
    while liczba_dziesietna >= wartosc:
        liczba_rzymska += symbol
        liczba_dziesietna -= wartosc

print(f"Liczba dziesiętna {liczba_dziesietna} w systemie rzymskim to: {liczba_rzymska}")
