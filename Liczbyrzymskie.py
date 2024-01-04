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
liczba_dziesietna=int(input("Podaj liczbe dziesietna do 3999 "))
while liczba_dziesietna<1 or liczba_dziesietna>=3999:
    print("Podales liczbe z poza zakresu")
    liczba_dziesietna=int(input("Podaj liczbe raz jescze "))

liczba_rzymska = ""
for key in sorted(liczbyrzymskie.keys(), reverse=True):
    while liczba_dziesietna >= key:
        liczba_rzymska += liczbyrzymskie[key]
        liczba_dziesietna -= key

print(f"Liczba rzymska: {liczba_rzymska}")