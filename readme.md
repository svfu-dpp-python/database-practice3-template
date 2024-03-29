# Лабораторная работа: Работа с SQLite, CSV и GitHub

## Цель работы
Изучить процесс установки SQLite Browser, импорта данных из CSV файла в базу данных SQLite, работу с данными с использованием SQL, и выполнение изменений в коде приложения для расширения его функционала.

## Шаги лабораторной работы

### Шаг 1: Открытие файла CSV в Excel
1. Запустите Microsoft Excel либо аналогичное приложение для работы с электронными таблицами.
2. На вкладке «Данные» импортируйте файл `imdb_top_1000.csv`, укажите в качестве разделителя символ `,` (запятая).
3. Изучите структуру таблицы (названия колонок и типы данных).

### Шаг 3: Импорт данных с помощью скрипта `import.py`
1. Откройте скрипт `import.py` в текстовом редакторе, изучите его и укажите путь к файлу с базой данных SQLite. Название файла нужно придумать самостоятельно. Формат файла `*.db`.
2. Запустите скрипт `import.py` для импорта данных в базу данных.

### Шаг 2: Установка SQLite Browser
1. Скачайте и установите SQLite Browser с официального сайта: [https://sqlitebrowser.org/](https://sqlitebrowser.org/).
2. Запустите SQLite Browser после установки.
3. Откройте созданный файл с базой данных и просмотрите загруженные данные.

### Шаг 4: Просмотр данных с использованием SQLite Browser
1. Откройте SQLite Browser.
2. Выберите базу данных, в которую вы импортировали данные.
3. Просмотрите данные в таблицах с использованием инструментов SQLite Browser.

### Шаг 5: Проверка работы приложения `app.py`
1. Запустите приложение `app.py`.
2. Проверьте его работу, осуществив поиск данных по описанию фильма.
3. Убедитесь, что результаты отображаются корректно.

### Шаг 6: Изменение кода приложения
1. Отредактируйте код приложения `app.py` так, чтобы выполнить поиск по актерам и режиссерам, а не только по описанию.
2. Сохраните изменения.

### Шаг 7: Создание нового коммита и отправка его в GitHub
1. Добавьте изменения в индекс: `git add .`.
2. Создайте новый коммит: `git commit -m "Добавлен поиск по актерам и режиссерам"`.
3. Отправьте коммит на GitHub: `git push`.

## Заключение
После завершения лабораторной работы у вас должны быть установлен SQLite Browser, импортированы данные в базу данных SQLite, и расширена функциональность приложения для поиска по актерам и режиссерам. Созданный коммит должен быть отправлен в ваш репозиторий на GitHub.
