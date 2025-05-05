import string
import itertools
import re


class EvenIndexIterator:
    """Iterator zwracający elementy z parzystych indeksów przekazanej sekwencji"""
    
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 2
        return value

# Test zadania 1
print("Test zadania 1:")
data = [1, 2, 3, 4, 5, 6]
even_iter = EvenIndexIterator(data)
print([x for x in even_iter])


class PrimeIterator:
    """Iterator generujący kolejne liczby pierwsze"""

    def __init__(self, limit):
        self.limit = limit
        self.current = 2

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.limit:
            if self.is_prime(self.current):
                prime = self.current
                self.current += 1
                return prime
            self.current += 1
        raise StopIteration


# Test zadania 2
print("\nTest zadania 2:")
prime_iter = PrimeIterator(20)
print([x for x in prime_iter])

class WeekDayIterator:
    """Iterator zwracający nazwy dni tygodnia w języku polskim"""

    def __init__(self, start_idx=0):
        self.days = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
        self.current = start_idx % len(self.days)

    def __iter__(self):
        return self

    def __next__(self):
        day = self.days[self.current]
        self.current = (self.current + 1) % len(self.days)
        return day


# Test zadania 3
print("\nTest zadania 3:")
day_iter = WeekDayIterator(2)
for _ in range(10):
    print(next(day_iter))


class WordIterator:
    """Iterator zwracający kolejne słowa z tekstu"""

    def __init__(self, text):
        self.words = re.findall(r'\b\w+\b', text)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return word


def word_generator(text):
    """Generator zwracający kolejne słowa z tekstu"""
    for word in re.finditer(r'\b\w+\b', text):
        yield word.group()


# Test zadania 4 i 5
print("\nTest zadania 4 i 5:")
text = "Kocham Pyton!!! Jak kocha to wróci."

print("Iterator słów:")
word_iter = WordIterator(text)
print([word for word in word_iter])

print("\nGenerator słów:")
print([word for word in word_generator(text)])


def product_code_generator(letter_pos, num_pos):
    """
    Generator kodów produktów wykorzystujący itertools.product

    Args:
        letter_pos (int): Liczba pozycji na litery (1 lub 2)
        num_pos (int): Liczba pozycji na cyfry

    Yields:
        str: Kolejny kod produktu
    """
    letters = list(itertools.product(string.ascii_uppercase, repeat=letter_pos))
    numbers = range(1, 10 ** num_pos)

    num_format = f"{{:0{num_pos}d}}"

    for letter_combo in letters:
        # Łączenie liter w jeden string
        letter_part = ''.join(letter_combo)
        for num in numbers:
            # Formatowanie części numerycznej i złączenie z literami
            yield f"{letter_part}_{num_format.format(num)}"


# Testy
print("Test generator kodów produktów:")
print("\nPrzykład dla letter_pos=1, num_pos=2:")
gen1 = product_code_generator(1, 2)
for _ in range(5):
    print(next(gen1))

print("\nPrzykład dla letter_pos=2, num_pos=3:")
gen2 = product_code_generator(2, 3)
for _ in range(5):
    print(next(gen2))

