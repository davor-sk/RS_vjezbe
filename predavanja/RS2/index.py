import datetime as d

# class Automobil:
#     def __init__(self, marka, model, godina_proizvodnje, kilometraza):
#         self.marka = marka
#         self.model = model
#         self.godina_proizvodnje = godina_proizvodnje
#         self.kilometraza = kilometraza

#     def ispisi(self):
#         print(f"Marka automobila je {self.marka}, model je {self.model}, automobil je proizveden {self.godina_proizvodnje} godine i prešao je {self.kilometraza} kilometara.")

#     def starost(self):
#         star = d.datetime.now().year - self.godina_proizvodnje
#         print(f"Automobil je star {star} godina!")

# auto = Automobil("Mazda", 3, 2011, 130000)

# auto.ispisi()
# auto.starost()

# class Kalkulator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def zbroj(self):
#         return self.a + self.b

#     def oduzimanje(self):
#         return self.a - self.b

#     def mnozenje(self):
#         return self.a * self.b

#     def dijeljenje(self):
#         return self.a / self.b

#     def potenciranje(self):
#         return self.a ** self.b

#     def korijen(self):
#         return self.a ** (1 / self.b)

# kalk = Kalkulator(10, 5)

# print(kalk.zbroj())
# print(kalk.oduzimanje())
# print(kalk.mnozenje())
# print(kalk.dijeljenje())
# print(kalk.potenciranje())
# print(kalk.korijen())

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def __repr__(self):
        return f"{self.ime} {self.prezime}, {self.godine} godina, ocjene: {self.ocjene}"

    def prosjek(self):
        prosjecne_ocjene = 0
        for o in self.ocjene:
            prosjecne_ocjene += o
        return prosjecne_ocjene / len(self.ocjene)
        

studenti = [
            {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
            {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
            {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
            {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
            {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
            {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]


studenti_objekti = [Student(s["ime"], s["prezime"], s["godine"], s["ocjene"]) for s in studenti]


print(studenti_objekti[5].prosjek())

najbolji_student = max(studenti_objekti, key = lambda s: s.prosjek())

print(najbolji_student)

