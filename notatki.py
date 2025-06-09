import  itertools
import time
from functools import reduce
from itertools import cycle

import random
from itertools import cycle, islice


#zadanie 1
class KoloFortuny:
    def __init__(self, pola):
        self.pola = pola
        self._cykl = cycle(self.pola)
        self._offset = 0  # początkowy offset w cyklu

    def zakrec_kolem(self):
        przesuniecie = random.randint(5, 20)
        self._offset += przesuniecie
        print(self._offset)
        # Przesuwamy iterator o 'przesuniecie' pozycji od obecnej
        wynik = next(islice(cycle(self.pola), self._offset, self._offset + 1))
        print(f"Wypadło pole: {wynik}")
        return wynik

    def __str__(self):
        return ','.join(str(p) for p in self.pola)

    def __getitem__(self, index):
        if index < 1 or index > len(self.pola):
            raise IndexError("Numer pola poza zakresem.")
        return self.pola[index - 1]

print("== TWORZENIE KOŁA ==")
kolo = KoloFortuny(["100", "BANKRUT", "200", "400", "STOP"])

print("\n== TEST __str__ ==")
print(str(kolo))  # Powinno wypisać: 100,BANKRUT,200,400,STOP

print("\n== TEST __getitem__ ==")
print(f"Pole 1: {kolo[1]}")  # 100
print(f"Pole 3: {kolo[3]}")  # 200

try:
    print(kolo[0])  # powinien rzucić wyjątek
except IndexError as e:
    print(f"Błąd: {e}")

print("\n== TEST zakrec_kolem() ==")
for i in range(5):
    print(f"Obrót {i + 1}:")
    kolo.zakrec_kolem()

#zadanie 2
data = [-1.1, 0.4, 0.1, -0.7]
sorted_data = sorted(data, key=lambda x: abs(0 - x), reverse=True)
print(sorted_data)

#zadanie 3
from typing import List


def filter_sentences(sentences: List[str], min_words: int) -> List[str]:
    if not all(isinstance(s, str) for s in sentences):
        raise ValueError("Wszystkie elementy muszą być typu str.")
    return list(filter(lambda s: len(s.split()) >= min_words, sentences))


print(filter_sentences(["To jest test", "Krótko", "Dłuższe zdanie zawierające więcej słów"], 3))

#zadanie 4
data = [1, True, 0.0, 'LOL']
as_string = '|'.join(map(lambda x: str(type(x)), data))
print(as_string)

import numpy as np
from concurrent.futures import ProcessPoolExecutor


def oblicz_srednia_kolumny(kolumna):
    return np.mean(kolumna)

if __name__ == "__main__":
    def srednia_wieloprocesowa(arr: np.ndarray, liczba_procesow: int) -> float:
        with ProcessPoolExecutor(max_workers=liczba_procesow) as executor:
            srednie_kolumn = list(executor.map(oblicz_srednia_kolumny, arr))

        return sum(srednie_kolumn) / len(srednie_kolumn)


    arr = np.random.randint(low=1, high=1000, size=600_000).reshape((20, 30_000))
    wynik = srednia_wieloprocesowa(arr, 4)
    print(wynik)



class Stoper:
    def __init__(self):
        self.czas = 0.0
        self._start_time = None

    def start(self):
        if self._start_time is None:
            self._start_time = time.time()
        else:
            print("Stoper już działa")
    def stop(self):
        if self._start_time is not None:
            elapsed = time.time() - self._start_time
            self.czas += elapsed
            self._start_time = None
        else:
            print("Stoper nie zostal uruchomiony")

    def reset(self):
        self.czas = 0.0
        self._start_time = None

    def __str__(self):
        return f"Czas całkowity: {self.czas} sekundy"

# s = Stoper()
# s.start()
# time.sleep(1.5)
# s.stop()
# print(s)

words = ["pies", "kot", "anakonda", "słoń", "rybaaaaaa"]

sortedbya = sorted(words, key=lambda x: x.count('a'), reverse=True)

