import random
while True:
    print("Gra w papier kamien nozyce z komputerem")
    print("Do wyboru: 1-papier 2-kamien 3-nozyce")
    wybor=int(input("Wybierz co chcesz zrobic "))
    los=random.randint(1,3)
    if wybor==1 and los==1:
        print("A wiec wybrales papier")
        print("Natomiast komputer tez wybral papier")
        print("W rezultacie jest remis")
    elif wybor==1 and los==2:
        print("A wiec wybrales papier")
        print("Natomiast kompter wybral kamien")
        print("Wiec w rezultacie wygrales")
    elif wybor==1 and los==3:
        print("A wiec wybrales papier")
        print("Natomiast komputer wybral nozyce")
        print("W rezultacie przegrales z komputerem (troche slabo)")
    elif wybor==2 and los==1:
        print("A wiec wybrales kamien")
        print("Natomiast komputer wybral papier")
        print("Wiec w rezultacie przegrales z komputerem (troche slabo)")
    elif wybor==2 and los==2:
        print("A wiec wybrales kamien")
        print("Natomiast komputer tez wybral kamien")
        print("W rezultacie jest remis")
    elif wybor==2 and los==3:
        print("A wiec wybrales kamien")
        print("Natomiast komputer wybral nozyce")
        print("Wiec w rezultacie wygrales")
    elif wybor==3 and los==1:
        print("A wiec wybrales nozyce") 
        print("Natomiast komputer wybral papier")
        print("Wiec w rezultacie wygrales")
    elif wybor==3 and los==2:
        print("A wiec wybrales nozyce")
        print("Natomaist komputer wybral kamien")
        print("W rezultacie przegrales z komputerem (troche slabo)")
    elif wybor==3 and los==3:
        print("A wiec wybrales nozyce")
        print("Natomaist komputer wybral nozyce")
        print("Wiec w rezultacie jest remis")
    else:
        print("Nie wybrales zadnej z powyzszych opcji kolezko")
    ponownie = input("Czy chcesz powtórzyć gre? (tak/nie): ")
    if ponownie.lower() != 'tak':
        break

    



