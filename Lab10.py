from array import array
from timeit import timeit

# Setup
setup_i = "from array import array; arr = array('i', range(10000))"
setup_list_i = "lst = list(range(10000))"
setup_w = "from array import array; arr = array('u', 'a'*10000)"
setup_list_w = "lst = ['a']*10000"

# Czas inicjalizacji
init_array_i = timeit("array('i', range(10000))", setup="from array import array", number=1000)
init_list_i = timeit("list(range(10000))", number=1000)

init_array_w = timeit("array('u', 'a'*10000)", setup="from array import array", number=1000)
init_list_w = timeit("['a']*10000", number=1000)

# Czas dostępu
access_array_i = timeit("arr[5000]", setup=setup_i, number=1_000_000)
access_list_i = timeit("lst[5000]", setup=setup_list_i, number=1_000_000)

# Insert (dla array tylko na końcu, bo insert na środku może być powolny)
insert_array = timeit("arr.insert(0, 123)", setup=setup_i, number=1000)
insert_list = timeit("lst.insert(0, 123)", setup=setup_list_i, number=1000)

print(f"Inicjalizacja array('i'): {init_array_i:.6f}s")
print(f"Inicjalizacja list(int): {init_list_i:.6f}s")
print(f"Inicjalizacja array('u'): {init_array_w:.6f}s")
print(f"Inicjalizacja list(str): {init_list_w:.6f}s")

print(f"Dostęp array('i'): {access_array_i:.6f}s")
print(f"Dostęp list(int): {access_list_i:.6f}s")

print(f"Insert array('i'): {insert_array:.6f}s")
print(f"Insert list(int): {insert_list:.6f}s")

from array import array
import random
import datetime

# Array
arr = array('f', [random.random() for _ in range(1_000_000)])
start = datetime.datetime.now()
with open("array_file.bin", "wb") as f:
    arr.tofile(f)
with open("array_file.bin", "rb") as f:
    loaded_arr = array('f')
    loaded_arr.fromfile(f, 1_000_000)
end = datetime.datetime.now()
array_time = end - start

# List
lst = [random.random() for _ in range(1_000_000)]
start = datetime.datetime.now()
with open("list_file.txt", "w") as f:
    f.writelines('\n'.join(map(str, lst)))
with open("list_file.txt", "r") as f:
    loaded_list = [float(x.strip()) for x in f.readlines()]
end = datetime.datetime.now()
list_time = end - start

print(f"Czas zapisu i odczytu tablicy: {array_time}")
print(f"Czas zapisu i odczytu listy:   {list_time}")

import datetime
from dateutil.relativedelta import relativedelta

def wiek_info(data_urodzenia: str):
    urodziny = datetime.datetime.strptime(data_urodzenia, "%Y-%m-%d").date()
    dzisiaj = datetime.date.today()

    wiek = relativedelta(dzisiaj, urodziny)
    dni_zycia = (dzisiaj - urodziny).days

    # Najbliższe urodziny
    najblizsze = datetime.date(dzisiaj.year, urodziny.month, urodziny.day)
    if najblizsze < dzisiaj:
        najblizsze = datetime.date(dzisiaj.year + 1, urodziny.month, urodziny.day)

    do_urodzin = relativedelta(najblizsze, dzisiaj)
    od_poprzednich = relativedelta(dzisiaj, najblizsze - relativedelta(years=1))

    print(f"Witaj! Na dzień dzisiejszy masz {wiek.years} lat, {wiek.months} miesięcy oraz {wiek.days} dni.")
    print(f"Razem daje to imponujące {dni_zycia} dni!")
    print(f"Twoje najbliższe urodziny będą miały miejsce w dniu {najblizsze} czyli za {do_urodzin.months} miesięcy oraz {do_urodzin.days} dni.")
    print(f"Od poprzednich urodzin minęło {od_poprzednich.months} miesięcy i {od_poprzednich.days} dni.")

# Przykład
wiek_info("1990-12-12")

import csv
import datetime

daty = []

with open("zamowienia.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        data = row["Data zamowienia"]
        try:
            parsed = datetime.datetime.strptime(data, "%Y-%m-%d").date()
            daty.append(parsed)
        except ValueError:
            continue

najstarsza = min(daty)
najnowsza = max(daty)
roznica = (najnowsza - najstarsza).days

print(f"Najstarsza data: {najstarsza}")
print(f"Najnowsza data: {najnowsza}")
print(f"Różnica dni: {roznica}")