import sqlite3
import csv

# Создание и подключение к БД
connection = sqlite3.connect('library.db')
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Создание таблиц
# Таблица стран
cursor.execute("""
CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    best_season TEXT NOT NULL,
    has_sea INTEGER NOT NULL
)
""")
# Таблица городов
cursor.execute("""
CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    place TEXT NOT NULL,
    cost TEXT NOT NULL
    
)
""")
# Таблица планов
cursor.execute("""
CREATE TABLE travel_plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER NOT NULL,
    planned INTEGER NOT NULL,
    day INTEGER NOT NULL,
    date_returned  TEXT,
    FOREIGN KEY (city_id) PEFERENCES cities(id)
               
   
""")