flt = [1.2, 102.2, 99.0, 100000.9, -37.7]

# print(sortedbya)
from typing import List, Tuple
def filter_negatives(floats: List[float]):
    if not all(isinstance(f, float) for f in floats):
        raise ValueError("to nie są floaty")
    return list(filter(lambda f: 0 <= f < 100, floats))

# print(filter_negatives(flt))

dane = [123, False, 3.14, "tekst", None]

as_string = '||'.join(map(lambda x: str(type(x)), dane))
# print(as_string)

words = ["kot", "encyklopedia", "Python", "procesor", "fortuna", "klasa", "rower"]

from concurrent.futures import ProcessPoolExecutor

def word_length(word):
    return len(word)

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(word_length, words))

    for word, length in zip(words, results):
        print(f"{word} -> {length}")


sentences = [
    "Ala ma kota",
    "Python jest super",
    "Sztuczna inteligencja",
    "Kot na dachu",
    "Uczenie maszynowe"
]

def count_vowels(sentence):
    return sum(1 for char in sentence if char.lower() in "aeiou")



if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(count_vowels, sentences))

    for sentence, length in zip(sentences, results):
        print(f"{sentence} -> {length}")


import numpy as np

arr = np.random.randint(0, 1000, size=(10000, 10))

def column_mean(column):
    return np.mean(column)

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(column_mean, arr.T))

    for column in results:
        print(column)

numbers = list(range(1, 10001))

def square(n):
    return n ** 2

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(square, numbers))

    b = list(filter(lambda x: x < 200 and x % 2 == 0, results))
    print(b)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))

    primes = [_ for _, is_p in zip(numbers, results) if is_p]


    print(primes[:20])

class Zwierze:
    def __init__(self):
        self.imie = 'Fafik'
        self.wiek = 5

    def przedstaw_sie(self):
        return f"Cześć, jestem pies {self.imie}, mam {self.wiek} lat"

class Pies(Zwierze):
    def __init__(self):
        super().__init__()
        self.rasa = "dalmatyńczyk"

    def przedstaw_sie(self):
        return f"Cześć, jestem pies {self.imie}, mam 5 lat i moja rasa to dalmatyńczyk"
#
#
# s = Zwierze()
# print(s.przedstaw_sie())
#
# s1 = Pies()
# print(s1.przedstaw_sie())

from abc import ABC, abstractmethod

class Pojazd(ABC):
    @abstractmethod
    def ruszaj(self):
        ...

class Rower(Pojazd):
    def ruszaj(self):
        print("Rower rusza")

class Samochod(Pojazd):
    def jedziem(self):
        return "Samochod rusza"

s = Samochod()
s.ruszaj()

class Waluta():
    def __init__(self, ilosc=0.0):
        self.ilosc = ilosc

    def __add__(self, other):
        if isinstance(other, Waluta):
            return Waluta(self.ilosc + other.ilosc)
        else:
            raise ValueError("Obiekt nie jest walutą")

    def __eq__(self, other):
        if isinstance(other, Waluta):
            return self.ilosc == other.ilosc
        else:
            raise ValueError("Obiekt nie jeste walutą")
#
#
# s1 = Waluta(4)
# s2 = Waluta(5)
# s3 = Waluta(9)
# s4 = s1 + s2
# print(s1)
# var = s4.__class__.__name__
# print(var)
# print(s3 == s4)

class Matematyka:
    @staticmethod
    def pierwiastek(x):
        return x ** 0.5

kolory = ["czerwony", "zielony", "niebieski"]

cycled_colors = itertools.cycle(kolory)

for _ in range(10):
    print(next(cycled_colors))

studenci = ["Ania", "Bartek", "Celina", "Daniel"]

studens_com = list(itertools.combinations(studenci, 2))

print(studens_com)

class Pojazd(ABC):
    def __init__(self):
        self.nazwa = None
        self.spalanie_na_100km = None
        self.koszt_na_km = None

    @abstractmethod
    def koszt_trasy(self, dlugosc_km: float) -> float:
        ...

