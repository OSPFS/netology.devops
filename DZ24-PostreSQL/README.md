#### Домашняя работа к занятию "6.4 PostgreSQL"

* Задача 1
```
вывода списка БД - \l
подключения к БД - \c db_name;
вывода списка таблиц \d
вывода описания содержимого таблиц - \d+ teble_name
выхода из psql \q
```
* Задача 2
```
select max(avg_width) from pg_stats where tablename='orders';
```
* Задача 3
```
1. Делаем create table для новой orders_temp, которая по структуре является точно копией таблицы order + добавляем  в этот оператор partition by блок
2. Создаем таблицы-секции для таблицы order_temp по тем условиям, которыми мы хотим данные разделить, главное, чтобы они все перекрывали те данные, которые находятся в order
3. Делаем insert into order_temp select <all columns> from order чтобы добавить все данные из обычной таблицы в секционированную
4. Переименуем таблицу order(или удаляем, если уверены в себе и в результате)
5. Переименуем таблицу order_temp в order чтобы приклад писал дальше в неё
```
```
CREATE TABLE orders (
    id integer NOT NULL,
    title character varying(80) NOT NULL,
    price integer DEFAULT 0
) PARTITION BY RANGE (price);

CREATE TABLE low_orders PARTITION OF orders
    FOR VALUES FROM ('0') TO ('499');

CREATE TABLE high_orders PARTITION OF orders
    FOR VALUES FROM ('500'); # Лектор сказал, что надо делать так, но оно так не работает выдаёт:

test_database=# CREATE TABLE high_orders PARTITION OF orders
    FOR VALUES FROM ('500');
ERROR:  syntax error at or near ";"
LINE 2:     FOR VALUES FROM ('500');
                                   ^

поэтому сделаем так:
CREATE TABLE high_orders PARTITION OF orders
    FOR VALUES FROM ('500') to ('999999999');
```
* Задача 4
```
CREATE TABLE orders (
    id integer NOT NULL,
    title character varying(80) UNIQUE NOT NULL,
    price integer DEFAULT 0
);
```