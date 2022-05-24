import re


biblioteka = {}
uzytkownicy = {}
class Czytelnik:
    def __init__(self, imie):
        self.imie = imie
        self.ksiazki_czytelnika = {}

class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.ilosc = 1

def dodaj_ksiazke(tytul, autor, rok_wydania):
    if tytul in biblioteka: 
        biblioteka[tytul].ilosc += 1
    else:
        biblioteka[tytul] = Ksiazka(tytul, autor, rok_wydania)
    return True


def wypozycz_ksiazke(imie, tytul):
    if imie in uzytkownicy:
        if sum(uzytkownicy[imie].ksiazki_czytelnika.values()) < 3 and (tytul not in  uzytkownicy[imie].ksiazki_czytelnika or uzytkownicy[imie].ksiazki_czytelnika[tytul] == 0) :
            if biblioteka[tytul].ilosc >=1:
                biblioteka[tytul].ilosc -= 1
                uzytkownicy[imie].ksiazki_czytelnika[tytul] = 1
                return True
            else:
                return False
        else:
            return False
    else:
        if biblioteka[tytul].ilosc >=1:
            uzytkownicy[imie] = Czytelnik(imie)
            biblioteka[tytul].ilosc -= 1
            uzytkownicy[imie].ksiazki_czytelnika[tytul] = 1
            return True 
        else:
            return False

def oddaj_ksiazke(imie, tytul):
    if bool(uzytkownicy):
        if uzytkownicy[imie].ksiazki_czytelnika[tytul] >0:
            biblioteka[tytul].ilosc += 1
            uzytkownicy[imie].ksiazki_czytelnika[tytul] = 0
            return True
        else:
            return False
    else:
        return False

def operacje(komenda, tytul, autor, rok_wydania = None):
    if komenda == 'dodaj':
        return dodaj_ksiazke(tytul, autor, rok_wydania)
        
    elif komenda == 'wypozycz':
        return wypozycz_ksiazke(imie=tytul, tytul=autor)
    
    elif komenda == 'oddaj':
        return oddaj_ksiazke(imie=tytul, tytul=autor)
    

    

if __name__ == "__main__":
    n = input()

    for i in range(int(n)):
        x = eval(input())
        if x[0].strip() == 'dodaj':
            print(operacje(x[0].strip(), x[1].strip(), x[2].strip(), x[3] ))
        else:
            print(operacje(x[0].strip(), x[1].strip(), x[2].strip()))





    