class SamochodOsobowy(Pojazd):
    def __init__(self):
        super().__init__()
        self.nazwa = "Samochod osobowy"
        self.spalanie_na_100km = 100
        self.koszt_na_km = 10

    def koszt_trasy(self, dlugosc_km: float) -> float:
        return self.spalanie_na_100km * dlugosc_km / 100 * self.koszt_na_km

    def __str__(self):
        return f"Nazwa: {self.nazwa}, Spalanie na 100km: {self.spalanie_na_100km}, Koszt na km: {self.koszt_na_km}"

class Ciezarowka(Pojazd):
    def __init__(self):
        super().__init__()
        self.nazwa = "Ciezarowka"
        self.spalanie_na_100km = 150
        self.koszt_na_km = 15

    def koszt_trasy(self, dlugosc_km: float) -> float:
        return (self.spalanie_na_100km * dlugosc_km / 100 * self.koszt_na_km) + 50

    def __str__(self):
        return f"Nazwa: {self.nazwa}, Spalanie na 100km: {self.spalanie_na_100km}, Koszt na km: {self.koszt_na_km}"

class Autobus(Pojazd):
    def __init__(self, passengers=0):
        super().__init__()
        self.nazwa = "Autobus"
        self.spalanie_na_100km = 200
        self.koszt_na_km = 20
        self.passengers = passengers

    def koszt_trasy(self, dlugosc_km: float) -> float:
        return (self.spalanie_na_100km * dlugosc_km / 100 * self.koszt_na_km) + (self.passengers * 2)

    def __str__(self):
        return f"Nazwa: {self.nazwa}, Spalanie na 100km: {self.spalanie_na_100km}, Koszt na km: {self.koszt_na_km}, Liczna pasażerów: {self.passengers}"


s = SamochodOsobowy()
# print(s.koszt_trasy(100))
a = Autobus(40)
# print(w.koszt_trasy(100))

class Flota:
    def __init__(self, pojazdy: List[Pojazd] = None):
        self.pojazdy = pojazdy if pojazdy is not None else []

    def dodaj_pojazd(self, pojazd):
        if not isinstance(pojazd, Pojazd):
            raise TypeError("Tylko obiekty typu Pojazd można dodać")
        self.pojazdy.append(pojazd)

    def usun_pojazd(self, nazwa):
        for pojazd in self.pojazdy:
            if pojazd.nazwa == nazwa:
                self.pojazdy.remove(pojazd)
                break
        else:
            raise ValueError("Pojazd o takiej nazwie nie istnieje")

    def __add__(self, other):
        if isinstance(other, Flota):
            return Flota(self.pojazdy + other.pojazdy)
        else:
            raise ValueError("Obiekt nie jest flota")

    def __str__(self):
        return "\n".join(str(pojazd) for pojazd in self.pojazdy)

    def __getitem__(self, item):
        return self.pojazdy[item]


c = Ciezarowka()
s1 = SamochodOsobowy()
f1 = Flota([s, a])
f2 = Flota([c, s1])
flota_polaczona = f1 + f2
print(type(flota_polaczona))
print(flota_polaczona[0].koszt_trasy(200))


trasy = [120.0, 400.0, 60.0, 200.0]


def symuluj_trasy(flota: Flota, trasy: List[float]) -> List[Tuple[str, float, float]]:
    przypisania = zip(cycle(flota), trasy)
    print(list(przypisania))
    return list(map(lambda x: (x[0].nazwa, x[1], x[0].koszt_trasy(x[1])), przypisania))

print(symuluj_trasy(flota_polaczona, trasy))

def filtruj_drogie_trasy(lista_trasy: List[Tuple[str, float, float]], prog:float):
    return list(filter(lambda x: x[2] > prog, lista_trasy))

def kategoryzuj_trasy(lista_trasy: List[Tuple[str, float, float]]):
    return {
        'krótkie': [x for x in lista_trasy if x[1] < 100],
        'średnie': [x for x in lista_trasy if 100 <= x[1] <= 300],
        'długie': [x for x in lista_trasy if x[1] > 300]
    }

