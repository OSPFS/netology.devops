#### Домашняя работа к занятию "6.2. SQL"

* Задача 1

```
version: '3.1'

services:

  db:
    image: postgres:12
    restart: always
    environment:
      POSTGRES_PASSWORD: 123456xx
      PGDATA: /srv/db      
    volumes:
      - db:/srv/db
      - bckp:/srv/backup

volumes:
  db:
  bckp:
```

* Задача 2

Итоговый список БД

```
test_db=# \l
                                     List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |       Access privileges
-----------+----------+----------+------------+------------+-------------------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres                  +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres                  +
           |          |          |            |            | postgres=CTc/postgres
 test_db   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =Tc/postgres                 +
           |          |          |            |            | postgres=CTc/postgres        +
           |          |          |            |            | "test-admin-user"=c/postgres +
           |          |          |            |            | "test-simple-user"=c/postgres
(4 rows)
```
Описание таблиц:
```
test_db=# \d clients
                                      Table "public.clients"
   Column    |          Type          | Collation | Nullable |               Default
-------------+------------------------+-----------+----------+-------------------------------------
 id          | integer                |           | not null | nextval('clients_id_seq'::regclass)
 second_name | character varying(255) |           |          |
 country     | character varying(255) |           |          |
 fc_order    | integer                |           |          |
Indexes:
    "clients_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "clients_fc_order_fkey" FOREIGN KEY (fc_order) REFERENCES orders(id)

test_db=# \d orders
                                    Table "public.orders"
 Column |          Type          | Collation | Nullable |              Default
--------+------------------------+-----------+----------+------------------------------------
 id     | integer                |           | not null | nextval('orders_id_seq'::regclass)
 item   | character varying(255) |           |          |
 price  | integer                |           |          |
Indexes:
    "orders_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "clients" CONSTRAINT "clients_fc_order_fkey" FOREIGN KEY (fc_order) REFERENCES orders(id)
```
SQL-запрос для выдачи списка пользователей с правами над таблицами test_db
```
test_db=# SELECT table_catalog, table_schema, table_name, privilege_type
test_db-# FROM   information_schema.table_privileges
test_db-# WHERE  grantee = 'test-admin-user'
test_db-# ;
 table_catalog | table_schema | table_name | privilege_type
---------------+--------------+------------+----------------
 test_db       | public       | orders     | INSERT
 test_db       | public       | orders     | SELECT
 test_db       | public       | orders     | UPDATE
 test_db       | public       | orders     | DELETE
 test_db       | public       | orders     | TRUNCATE
 test_db       | public       | orders     | REFERENCES
 test_db       | public       | orders     | TRIGGER
 test_db       | public       | clients    | INSERT
 test_db       | public       | clients    | SELECT
 test_db       | public       | clients    | UPDATE
 test_db       | public       | clients    | DELETE
 test_db       | public       | clients    | TRUNCATE
 test_db       | public       | clients    | REFERENCES
 test_db       | public       | clients    | TRIGGER
(14 rows)

test_db=# SELECT table_catalog, table_schema, table_name, privilege_type
FROM   information_schema.table_privileges
WHERE  grantee = 'test-simple-user'
;
 table_catalog | table_schema | table_name | privilege_type
---------------+--------------+------------+----------------
 test_db       | public       | orders     | INSERT
 test_db       | public       | orders     | SELECT
 test_db       | public       | orders     | UPDATE
 test_db       | public       | orders     | DELETE
 test_db       | public       | clients    | INSERT
 test_db       | public       | clients    | SELECT
 test_db       | public       | clients    | UPDATE
 test_db       | public       | clients    | DELETE
(8 rows)
```
* Задача 3

```
insert into orders (item,price) values ('Шоколад',10),
('Принтер',3000),
('Книга',500),
('Монитор',7000),
('Гитара',4000);
INSERT 0 5

insert into clients (second_name,country) values 
('Иванов Иван Иванович','USA'),
('Петров Петр Петрович','Canada'),
('Иоганн Себастьян Бах','Japan'),
('Ронни Джеймс Дио','Russia'),
('Ritchie Blackmore','Russia');
INSERT 0 5

test_db=# select count (*) from clients;
 count
-------
     5
(1 row)

test_db=# select count (*) from orders;
 count
-------
     5
(1 row)
```
* Задача 4
```
update clients set fc_order=3 where second_name='Иванов Иван Иванович';
update clients set fc_order=4 where second_name='Петров Петр Петрович';
update clients set fc_order=5 where second_name='Иоганн Себастьян Бах';

test_db=# select second_name from clients where fc_order>0;
     second_name
----------------------
 Иванов Иван Иванович
 Петров Петр Петрович
 Иоганн Себастьян Бах
(3 rows)
```
* Задача 5
```
test_db=# explain select second_name from clients where fc_order>0;
                        QUERY PLAN
-----------------------------------------------------------
 Seq Scan on clients  (cost=0.00..10.88 rows=23 width=516)
   Filter: (fc_order > 0)
(2 rows)

Поочередно пройти по записям в таблице clients отфильтровать по полю fc_order, где значение больше 0
```
* Задача 6

Создаём бэкап
```
root@0260c87aeae1:/# pg_dump -U postgres test_db > /srv/backup/test_db.sql
```

Переделаем docker-compose.yml
```
version: '3.1'

services:

  db:
    image: postgres:12
    restart: always
    environment:
      POSTGRES_PASSWORD: 123456xx
      PGDATA: /srv/db
    volumes:
      - db:/srv/db
      - bckp:/srv/backup

  db2:
    image: postgres:12
    restart: always
    environment:
      POSTGRES_PASSWORD: 123456xx
      PGDATA: /srv/db
    volumes:
      - db2:/srv/db
      - bckp:/srv/backup

volumes:
  db:
  db2:
  bckp:
```

Восстановим БД в другом контейнере
```
root@ee1f7a87f3d5:/# psql -U postgres -c 'create database test_db;'
CREATE DATABASE
root@ee1f7a87f3d5:/# psql -U postgres -c 'create user "test-admin-user";'
CREATE ROLE
root@ee1f7a87f3d5:/# psql -U postgres -c 'create user "test-simple-user";'
CREATE ROLE

root@ee1f7a87f3d5:/# psql -U postgres --set ON_ERROR_STOP=on test_db < /srv/backup/test_db.sql
```
Проверим:
```
root@ee1f7a87f3d5:/# psql -U postgres -d test_db -c 'select * from clients;'
 id |     second_name      | country | fc_order
----+----------------------+---------+----------
  4 | Ронни Джеймс Дио     | Russia  |
  5 | Ritchie Blackmore    | Russia  |
  1 | Иванов Иван Иванович | USA     |        3
  2 | Петров Петр Петрович | Canada  |        4
  3 | Иоганн Себастьян Бах | Japan   |        5
(5 rows)
```
