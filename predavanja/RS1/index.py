# broj_1 = float(input("Unesite broj_1:"))

# broj_2 = float(input("Unesite broj_2:"))

# print(broj_1, broj_2, type (broj_2))

# operator = input("Unesite operator: ")

# dozvoljeni_operatori = ["+", "-", "*", "/"]

# if operator not in dozvoljeni_operatori:
#     print("Nepodržani operator!")

# if operator == "+":
#     print(f"Rezultat operacije {broj_1} + {broj_2} je {broj_1 + broj_2}")

# elif operator == "-":
#     print(f"Rezultat operacije {broj_1} - {broj_2} je {broj_1 - broj_2}")

# elif operator == "*":
#     print(f"Rezultat operacije {broj_1} * {broj_2} je {broj_1 * broj_2}")

# elif operator == "/":
#     if broj_2 == 0:
#         print("Dijeljenje s nulom nije dozvoljeno!")
#     print(f"Rezultat operacije {broj_1} / {broj_2} je {broj_1 / broj_2}")

# godina = int(input("Unesite godinu:"))

# if (godina % 4 == 0 and godina % 100 != 0) or godina % 400 == 0:
#     print(f"Godina {godina} je prijestupna!")
# else:
#     print(f"Godina {godina} nije prijestupna!")

# tajni_broj = 47
# broj_pokusaja = 0
# broj_je_pogoden = False

# while not broj_je_pogoden:
#     broj = int(input("Pogodi broj: "))
#     broj_pokusaja += 1
#     if broj < tajni_broj:
#         print("Premalen")
#     elif broj > tajni_broj:
#             print("Prevelik")
#     else:
#         print("Pogodak!")
#         broj_je_pogoden = True


# lozinka = input("Unesite lozinku:")

# def provjera_lozinke(lozinka):
#     velika_slova = 0
#     brojevi = 0
#     if len(lozinka) < 8 or len(lozinka) > 15:
#         return "Lozinka mora sadržavati između 8 i 15 znakova"
#     for znak in lozinka:
#         if znak.isupper():
#             velika_slova += 1
#         if znak.isdigit():
#             brojevi += 1
#     if velika_slova == 0 or brojevi == 0:
#         return "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj"
#     if "password" in lozinka.lower() or "lozinka" in lozinka.lower():
#         return "Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'"
#     return "Lozinka je jaka!"

# provjera_lozinke(lozinka)

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def parni(lista):
#     lista_parnih = []
#     for broj in lista:
#         if broj % 2 == 0:
#             lista_parnih.append(broj)
#     return lista_parnih

# print(parni(lista))



# def deduplicirana_lista(lista):
#     ded = set(lista)
#     return ded


# print(deduplicirana_lista(lista))

# def grupiraj_po_paritetu(lista):
#     rjecnik = {"parni": [], "neparni": []}
#     for broj in lista:
#         if broj % 2 == 0:
#             rjecnik["parni"].append(broj)
#         else:
#             rjecnik["neparni"].append(broj)
#     return rjecnik

# print(grupiraj_po_paritetu(lista))

# rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

# def obrni_rjecnik(rjecnik):
#     novi_rjecnik = {}
#     for kljuc, vrijednost in rjecnik.items():
#         novi_rjecnik[vrijednost] = kljuc
#     return novi_rjecnik

# print(obrni_rjecnik(rjecnik))

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def prvi_i_zadnji(lista):
#     return (lista[0], lista[-1])

# print(prvi_i_zadnji(lista))

# lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

# def maks_i_min(lista):
#     manji = lista[0]
#     veci = lista[0]
#     for broj in lista:
#         if broj < manji:
#             manji = broj
#         if broj > veci:
#             veci = broj
#     return manji, veci

# print(maks_i_min(lista))

# skup_1 = {1, 2, 3, 4, 5}
# skup_2 = {4, 5, 6, 7, 8}

# def presjek(skup_1, skup_2):
#     skup_3 = skup_1.intersection(skup_2)
#     return skup_3

# print(presjek(skup_1, skup_2))

# def isPrime(broj):
#     if broj < 2:
#         return False
#     for djelitelj in range(2, broj):
#         if broj % djelitelj == 0:
#             return False
#     return True


# print(isPrime(7))   
# print(isPrime(10)) 

# def primes_in_range(start, end):
#     prosti = []
#     for broj in range(start, end + 1):
#         if broj < 2:
#             continue
#         je_prost = True
#         for djelitelj in range(2, broj):
#             if broj % djelitelj == 0:
#                 je_prost = False
#                 break
#         if je_prost:
#             prosti.append(broj)
#     return prosti


# print(primes_in_range(1, 10))

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

def count_vowels_consonants(tekst):
    rjecnik = {"vowels": 0, "consonants": 0}
    for slovo in tekst:
        if slovo in vowels:
            rjecnik["vowels"] += 1
        elif slovo in consonants:
            rjecnik["consonants"] += 1
    return rjecnik

print(count_vowels_consonants(tekst))