class RentowneTrasyIterator:
    def __init__(self, pojazd: Pojazd, dystanse: List[float], przychod_na_km: float = 2.0):
        self.pojazd = pojazd
        self.dystanse = dystanse
        self.przychod_na_km = przychod_na_km
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.dystanse):
            d = self.dystanse[self.index]
            self.index += 1
            koszt = self.pojazd.koszt_trasy(d)
            przychod = self.przychod_na_km * d
            if przychod > koszt:
                return (d, koszt, przychod)
        raise StopIteration


class KontoBankowe(ABC):
    def __init__(self, saldo=0):
        self._saldo = saldo

    def wplac(self, kwota):
        self._saldo += kwota

    def saldo(self):
        return self._saldo

    @abstractmethod
    def wyplac(self, kwota):
        ...

    @staticmethod
    def przelicz_walute(kwota, kurs=4.5):  # PLN → EUR domyślnie
        return round(kwota / kurs, 2)

    def __add__(self, other):
        if isinstance(other, KontoBankowe):
            return self._saldo + other._saldo
        return NotImplemented


class KontoOsobiste(KontoBankowe):
    LIMIT_DZIENNY = 1000

    def wyplac(self, kwota):
        if kwota <= self.LIMIT_DZIENNY and kwota <= self._saldo:
            self._saldo -= kwota
        else:
            print("Limit lub brak środków")


class KontoFirmowe(KontoBankowe):
    def wyplac(self, kwota):
        prowizja = kwota * 0.02
        suma = kwota + prowizja
        if suma <= self._saldo:
            self._saldo -= suma
        else:
            print("Brak środków")


# Przykład:
konto1 = KontoOsobiste(1500)
konto2 = KontoFirmowe(3000)

konto1.wyplac(900)
konto2.wyplac(1000)

print("Saldo konto1:", konto1.saldo())
print("Saldo konto2:", konto2.saldo())
print("Suma kont:", konto1 + konto2)
print("EUR z konta1:", KontoBankowe.przelicz_walute(konto1.saldo()))

from itertools import cycle, islice, combinations
import random

def generuj_harmonogram(dni_liczba):
    dni_tygodnia = ["pon", "wt", "sr", "czw", "pt"]
    zajecia = ["matma", "wf", "angielski", "fizyka"]

    dni = list(islice(cycle(dni_tygodnia), dni_liczba))
    kombinacje_zajec = list(combinations(zajecia, 2))

    harmonogram = {dz: random.choice(kombinacje_zajec) for dz in dni}
    return harmonogram

# Przykład:
harmonogram = generuj_harmonogram(10)
for dzien, zajecia in harmonogram.items():
    print(f"{dzien}: {zajecia}")

slowa = ["kot", "pies", "sowa", "anakonda", "bóbr", "słoń", "hipopotam"]

# Samogłoski:
samogloski = "aeiouyąęóAEIOUYĄĘÓ"

# Liczba samogłosek:
def licz_samogloski(s):
    return sum(1 for c in s if c in samogloski)

# Posortowane malejąco wg liczby samogłosek
posortowane = sorted(slowa, key=lambda x: licz_samogloski(x), reverse=True)

# Grupowanie długości słów
grupy = {
    dl: list(filter(lambda s: len(s) == dl, posortowane))
    for dl in set(map(len, slowa))
}

print("Posortowane:", posortowane)
print("Grupowanie po długości:", grupy)

class LiczbyPierwsze:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.stop:
            liczba = self.current
            self.current += 1
            if self.czy_pierwsza(liczba):
                return liczba
        raise StopIteration

    def czy_pierwsza(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

# Użycie:
for p in LiczbyPierwsze(10, 30):
    print("Pierwsza:", p)

def collatz(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    yield 1

# Użycie:
print("Ciąg Collatza od 13:")
print(list(collatz(13)))
