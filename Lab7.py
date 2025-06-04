# Zadanie 1
# Wykorzystując funkcję reduce napisz funkcję anonimową, która będzie zliczała ilość samogłosek w podanym jej jako argument tekście.
from functools import reduce
from operator import add, mul

# Lambda do zliczania samogłosek
count_vowels = lambda text: reduce(lambda count, char: count + 1 if char.lower() in 'aeiouy' else count, text, 0)

# Test funkcji
text = "Abracadabra to czary i magia"
print("Zadanie 1:")
print(f"Liczba samogłosek w tekście '{text}': {count_vowels(text)}")

# Zadanie 2
# Wykorzystując funckję sorted oraz lambdę posortuj krotki po wartości punktowej
data = [('Adam', 'Nowak', '13 pkt'), ('Anna','Górka', '15 pkt'), ('Wojtek', 'Bonk', '8 pkt')]

# Sortowanie po punktach
sorted_data = sorted(data, key=lambda x: int(x[2].split()[0]))
print("\nZadanie 2:")
print("Posortowane dane po punktach (rosnąco):", sorted_data)

# Zadanie 3
# Wykorzystując lambdę, funkcję reduce oraz operator mul oblicz iloczyn pierwszych 10 liczb ciągu Fibonacciego
# Generowanie ciągu Fibonacciego
fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [1, 1])

# Obliczanie iloczynu pierwszych 10 liczb Fibonacciego
fib_10 = fib_series(10)
fib_product = reduce(mul, fib_10)
print("\nZadanie 3:")
print(f"Pierwsze 10 liczb ciągu Fibonacciego: {fib_10}")
print(f"Iloczyn pierwszych 10 liczb ciągu Fibonacciego: {fib_product}")

# Zadanie 4
# Napisz funkcję, która wykorzysta wbudowaną funkcję itertools.cycle do zwracania dnia tygodnia za n dni
import itertools

def jaki_dzien(aktualny_dzien, n_dni):
    dni_tygodnia = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']

    # Znajdź indeks aktualnego dnia
    try:
        indeks = dni_tygodnia.index(aktualny_dzien.lower())
    except ValueError:
        return "Nieprawidłowa nazwa dnia tygodnia"

    # Utwórz cykl dni tygodnia
    cycle = itertools.cycle(dni_tygodnia)

    # Przejdź do aktualnego dnia
    for _ in range(indeks):
        next(cycle)

    next(cycle) #nie liczymy dnia w którym jesteśmy obecnie

    for _ in range(n_dni):
        dzien = next(cycle)

    return dzien

print("\nZadanie 4:")
print(f"Dzień tygodnia za 3 dni od wtorku: {jaki_dzien('wtorek', 3)}")
print(f"Dzień tygodnia za 10 dni od piątku: {jaki_dzien('piątek', 10)}")

# Zadanie 5
# Wykorzystaj funkcję itertools.permutations dla ciągu 'ABCD' i r=2, a następnie utwórz funkcję lambda, która zwróci te wartości jako łańcuchy znaków
perms = list(itertools.permutations('ABCD', 2))
perm_strings = list(map(lambda x: ''.join(x), perms))

print("\nZadanie 5:")
print(f"Permutacje 'ABCD' dla r=2 jako krotki: {perms}")
print(f"Permutacje 'ABCD' dla r=2 jako łańcuchy znaków: {perm_strings}")

# Zadanie 6
# Wykorzystując funkjce z modułu itertools związane z kombinatoryką rozwiąż zadanie z rozmienianiem banknotu 100 zł
# Mamy: 4 banknoty po 20 zł, 3 banknoty po 10 zł, 2 banknoty po 50 zł oraz 2 monety po 5 zł

def licz_kombinacje_rozmienienia():
    # Dostępne nominały i ich ilości
    nominaly = {20: 4, 10: 3, 50: 2, 5: 2}

    # Generowanie wszystkich możliwych kombinacji użycia nominałów
    kombinacje = []

    # Dla każdego nominału generujemy możliwą liczbę użyć (od 0 do maksymalnej ilości)
    for n20 in range(nominaly[20] + 1):
        for n10 in range(nominaly[10] + 1):
            for n50 in range(nominaly[50] + 1):
                for n5 in range(nominaly[5] + 1):
                    suma = n20 * 20 + n10 * 10 + n50 * 50 + n5 * 5
                    if suma == 100:
                        kombinacje.append((n20, n10, n50, n5))

    return kombinacje

kombinacje = licz_kombinacje_rozmienienia()
print("\nZadanie 6:")
print(f"Liczba możliwych kombinacji rozmienienia banknotu 100 zł: {len(kombinacje)}")
print("Przykładowe kombinacje:")
for i, komb in enumerate(kombinacje[:5], 1):
    print(f"{i}. {komb[0]} x 20zł + {komb[1]} x 10zł + {komb[2]} x 50zł + {komb[3]} x 5zł")
if len(kombinacje) > 5:
    print("...")

# Zadanie 7
# Wykorzystaj funkcję starmap do wywołania funkcji wbudowanej format() i przygotuj listę argumentów [wartość, format]
wartosci = [
    [3.14159, ".2f"],
    [42, "d"],
    ["Python", "s"],
    [255, "X"],
    [0.5, ".1%"]
]

# Używamy starmap do formatowania wartości
sformatowane = list(itertools.starmap(lambda val, fmt: format(val, fmt), wartosci))

print("\nZadanie 7:")
print("Wartości przed formatowaniem:", [v[0] for v in wartosci])
print("Formaty:", [v[1] for v in wartosci])
print("Sformatowane wartości:", sformatowane)
