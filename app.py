import sqlite3
import tkinter as tk
from tkinter import ttk


def main():
    """Главная функция"""

    # Главное окно приложения
    root_window = tk.Tk()
    root_window.title("База данных фильмов")

    # Невидимая рамка для элементов поиска
    global search_editor
    search_frame = tk.Frame(root_window)
    search_frame.pack(fill=tk.X)

    # Поле для ввода строки поиска
    search_editor = tk.Entry(search_frame, width=40)
    search_editor.pack(side=tk.LEFT, expand=1, fill=tk.X)

    # Кнопка для запуска поиска
    search_button = tk.Button(search_frame, text="Поиск", command=search)
    search_button.pack(side=tk.LEFT)

    # Кнопка для отмены поиска
    cancel_button = tk.Button(search_frame, text="Отмена", command=cancel)
    cancel_button.pack(side=tk.LEFT)

    # Названия колонок отображаемые в заголовках таблицы
    columns_gui = ('Название', 'Рейтинг', 'Описание',
                   'Режиссер', 'Актер1', 'Актер2', 'Актер3')

    # Ширина колонок в таблице
    columns_width = (300, 100, 400, 200, 200, 200, 200)

    # Табличное поле
    global table
    table = ttk.Treeview(root_window, columns=columns_gui, show="headings")
    for name, width in zip(columns_gui, columns_width):
        table.heading(name, text=name)  # Заголовки столбцов
        table.column(name, width=width)  # Ширина столбцов
    table.pack(expand=1, fill=tk.BOTH)

    # Отменяем поиск
    cancel()

    # Показываем окну приложения и ждем его закрытия
    root_window.mainloop()


def search():
    """Реакция на кнопку поиска"""

    # Получаем строку из поля ввода
    user_query = search_editor.get()

    # Удаляем строки из таблицы
    for row in table.get_children():
        table.delete(row)

    # Добавляем строки - результат запроса
    for row in retrieve_rows(user_query):
        table.insert("", "end", values=row)


def cancel():
    """Реакция на кнопку отмены поиска"""

    # Очищаем поле ввода
    search_editor.delete(0)

    # Удаляем строки из таблицы
    for row in table.get_children():
        table.delete(row)

    # Добавляем все строки из таблицы
    for row in retrieve_rows():
        table.insert("", "end", values=row)


def retrieve_rows(user_query=''):
    """Подготовка SQL-запроса к базе данных"""

    # Названия колонок в таблице в базе данных
    columns_db = ('Title', 'IMDB_Rating', 'Overview',
                  'Director', 'Star1', 'Star2', 'Star3')
    cols = ', '.join([f'`{col}`' for col in columns_db])

    # Имя таблицы, в которой вы хотите выполнить поиск
    table_name = 'movies'

    # Текст и параметры запроса
    query = f"SELECT {cols} FROM `{table_name}`"
    params = []

    # Если задан пользовательский запрос
    if user_query:
        # Добавляем условие на название фильма
        query += f" WHERE `Title` LIKE ?"
        params.append(f'%{user_query}%')

        # Добавляем условие на описание фильма
        query += f" OR `Overview` LIKE ?"
        params.append(f'%{user_query}%')

    # Выполняем запрос и возвращаем результат
    return get_query_results(query, params)


def get_query_results(sql_query, params):
    """Выполнение SQL-запроса"""

    # Файл с базой данных
    database = 'movies.db'

    # Подключаемся к базе данных
    connection = sqlite3.connect(database)

    # Выполняем запрос
    cursor = connection.cursor()
    # if params:
    cursor.execute(sql_query, params)
    # else:
    #     cursor.execute(sql_query)

    # Получаем результат запроса
    results = cursor.fetchall()

    # Закрываем соединение к базе данных
    connection.close()

    # Возвращаем результат запроса
    return results


if __name__ == '__main__':
    search_editor: tk.Entry
    table: ttk.Treeview

    # Запуск главной функции
    main()
