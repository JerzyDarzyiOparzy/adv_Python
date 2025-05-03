from datetime import datetime
import functools


# Zadanie 1 - dekorator logujący
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        czas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{czas}] Wywołano {func.__name__}")
        if args:
            print(f"Argumenty: {args}")
        if kwargs:
            print(f"Nazwane argumenty: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


# Zadanie 2 - dekorator sprawdzający uprawnienia
def require_permission(permission):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if not user.has_permission(permission):
                raise PermissionError(f"Brak uprawnień: {permission}")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator


# Zadanie 3 - dekorator singleton
def Singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


# Przykładowa klasa User do testów
class User:
    def __init__(self, permissions):
        self.permissions = permissions

    def has_permission(self, permission):
        return permission in self.permissions


# Testy
def test_zadania():
    # Test zadania 1
    print("\nTest zadania 1 - logger:")
    @log_call
    def testowa_funkcja(x, y=10):
        return x + y
    
    wynik = testowa_funkcja(5, y=20)
    print(f"Wynik: {wynik}")

    # Test zadania 2
    print("\nTest zadania 2 - uprawnienia:")
    @require_permission('admin')
    def usun_uzytkownika(user, user_id):
        print(f"Usunięto użytkownika {user_id}")

    admin = User(['admin'])
    zwykly_user = User(['user'])

    try:
        usun_uzytkownika(admin, 123)
        print("Test admin - OK")
    except PermissionError as e:
        print(f"Błąd: {e}")

    try:
        usun_uzytkownika(zwykly_user, 123)
    except PermissionError as e:
        print(f"Test zwykły user - OK, złapano błąd: {e}")

    # Test zadania 3
    print("\nTest zadania 3 - singleton:")
    @Singleton
    class Konfiguracja:
        def __init__(self, nazwa="domyślna"):
            self.nazwa = nazwa

    k1 = Konfiguracja("pierwsza")
    k2 = Konfiguracja("druga")

    print(f"k1.nazwa: {k1.nazwa}")
    print(f"k2.nazwa: {k2.nazwa}")
    print(f"Czy to ten sam obiekt: {k1 is k2}")


if __name__ == "__main__":
    test_zadania()