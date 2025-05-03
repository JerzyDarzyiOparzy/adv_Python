# Zadanie 1
names = ['marek', 'Damian', 'wojtas', 'maczuga333']
print("Długości imion:", list(map(lambda x: len(x), names)))

# Zadanie 2
mypow = lambda x: x ** 2
print("Kwadrat liczby 5:", mypow(5))
num = 5
print("Kwadrat liczby 5 (wywołanie bezpośrednie):", (lambda x: x ** 2)(num))

# Zadanie 3
print("Suma 2 i 3:", (lambda x, y: x + y)(2, 3))

# Zadanie 4
data = 'Marek ma 34 lata i 182 cm wzrostu.'.split()
numbers = list(filter(lambda x: x.isdigit(), data))
print("Znalezione liczby:", numbers)

# Zadanie 5
from functools import reduce
from operator import add

# Połączenie filter, map i reduce
suma_liczb = reduce(lambda x, y: x + y, map(int, filter(lambda x: x.isdigit(), data)))
print("Suma znalezionych liczb:", suma_liczb)

# z użyciem operatora add
suma_liczb_2 = reduce(add, map(int, filter(lambda x: x.isdigit(), data)))
print("Suma znalezionych liczb (z operator.add):", suma_liczb_2)

# Zadanie 6 - funkcja power
def power(n):
    return lambda a: a ** n

square = power(2)
cube = power(3)
print("Liczba 2 do kwadratu:", square(2))
print("Liczba 5 do sześcianu:", cube(5))

# Zadanie 7
data_text = 'Abracadabra to czary i magia.'
words = data_text.split()

print("Sortowanie po długości (malejąco):", 
      sorted(words, key=lambda x: len(x), reverse=True))

print("Sortowanie po liczbie liter 'i' (malejąco):", 
      sorted(words, key=lambda x: x.count('i'), reverse=True))

# Zadanie 8 - Ciąg Fibonacciego
fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
print("Ciąg Fibonacciego dla n=6:", fib_series(6))

# Zadanie 9 - itertools
import itertools

# count
print("\nPrzykład count:")
counter = itertools.count(2)
for _ in range(3):
    print(next(counter))

# cycle
print("\nPrzykład cycle:")
dni_tygodnia = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
day_cycle = itertools.cycle(dni_tygodnia)
print("Pierwsze trzy dni z cyklu:")
for _ in range(3):
    print(next(day_cycle))

# accumulate
print("\nPrzykład accumulate:")
numbers = range(1, 6)
print("Akumulacja przez dodawanie:", list(itertools.accumulate(numbers)))
print("Akumulacja przez mnożenie:", list(itertools.accumulate(numbers, lambda x, y: x * y)))

# batched
print("\nPrzykład batched:")
nums = list(range(1, 13))
print("Grupy po 3 elementy:")
for batch in itertools.islice(nums, 3):
    print(batch)