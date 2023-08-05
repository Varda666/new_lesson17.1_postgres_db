"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2


with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="Varda141190") as conn:
    with conn.cursor() as cur:
        postgres_insert_query_customers = """ INSERT INTO customers VALUES (%s,%s,%s)"""
        with open('north_data/customers_data.csv', mode="r", encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=",")
            for row in file_reader:
                if row[0] == "customer_id":
                    pass
                else:
                    record_to_insert_customers = (row[0], row[1], row[2])
                    cur.execute(postgres_insert_query_customers, record_to_insert_customers)

with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="Varda141190") as conn:
    with conn.cursor() as cur:
        postgres_insert_query_employees = """ INSERT INTO employees VALUES (%s,%s,%s,%s,%s,%s)"""
        with open('north_data/employees_data.csv', mode="r", encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=",")
            for row in file_reader:
                if row[0] == "employee_id":
                    pass
                else:
                    record_to_insert_employees = (row[0], row[1], row[2], row[3], row[4], row[5])
                    cur.execute(postgres_insert_query_employees, record_to_insert_employees)

with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="Varda141190") as conn:
    with conn.cursor() as cur:
        postgres_insert_query_orders = """ INSERT INTO orders VALUES (%s,%s,%s,%s,%s)"""
        with open('north_data/orders_data.csv', mode="r", encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=",")
            for row in file_reader:
                if row[0] == "order_id":
                    pass
                else:
                    record_to_insert_orders = (row[0], row[1], row[2], row[3], row[4])
                    cur.execute(postgres_insert_query_orders, record_to_insert_orders)


"""Получает построчно все вакансии из csv-файла
        with open('vacancies.csv', mode="r", encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=",")
            return file_reader
"""