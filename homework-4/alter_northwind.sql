-- Подключиться к БД Northwind и сделать следующие изменения:

import psycopg2


with psycopg2.connect(host="localhost", database="northwind", user="postgres", password="Varda141190") as conn:
    with conn.cursor() as cur:

-- 1. Добавить ограничение на поле unit_price таблицы products (цена должна быть больше 0)
postgres_insert_query_products = """ALTER TABLE products ADD CONSTRAINT chk_products_unit_price CHECK (unit_price >= 0);"""
cur.execute(postgres_insert_query_products)

-- 2. Добавить ограничение, что поле discontinued таблицы products может содержать только значения 0 или 1

postgres_insert_query_products = """ALTER TABLE products ADD CONSTRAINT chk_products_discontinued CHECK (discontinued IN (0, 1));"""
cur.execute(postgres_insert_query_products)

-- 3. Создать новую таблицу, содержащую все продукты, снятые с продажи (discontinued = 1)

postgres_insert_query_products = """SELECT * INTO top_products FROM products WHERE discontinued = 1;"""
cur.execute(postgres_insert_query_products)

-- 4. Удалить из products товары, снятые с продажи (discontinued = 1)
-- Для 4-го пункта может потребоваться удаление ограничения, связанного с foreign_key. Подумайте, как это можно решить, чтобы связь с таблицей order_details все же осталась.

postgres_insert_query_products = """
ALTER TABLE order_details DROP CONSTRAINT fk_order_details_products;
DELETE FROM products WHERE discontinued = 1;
ALTER TABLE order_details
ADD CONSTRAINT fk_order_details_products
FOREIGN KEY(product_id)
REFERENCES products(product_id);
"""
cur.execute(postgres_insert_query_products)

