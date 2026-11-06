broj_1 = float(input("Unesite broj_1:"))

broj_2 = float(input("Unesite broj_2:"))

print(broj_1, broj_2, type (broj_2))

operator = input("Unesite operator: ")

dozvoljeni_operatori = ["+", "-", "*", "/"]

if operator not in dozvoljeni_operatori:
    print("Nepodržani operator!")

if operator == "+":
    print(f"Rezultat operacije {broj_1} + {broj_2} je {broj_1 + broj_2}")

elif operator == "-":
    print(f"Rezultat operacije {broj_1} - {broj_2} je {broj_1 - broj_2}")

elif operator == "*":
    print(f"Rezultat operacije {broj_1} * {broj_2} je {broj_1 * broj_2}")

elif operator == "/":
    if broj_2 == 0:
        print("Dijeljenje s nulom nije dozvoljeno!")
    print(f"Rezultat operacije {broj_1} / {broj_2} je {broj_1 / broj_2}")

godina = int(input("Unesite godinu:"))

if (godina % 4 == 0 and godina % 100 != 0) or godina % 400 == 0:
    print(f"Godina {godina} je prijestupna!")
else:
    print(f"Godina {godina} nije prijestupna!")

tajni_broj = 47
broj_pokusaja = 0
broj_je_pogoden = False

while not broj_je_pogoden:
    broj = int(input("Pogodi broj: "))
    broj_pokusaja += 1
    if broj < tajni_broj:
        print("Premalen")
    elif broj > tajni_broj:
            print("Prevelik")
    else:
        print("Pogodak!")
        broj_je_pogoden = True



