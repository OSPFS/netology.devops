#### Домашняя работа к занятию "6.3 MySQL"

* Задача 1

```
mysql> use test_db
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> \s
--------------
mysql  Ver 8.0.22 for Linux on x86_64 (MySQL Community Server - GPL)

Connection id:		11
Current database:	test_db
Current user:		root@localhost
SSL:			Not in use
Current pager:		stdout
Using outfile:		''
Using delimiter:	;
Server version:		8.0.22 MySQL Community Server - GPL
Protocol version:	10
Connection:		Localhost via UNIX socket
Server characterset:	utf8mb4
Db     characterset:	utf8mb4
Client characterset:	latin1
Conn.  characterset:	latin1
UNIX socket:		/var/run/mysqld/mysqld.sock
Binary data as:		Hexadecimal
Uptime:			1 min 58 sec

Threads: 2  Questions: 56  Slow queries: 0  Opens: 159  Flush tables: 3  Open tables: 79  Queries per second avg: 0.474
--------------
```
```
mysql> show tables;
+-------------------+
| Tables_in_test_db |
+-------------------+
| orders            |
+-------------------+
1 row in set (0.00 sec)
```
```
mysql> select * from orders where price > 300;
+----+----------------+-------+
| id | title          | price |
+----+----------------+-------+
|  2 | My little pony |   500 |
+----+----------------+-------+
1 row in set (0.00 sec)
```
* Задача 2
```
mysql> CREATE USER test IDENTIFIED WITH mysql_native_password BY 'test-pass'
    -> WITH MAX_CONNECTIONS_PER_HOUR 100 PASSWORD EXPIRE INTERVAL 180 DAY 
    -> FAILED_LOGIN_ATTEMPTS 3 ATTRIBUTE '{"fname": "James", "lname": "Pretty"}';
Query OK, 0 rows affected (0.02 sec)

mysql> grant select on test_db.* to test;
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT * FROM INFORMATION_SCHEMA.USER_ATTRIBUTES WHERE USER='test';
+------+------+---------------------------------------+
| USER | HOST | ATTRIBUTE                             |
+------+------+---------------------------------------+
| test | %    | {"fname": "James", "lname": "Pretty"} |
+------+------+---------------------------------------+
1 row in set (0.00 sec)
```
* Задача 3

```
mysql> SET profiling = 1;
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> use test_db
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> select * from orders;
+----+-----------------------+-------+
| id | title                 | price |
+----+-----------------------+-------+
|  1 | War and Peace         |   100 |
|  2 | My little pony        |   500 |
|  3 | Adventure mysql times |   300 |
|  4 | Server gravity falls  |   300 |
|  5 | Log gossips           |   123 |
+----+-----------------------+-------+
5 rows in set (0.00 sec)

mysql> SHOW PROFILES;
+----------+------------+----------------------+
| Query_ID | Duration   | Query                |
+----------+------------+----------------------+
|        1 | 0.00013750 | SELECT DATABASE()    |
|        2 | 0.00109750 | show databases       |
|        3 | 0.00122525 | show tables          |
|        4 | 0.00068725 | select * from orders |
+----------+------------+----------------------+
4 rows in set, 1 warning (0.00 sec)

mysql> SHOW TABLE STATUS WHERE Name = 'orders';
+--------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+---------------------+------------+--------------------+----------+----------------+---------+
| Name   | Engine | Version | Row_format | Rows | Avg_row_length | Data_length | Max_data_length | Index_length | Data_free | Auto_increment | Create_time         | Update_time         | Check_time | Collation          | Checksum | Create_options | Comment |
+--------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+---------------------+------------+--------------------+----------+----------------+---------+
| orders | InnoDB |      10 | Dynamic    |    5 |           3276 |       16384 |               0 |            0 |         0 |              6 | 2020-11-15 19:19:59 | 2020-11-15 19:19:59 | NULL       | utf8mb4_0900_ai_ci |     NULL |                |         |
+--------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+---------------------+------------+--------------------+----------+----------------+---------+
1 row in set (0.01 sec)

Engine = InnoDB
```
```
mysql> ALTER TABLE orders ENGINE = MyISAM;
Query OK, 5 rows affected (0.02 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from orders;
+----+-----------------------+-------+
| id | title                 | price |
+----+-----------------------+-------+
|  1 | War and Peace         |   100 |
|  2 | My little pony        |   500 |
|  3 | Adventure mysql times |   300 |
|  4 | Server gravity falls  |   300 |
|  5 | Log gossips           |   123 |
+----+-----------------------+-------+
5 rows in set (0.00 sec)

mysql> SHOW PROFILES;
+----------+------------+-----------------------------------------+
| Query_ID | Duration   | Query                                   |
+----------+------------+-----------------------------------------+
|        1 | 0.00013750 | SELECT DATABASE()                       |
|        2 | 0.00109750 | show databases                          |
|        3 | 0.00122525 | show tables                             |
|        4 | 0.00068725 | select * from orders                    |
|        5 | 0.00859000 | SHOW TABLE STATUS WHERE Name = 'orders' |
|        6 | 0.00160475 | ALTER TABLE my_table ENGINE = InnoDB    |
|        7 | 0.02701175 | ALTER TABLE orders ENGINE = MyISAM      |
|        8 | 0.00047100 | select * from orders                    |
+----------+------------+-----------------------------------------+
8 rows in set, 1 warning (0.00 sec)
```
Запрос _select * from orders_ на InnoDB выпполнялся за 0.00068725 секунд, 
при изменении на MyISAM время выплнения уменьшилось и стало 0.00047100 секунд

* Задача 4
```
/etc/mysql/conf.d/mysql.cnf:

[mysql]
innodb_buffer_pool_size = 614M # 30% from 2GB
innodb_log_file_size    = 100M
innodb_log_buffer_size  = 1M
innodb-file-per-table   = ON 
```
Как включить компрессию в параметрах my.cnf не нашел, компрессия вроде как включается для каждой таблицы отдельно 
при создании параметром ROW_FORMAT=COMPRESSED, а в my.cnf надо указать innodb-file-per-table = ON 
