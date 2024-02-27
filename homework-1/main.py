"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
import os

customers_path = os.path.join("north_data", "customers_data.csv")
employees_path = os.path.join("north_data", "employees_data.csv")
orders_path = os.path.join("north_data", "orders_data.csv")

with open(customers_path, "r") as f:
    customers_reader = csv.DictReader(f)
    customers_data = []
    for row in customers_reader:
        customers_data.append(tuple(row.values()))

with open(employees_path, "r") as f:
    employees_reader = csv.DictReader(f)
    employees_data = []
    for row in employees_reader:
        employees_data.append(tuple(row.values()))

with open(orders_path, "r") as f:
    orders_reader = csv.DictReader(f)
    orders_data = []
    for row in orders_reader:
        orders_data.append(tuple(row.values()))


conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='852467913'
)

try:
    with conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO customers VALUES(%s, %s, %s)", customers_data)
            cur.execute("SELECT * FROM customers")

            cur.executemany("INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)", employees_data)
            cur.execute("SELECT * FROM employees")

            cur.executemany("INSERT INTO orders VALUES(%s, %s, %s, %s, %s)", orders_data)
            cur.execute("SELECT * FROM orders")

except psycopg2.Error as e:
    print("Ошибка при вставке данных:", e)
finally:
    conn.close()