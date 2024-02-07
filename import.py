import csv
import sqlite3

# Подключение к базе данных SQLite (если базы данных нет, она будет создана)
filename = 'movies.db'  # Путь к файлу с базой данных
conn = sqlite3.connect(filename)
cursor = conn.cursor()

# Создание таблицы в базе данных
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        Title TEXT,
        Year INTEGER,
        Certificate TEXT,
        Runtime TEXT,
        Genre TEXT,
        IMDB_Rating REAL,
        Overview TEXT,
        Meta_score INTEGER,
        Director TEXT,
        Star1 TEXT,
        Star2 TEXT,
        Star3 TEXT,
        Star4 TEXT,
        No_of_Votes INTEGER,
        Gross NUMERIC
    )
''')

# Имя файла CSV и таблицы для импорта
csv_file_path = 'imdb_top_1000.csv'
table_name = 'movies'

# Открытие файла CSV и чтение данных
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Извлечение заголовков столбцов (первая строка файла)
    headers = next(csv_reader)
    
    # Подготовка строки запроса SQL для вставки данных
    placeholders = ', '.join(['?'] * len(headers))
    insert_query = f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES ({placeholders})'
    
    # Вставка данных в базу данных
    for row in csv_reader:
        cursor.execute(insert_query, row)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
