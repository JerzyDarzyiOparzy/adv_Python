import re

text = """
Adam Malinowski
.gitignore
2023-01-17 error "Page not found"
[2025-03-06] NOTICE "User admin logged in"
Code 3300 was invalid
https://www.onet.pl 200 176353
File /etc/passwd: permission denied
Józef
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

# 1. Linie rozpoczynające się wielką literą
print("1. Linie rozpoczynające się wielką literą:")
wielkie_litery = re.findall(r'^[A-ZŻŹĆĄŚĘŁÓŃ].*', text, re.MULTILINE)
print(wielkie_litery)

# 2. Dopasowania zawierające cyfry
print("\n2. Dopasowania zawierające cyfry:")
cyfry = re.findall(r'\d+', text)
print(cyfry)

# 3. Linie zawierające kropkę
print("\n3. Linie zawierające kropkę:")
kropki = re.findall(r'^.*\..*$', text, re.MULTILINE)
print(kropki)

# 4. Liczby składające się z co najmniej 3 cyfr
print("\n4. Liczby z co najmniej 3 cyframi:")
trzycyfrowe = re.findall(r'\b\d{3,}\b', text)
print(trzycyfrowe)

# 5. Linie zawierające liczby z co najmniej 3 cyframi
print("\n5. Linie z liczbami co najmniej 3-cyfrowymi:")
linie_trzycyfrowe = re.findall(r'^.*\b\d{3,}\b.*$', text, re.MULTILINE)
print(linie_trzycyfrowe)

# 6. Linie zawierające tylko litery
print("\n6. Linie zawierające tylko litery:")
tylko_litery = re.findall(r'^[a-zA-ZżźćąśęłóńŻŹĆĄŚĘŁÓŃ]+$', text, re.MULTILINE)
print(tylko_litery)

# 7. Linie zawierające tylko cyfry
print("\n7. Linie zawierające tylko cyfry:")
tylko_cyfry = re.findall(r'^\d+$', text, re.MULTILINE)
print(tylko_cyfry)

# 8. Dopasowania zawierające valid lub invalid
print("\n8. Dopasowania z valid/invalid:")
valid_invalid = re.findall(r'\w*valid\w*', text)
print(valid_invalid)

# 9. Daty w formacie YYYY-MM-DD
print("\n9. Daty w formacie YYYY-MM-DD:")
daty = re.findall(r'\d{4}-\d{2}-\d{2}', text)
print(daty)

# 10. Ścieżki UNIX
print("\n10. Ścieżki UNIX:")
sciezki = re.findall(r'/[^\s]+/[^\s]+', text)
print(sciezki)

# 11. Adresy IP v4
print("\n11. Adresy IP v4:")
ip = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
print(ip)

# 12. Tekst w cudzysłowach
print("\n12. Tekst w cudzysłowach:")
cytaty = re.findall(r'"([^"]*)"', text)
print(cytaty)

# 13. Linie o długości 4 znaków
print("\n13. Linie o długości 4 znaków:")
cztery_znaki = re.findall(r'^.{4}$', text, re.MULTILINE)
print(cztery_znaki)