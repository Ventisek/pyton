print("KALKULATOR")
print("1-dodawanie 2-odejmowanie 3-mnozenie 4-dzielenie 5-potegowanie 6-dzielenie modulo")
a=float(input("podaj liczbe a "))
b=float(input("podaj liczbe b "))
dzialanie=int(input("a teraz podaj dzialanie "))
if dzialanie==1:
    print(a+b)
if dzialanie==2:

    print(a-b)

if dzialanie==3:
    print(a*b)
elif b==0 and dzialanie==4:
    print("nie mozna dzielic przez zero")
elif dzialanie==4:
    print(a/b)
elif dzialanie==5:
    print(a**b)
elif dzialanie==6 and b==0:
    print("nie mozna dzielic przez 0")
elif dzialanie==6:
     print(a%b)
else: 
    print("nie ma takiego dzialania")
    


    


