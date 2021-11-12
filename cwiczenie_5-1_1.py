fn = ["Czesław", "Ludwik", "Piotr", "Augustyna", "Julitta"]
ln = ["Jasinski", "Borkowski", "Zajac", "Zawadzka", "Adamczyk"]
e_m = ["CzeslawJasinski@jourrapide.com", "LudwikBorkowski@dayrep.com", "PiotrZajac@teleworm.us", "AugustynaZawadzka@dayrep.com", "JulittaAdamczyk@dayrep.com"]

class Vcards:
    def __init__(self, first_name, last_name, e_mail):
        self.first_name, self.last_name, self.e_mail = first_name, last_name, e_mail
        
        print(f"Imię i nazwisko: {self.first_name} {self.last_name}, email: {self.e_mail}")

clients = [Vcards(first_name, last_name, e_mail) for first_name, last_name, e_mail in zip(fn, ln, e_m)]