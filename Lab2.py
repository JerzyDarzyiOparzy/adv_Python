import csv
from collections import namedtuple
from dataclasses import make_dataclass


def zadanie_1():
    with open("zamowienia.csv", encoding="utf8") as f:
        reader = csv.reader(f, delimiter=';')
        headers = next(reader)
        fields = [h.lower().replace(' ', '_') for h in headers]
        Order = namedtuple('Order', fields)
        orders = [Order._make(row) for row in reader]

    for order in orders[:10]:
        print(order)


def zadanie_2():
    Point = namedtuple('Point', ['x', 'y'], defaults=[0, 0])
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    p3 = Point(1, 2)

    print("Porównania:")
    print("p1 == p2:", p1 == p2)
    print("p1 == p3:", p1 == p3)
    print("p1 < p2:", p1 < p2)
    print("p1 > p2:", p1 > p2)
    print("p1 <= p3:", p1 <= p3)
    print("p1 >= p3:", p1 >= p3)

    print("\nOperacje arytmetyczne:")
    try:
        print("Dodawanie:", p1 + p2)
    except TypeError as e:
        print("Błąd dodawania:", e)

    try:
        print("Mnożenie:", p1 * 2)
    except TypeError as e:
        print("Błąd mnożenia:", e)


def zadanie_3(slownik):
    klasy = {}

    for key, val in slownik.items():
        class_name = val['class_name']
        props = [(prop[0], eval(prop[1])) if len(prop) == 2 else (prop[0], eval(prop[1]), eval(prop[2])) for prop in
                 val['props']]
        klass = make_dataclass(class_name, props)
        klasy[class_name] = klass

    return klasy


# Testy
dane = {
    1: {'class_name': 'Osoba', 'props': [('name', 'str'), ('is_admin', 'bool', 'False')]},
    2: {'class_name': 'Produkt', 'props': [('name', 'str'), ('price', 'float', '0.0'), ('quantity', 'float', '0.0')]}
}


def main():
    print("Zadanie 1:")
    zadanie_1()
    print("\nZadanie 2:")
    zadanie_2()
    print("\nZadanie 3:")
    klasy = zadanie_3(dane)
    osoba = klasy['Osoba']('Jan', True)
    produkt = klasy['Produkt']('Laptop', 3999.99, 5)
    print(osoba)
    print(produkt)


if __name__ == "__main__":
    main()
