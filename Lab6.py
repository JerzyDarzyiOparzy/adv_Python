import re

# Tekst do zadań z wyrażeniami regularnymi
text = """Adam Malinowski
.gitignore
2023-01-17 error "Page not found"
[2025-03-06] NOTICE "User admin logged in"
Code 3300 was invalid
https://www.onet.pl 200 176353
File /etc/passwd: permission denied
Józef
C:\\Program Files
Ania
JOLA
marek
Kowalski
bodo363
PIN 0000 was invalid
/users/test is not a valid directory name
192.168.0.1 access denied
1000
666
"""

# Zadanie 1.1 - wszystkie liczby
print("Zadanie 1.1 - wszystkie liczby:")
numbers = re.findall(r'\d+', text)
print(numbers)

# Zadanie 1.2 - liczby co najmniej dwucyfrowe
print("\nZadanie 1.2 - liczby co najmniej dwucyfrowe:")
two_digit_numbers = re.findall(r'\d{2,}', text)
print(two_digit_numbers)

# Zadanie 1.3 - liczby z co najmniej dwoma kolejnymi zerami
print("\nZadanie 1.3 - liczby z co najmniej dwoma kolejnymi zerami:")
numbers_with_zeros = re.findall(r'\d*00\d*', text)
print(numbers_with_zeros)

# Zadanie 1.4 - wyrazy bez cyfr
print("\nZadanie 1.4 - wyrazy bez cyfr:")
words_no_digits = re.findall(r'\b[^\d\W]+\b', text)
print(words_no_digits)

# Zadanie 2 - numery telefonów
tel = ['+48 555 444 333', 
       '(48) 555-444-333',
       '(+48)555444333',
       '+48 555444333', 
       '+48555444333', 
       '48555444333']

print("\nZadanie 2 - numery telefonów:")
phone_pattern = r'[+(]?(\d{2})[) ]?[- ]?(\d{3})[- ]?(\d{3})[- ]?(\d{3})'
phone_numbers = [[(match[0], ''.join(match[1:]))] for number in tel for match in re.findall(phone_pattern, number)]
print(phone_numbers)

# Zadanie 3 - ceny bez waluty
tekst = """
Komputer: 3999.00 PLN, myszka: $30.0, monitor: 399.00 Euro, podkładka: 39 zł
"""

print("\nZadanie 3 - ceny bez waluty:")
prices = re.findall(r'(?<=\$)\d+\.\d+|(?<=: )\d+(?:\.\d+)?(?= (?:PLN|Euro|zł))', tekst)
print(prices)