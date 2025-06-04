import os
import zipfile
import pandas as pd
import sys

# Ścieżka do pliku ZIP
zip_path = 'dane/test.zip'
extract_path = 'dane'

# Rozpakuj ZIP
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

# Licz foldery i pliki w rozpakowanym katalogu
base_folder = os.path.join(extract_path, 'test')
folder_count = 0
file_count = 0

for root, dirs, files in os.walk(base_folder):
    # Pomijamy katalog główny
    if root != base_folder:
        folder_count += len(dirs)
        file_count += len(files)

print(f"[Zadanie 1] Liczba folderów: {folder_count}")
print(f"[Zadanie 1] Liczba plików: {file_count}")

def file_stats(base_path, folder_name):
    for root, dirs, files in os.walk(base_path):
        if os.path.basename(root) == folder_name:
            total_size = 0
            file_count = 0
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    total_size += os.path.getsize(file_path)
                    file_count += 1
            return file_count, total_size
    return 0, 0

# Przykład użycia:
print(file_stats('dane/test', '3'))

def fs_stats(path):
    data = []
    for root, dirs, files in os.walk(path):
        for name in dirs + files:
            full_path = os.path.join(root, name)
            is_file = os.path.isfile(full_path)
            is_dir = os.path.isdir(full_path)
            size = os.path.getsize(full_path) if is_file else 0
            try:
                line_count = sum(1 for _ in open(full_path, encoding='utf-8')) if is_file else 0
            except:
                line_count = 0
            data.append({
                "nazwa": name,
                "ścieżka_względna": os.path.relpath(full_path, path),
                "ścieżka_bezwzględna": os.path.abspath(full_path),
                "czy_folder": is_dir,
                "czy_plik": is_file,
                "rozmiar_bajty": size,
                "liczba_linii": line_count
            })
    return pd.DataFrame(data)

# Przykład:
df = fs_stats('dane/test')
print(df.head())

def save_all_texts_to_csv(path, output_csv='scalone_dane.csv'):
    df = fs_stats(path)
    text_data = []

    for _, row in df[df['czy_plik']].iterrows():
        try:
            with open(row['ścieżka_bezwzględna'], 'r', encoding='utf-8') as f:
                content = f.read()
            text_data.append({
                'plik': row['ścieżka_względna'],
                'treść': content
            })
        except:
            continue  # pomiń pliki binarne lub z błędnym kodowaniem

    result_df = pd.DataFrame(text_data)
    result_df.to_csv(output_csv, index=False)
    print(f"[Zadanie 4] Zapisano {len(result_df)} plików do pliku {output_csv}")

# Przykład:
save_all_texts_to_csv('dane/test')

print("[Zadanie 5] Porównanie sys.getsizeof dla list")

a = []
b = [1]
c = [1, 2, 3]

print(f"Pusta lista: {sys.getsizeof(a)} bajtów")
print(f"Lista z 1 elementem: {sys.getsizeof(b)} bajtów")
print(f"Lista z 3 elementami: {sys.getsizeof(c)} bajtów")

print("Wyjaśnienie: sys.getsizeof() mierzy rozmiar obiektu w pamięci (nie zawartości).\nLista w Pythonie to dynamiczna tablica, która rezerwuje pamięć z nadmiarem.\nRozmiar rośnie skokowo przy dodawaniu elementów (np. x1.125 lub x2).\n")