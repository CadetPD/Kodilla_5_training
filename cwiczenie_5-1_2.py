
from faker import Faker
fake = Faker('pl_PL')
#Ver. 1
class Vcards:
    def __init__(self, first_name, last_name, e_mail):
        self.first_name, self.last_name, self.e_mail = first_name, last_name, e_mail

    def __str__(self):
        return (f"Imię i nazwisko: {self.first_name} {self.last_name}, e-mail: {self.e_mail}")

def card(num):
    for i in range(num):
        cards = Vcards(first_name = fake.first_name(), last_name = fake.last_name(), e_mail = fake.email())
        print(cards)
card(5)

print("\nInterline\n")
#Ver.2
class Vcards:
    def __init__(self, first_name, last_name, e_mail):
        self.first_name, self.last_name, self.e_mail = first_name, last_name, e_mail

        #Czy wprowadzanie akcji do konstruktora (mimo, że kod działa prawidłowo) jest właściwe z punktu puryzmu pythona?
        #Bo takie rozwiązanie zastosowałem w cwiczenie_5-1_1.py w repo
        print(f"Imię i nazwisko: {self.first_name} {self.last_name}, e-mail: {self.e_mail}")

def card(num):
    for i in range(num):
        cards = Vcards(first_name = fake.first_name(), last_name = fake.last_name(), e_mail = fake.email())
card(2)

print("\nInterline\n")
#Ver. 3
class Vcards:
    def __init__(self, first_name, last_name, e_mail):
        self.first_name, self.last_name, self.e_mail = first_name, last_name, e_mail

    def __str__(self):
        return (f"Imię i nazwisko: {self.first_name} {self.last_name}, e-mail: {self.e_mail}")

#Dlaczego func zwraca tylko zdefiniowaną instancję, skoro taki zapis jest chyba tożsamy z zapisem pętli z Ver. 1? 
#Zaciąganie z listy po takiej iteracji dało prawidłowy wynik dla cwiczenie_5-1_1.py (w repo)
def card(num):
    cards = [Vcards(first_name = fake.first_name(), last_name = fake.last_name(), e_mail = fake.email()) for i in range(num)]
    print(cards)
card(6)
