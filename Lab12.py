import os
import threading
import multiprocessing as mp
import pandas as pd
import time
import csv
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import random
from tqdm import tqdm
import requests

# Zadanie 1: Porównanie czasu wykonania dla wątków i procesów

def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)

def test_threads(n, repeats=3):
    total_time = 0
    for _ in range(repeats):
        threads = []
        t0 = time.perf_counter()
        
        for _ in range(os.cpu_count()):
            threads.append(threading.Thread(target=fib, args=(n,)))
        
        for t in threads:
            t.start()   
        
        for t in threads:
            t.join()
        
        total_time += time.perf_counter() - t0
    
    return total_time / repeats

def test_processes(n, repeats=3):
    total_time = 0
    for _ in range(repeats):
        processes = []
        t0 = time.perf_counter()
        
        for _ in range(os.cpu_count()):
            processes.append(mp.Process(target=fib, args=(n,)))
        
        for p in processes:
            p.start()   
        
        for p in processes:
            p.join()
        
        total_time += time.perf_counter() - t0
    
    return total_time / repeats

def run_task1(n_values, repeats=3, output_file='fibo_comparison.csv'):
    results = []
    
    for n in n_values:
        print(f"Testowanie dla fib({n})...")
        thread_time = test_threads(n, repeats)
        process_time = test_processes(n, repeats)
        
        results.append({
            'n': n,
            'thread_time': thread_time,
            'process_time': process_time
        })
        
        # Zapisujemy wyniki na bieżąco
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = ['n', 'thread_time', 'process_time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for result in results:
                writer.writerow(result)
        
        print(f"fib({n}): Wątki: {thread_time:.4f}s, Procesy: {process_time:.4f}s")
    
    return results

def plot_results(csv_file='fibo_comparison.csv'):
    df = pd.read_csv(csv_file)
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['n'], df['thread_time'], 'b-', marker='o', label='Wątki')
    plt.plot(df['n'], df['process_time'], 'r-', marker='s', label='Procesy')
    plt.xlabel('Wartość n dla funkcji fib(n)')
    plt.ylabel('Średni czas wykonania (s)')
    plt.title('Porównanie czasu wykonania dla wątków i procesów')
    plt.legend()
    plt.grid(True)
    plt.savefig('fibo_comparison.png')
    plt.close()

# Zadanie 2: Przepisanie kodu z Lab11 używając ThreadPoolExecutor

def fetch_and_save(url_filename):
    url, filename = url_filename
    response = requests.get(url)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f"Zakończono pobieranie: {url}")
    return f"Pobrano {url} do {filename}"

def run_task2():
    urls = [
        ("https://www.python.org", "python.html"),
        ("https://www.wikipedia.org", "wikipedia.html"),
        ("https://www.openai.com", "openai.html"),
        ("https://www.github.com", "github.html"),
        ("https://www.stackoverflow.com", "stackoverflow.html")
    ]
    
    # Używamy ThreadPoolExecutor z połową dostępnych rdzeni
    max_workers = max(1, os.cpu_count() // 2)
    print(f"Używam {max_workers} wątków (połowa dostępnych rdzeni)")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(fetch_and_save, urls))
    
    for result in results:
        print(result)

# Zadanie 3: Generowanie i przetwarzanie dużych zbiorów danych

def build_dataset(filename, n_rows=100, chunk_size=100000):
    header = ['id', 'firstname', 'lastname', 'age', 'salary']
    firstnames = ['Adam', 'Katarzyna', 'Krzysztof', 'Marek', 'Aleksandra', 'Zbigniew', 'Wojciech', 'Mieczysław', 'Agata', 'Wisława']
    lastnames = ['Mieczykowski', 'Kowalski', 'Malinowski', 'Szczaw', 'Glut', 'Barański', 'Brzęczyszczykiewicz', 'Wróblewski', 'Wlotka', 'Pysla']
    age = {'min': 18, 'max': 68}
    salary = {'min': 3200, 'max': 12500}
    
    rows = []
    rows.append(header)
    mu = (salary['max'] + salary['min']) / 2
    sigma = 1000

    with open(filename, 'w', encoding='utf-8') as filehandler:
        for id in tqdm(range(1, n_rows + 1), total=n_rows, desc=f"Building dataset {filename}..."):
            row = [
                f'{id}', 
                f'{random.choice(firstnames)}', 
                f'{random.choice(lastnames)}', 
                f"{random.randint(age['min'], age['max'])}",
                f"{round(float(random.normalvariate(mu=mu, sigma=sigma)), 2)}"
            ]
            rows.append(row)
            if id % chunk_size == 0:
                filehandler.writelines([f"{','.join(row)}\n" for row in rows])
                rows = []
        
        # Zapisz pozostałe wiersze
        if rows:
            filehandler.writelines([f"{','.join(row)}\n" for row in rows])

def generate_datasets(num_files=4, rows_per_file=10_000_000):
    filenames = [f'employee_{i}.csv' for i in range(1, num_files + 1)]
    
    for filename in filenames:
        build_dataset(filename, rows_per_file, chunk_size=100000)
    
    return filenames

def load_dataframe(filename):
    print(f"Wczytywanie {filename}...")
    return pd.read_csv(filename)

def sequential_load_and_merge(filenames):
    t0 = time.perf_counter()
    
    # Wczytaj sekwencyjnie
    dataframes = []
    for filename in filenames:
        df = load_dataframe(filename)
        dataframes.append(df)
    
    # Scal ramki danych
    merged_df = pd.concat(dataframes, ignore_index=True)
    
    total_time = time.perf_counter() - t0
    print(f"Czas sekwencyjnego wczytania i scalenia: {total_time:.4f}s")
    print(f"Rozmiar scalonej ramki: {len(merged_df)} wierszy")
    
    return total_time

def parallel_load_and_merge(filenames):
    t0 = time.perf_counter()
    
    # Wczytaj równolegle
    with ProcessPoolExecutor() as executor:
        dataframes = list(executor.map(load_dataframe, filenames))
    
    # Scal ramki danych
    merged_df = pd.concat(dataframes, ignore_index=True)
    
    total_time = time.perf_counter() - t0
    print(f"Czas równoległego wczytania i scalenia: {total_time:.4f}s")
    print(f"Rozmiar scalonej ramki: {len(merged_df)} wierszy")
    
    return total_time

def run_task3(generate=True, num_files=4, rows_per_file=10_000_000):
    if generate:
        print(f"Generowanie {num_files} zbiorów danych po {rows_per_file} wierszy każdy...")
        filenames = generate_datasets(num_files, rows_per_file)
    else:
        filenames = [f'employee_{i}.csv' for i in range(1, num_files + 1)]
        
    print("Wczytywanie i scalanie sekwencyjne...")
    seq_time = sequential_load_and_merge(filenames)
    
    print("Wczytywanie i scalanie równoległe...")
    par_time = parallel_load_and_merge(filenames)
    
    print(f"Przyspieszenie: {seq_time / par_time:.2f}x")

if __name__ == "__main__":
    print("Lab 12 - Przetwarzanie równoległe w Pythonie")
    
    # Zadanie 1
    print("\n--- Zadanie 1: Porównanie czasu wykonania dla wątków i procesów ---")
    results = run_task1([20, 25, 30], repeats=2)
    plot_results()
    
    # Zadanie 2
    print("\n--- Zadanie 2: Przepisanie kodu z Lab11 używając ThreadPoolExecutor ---")
    run_task2()
    
    # Zadanie 3
    print("\n--- Zadanie 3: Generowanie i przetwarzanie dużych zbiorów danych ---")
    run_task3(generate=True, num_files=4, rows_per_file=10000)
