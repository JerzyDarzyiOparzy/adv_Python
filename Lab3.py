from enum import Enum
import inspect
from abc import ABC, abstractmethod
from collections.abc import MutableSequence, Collection


# Listing 1

class Field:
    class FieldType(Enum):
        INTEGER = 1
        FLOAT = 2
        STRING = 3
        DATE = 4

    def __init__(self, field_type: FieldType):
        self.field_type = field_type
        self._value = None

    def get_fieldtype(self):
        return self.field_type

    def __str__(self):
        return self.field_type.__class__.__name__

    def _get_field_value(self):
        return self._value

    def _set_field_value(self, val):
        self._value = val

    def __get__(self, instance, owner):
        return self._get_field_value()

    def __set__(self, instance, value):
        self._set_field_value(value)


class Model:
    def __init__(self, db_table=None):
        if db_table is None:
            self.db_table = self.set_db_table(self.__class__.__name__)
        else:
            self.db_table = db_table

    def set_db_table(self, name: str):
        """ Metoda do ustawiania wartości db_table """
        return f'db_{name.lower()}'

    def get_fields(self):
        fields = {}
        for name, obj in inspect.getmembers(self):
            if isinstance(obj, Field):
                fields[name] = obj.get_fieldtype()
        return fields

    def __setattr__(self, attr, val):
        for name, obj in inspect.getmembers(self):
            if name == attr and isinstance(obj, Field):
                obj.value = val
                return
        super().__setattr__(attr, val)

    @staticmethod
    def generate_table_for_name(name: str):
        """ metoda statyczna wzracająca nazwę tabeli dla przykładowej nazwy modelu """
        return f'db_{name.lower()}'

    @classmethod
    def from_dict(cls, name: str, fields: dict):
        for field in fields.items():
            match field:
                case (str(), Field()):
                    setattr(cls, field[0], field[1])

        model = cls()
        model.db_table = f'db_{name.lower()}'
        return model


# Listing 2
class Field(ABC):
    class FieldType(Enum):
        INTEGER = 1
        FLOAT = 2
        STRING = 3
        DATE = 4

    def __init__(self):
        self._value = None

    def get_fieldtype(self):
        return self.__class__.__name__

    def __setattr__(self, attr, val):
        if attr == 'value':
            self._set_field_value(val)
        else:
            super().__setattr__(attr, val)

    @abstractmethod
    def _get_field_value(self):
        ...

    @abstractmethod
    def _set_field_value(self, val):
        ...

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return str(self._get_field_value())


class StringField(Field):
    def _set_field_value(self, val):
        if isinstance(val, str):
            self._value = val

    def _get_field_value(self):
        return self._value


# Implementacja IntegerField i DateField

class IntegerField(Field):
    def _set_field_value(self, val):
        if isinstance(val, int):
            self._value = val

    def _get_field_value(self):
        return self._value


class DateField(Field):
    def _set_field_value(self, val):
        if isinstance(val, str):
            self._value = val

    def _get_field_value(self):
        return self._value


# Model z metodą save
class ModelWithSave(Model):
    def save(self):
        fields = self.get_fields()
        values = [f"{name} = {getattr(self, name)}" for name in fields]
        values_str = ", ".join(values)

        if hasattr(self, "id") and self.id is not None:
            query = f"UPDATE {self.db_table} SET {values_str} WHERE id = {self.id}"
        else:
            query = f"INSERT INTO {self.db_table} ({', '.join(fields.keys())}) VALUES ({', '.join([str(v) for v in fields.values()])})"

        return query


# Testowanie
class Movie(ModelWithSave):
    title = StringField()
    director = StringField()
    release_date = DateField()


movie = Movie()
movie.title = "Transformers"
movie.director = "Michael Bay"
movie.release_date = "2007-06-12"

print(movie.save())  # Test zapytania SQL
print(movie.title)
print(movie.release_date)


# Klasa Koszyk dziedzicząca po MutableSequence
class Koszyk(MutableSequence):
    def __init__(self):
        self.items = []

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def insert(self, index, value):
        self.items.insert(index, value)

    def __len__(self):
        return len(self.items)


# Klasa Tydzien dziedzicząca po Collection
class Tydzien(Collection):
    def __init__(self):
        self.dni = [
            "Poniedziałek", "Wtorek", "Środa", "Czwartek",
            "Piątek", "Sobota", "Niedziela"
        ]

    def __len__(self):
        return len(self.dni)

    def __iter__(self):
        return iter(self.dni)

    def __contains__(self, item):
        return item in self.dni


# Testowanie Koszyk
koszyk = Koszyk()
koszyk.append("Jabłka")
koszyk.append("Banany")
koszyk.append("Pomarańcze")
print("Koszyk po dodaniu elementów:", koszyk.items)
koszyk[1] = "Gruszki"
print("Koszyk po modyfikacji:", koszyk.items)
del koszyk[0]
print("Koszyk po usunięciu elementu:", koszyk.items)

# Testowanie Tydzien
tydzien = Tydzien()
print("Dni tygodnia:", list(tydzien))  # Wyświetli dni tygodnia
print("Liczba dni w tygodniu:", len(tydzien))  # Powinno zwrócić 7

# Sprawdzanie zawartości
print("Czy 'Poniedziałek' jest w tygodniu?", "Poniedziałek" in tydzien)  # Powinno zwrócić True
print("Czy 'Niedziałek' jest w tygodniu?", "Niedziałek" in tydzien)  # Powinno zwrócić False


def test_model_db_table():
    model = Model()  # Model bez przekazywania db_table
    expected_db_table = 'db_model'

    assert model.db_table == expected_db_table, f"Nie udało się (test 1). Oczekiwano '{expected_db_table}', ale otrzymano '{model.db_table}'."
    print("Test 1: Domyślny db_table ustawiony poprawnie!")

    custom_model = Model(db_table='custom_table')  # Model z własnym db_table

    assert custom_model.db_table == 'custom_table', f"Nie udało się (test 2). Oczekiwano 'custom_table', ale otrzymano '{custom_model.db_table}'."
    print("Test 2: Własny db_table ustawiony poprawnie!")


# Uruchamiamy testy
test_model_db_table()

