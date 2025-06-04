import threading
from tqdm import tqdm
import psutil
import time

binary = '111'  # To string, a nie wartość binarna

print(binary)
# '111' — po prostu wypisanie stringa

print(bin(int(binary)))
# '0b1101111' — najpierw konwertujemy string '111' na liczbę dziesiętną: int('111') == 111,
# potem zamieniamy 111 na postać binarną: bin(111) == '0b1101111'

print(int(binary))
# 111 — domyślna interpretacja stringa jako liczby dziesiętnej

print(hex(int(binary)))
# '0x6f' — int('111') == 111, a hex(111) == '0x6f'

print(int(binary, base=2))
# 7 — interpretujemy '111' jako liczbę binarną (1*2^2 + 1*2^1 + 1*2^0)

print(int(binary, base=8))
# 73 — interpretujemy '111' jako liczbę ósemkową (1*8^2 + 1*8^1 + 1*8^0 = 64 + 8 + 1)

print(int(binary, base=16))
# 273 — interpretujemy '111' jako szesnastkową (1*16^2 + 1*16^1 + 1*16^0 = 256 + 16 + 1)

import this

# this.d to słownik kodujący (ROT13) — nie trzeba tworzyć nowego słownika
cipher = this.d

# Wczytanie zdania od użytkownika
text = input("Wpisz zdanie do zakodowania: ")

# Zakodowanie tekstu: dla każdego znaku pobierz zamiennik z cipher, jeśli nie ma — przepisz znak bez zmian
encoded = ''.join(cipher.get(char, char) for char in text)

print("Zakodowane zdanie:", encoded)

import threading
import requests

def fetch_and_save(url, filename):
    response = requests.get(url)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f"Zakończono pobieranie: {url}")

urls = [
    ("https://www.python.org", "python.html"),
    ("https://www.wikipedia.org", "wikipedia.html"),
    ("https://www.openai.com", "openai.html"),
    ("https://www.github.com", "github.html"),
    ("https://www.stackoverflow.com", "stackoverflow.html")
]

threads = []

for url, filename in urls:
    t = threading.Thread(target=fetch_and_save, args=(url, filename))
    threads.append(t)
    t.start()

for t in threads:
    t.join()



while True:
    mem = psutil.virtual_memory()
    print(f"Zużycie pamięci RAM: {mem.percent}%")
    time.sleep(1)



def read_file_with_progress(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in tqdm(lines, desc=filepath):
            time.sleep(0.01)  # sztuczne opóźnienie symulujące wolne czytanie

filepaths = [
    "C:/Games/data1.txt",
    "C:/Games/data2.txt",
    "C:/Games/data3.txt"
]

threads = []

for path in filepaths:
    t = threading.Thread(target=read_file_with_progress, args=(path,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()