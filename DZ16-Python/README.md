  ### Домашняя работа к занятию "4.2. Использование Python для решения типовых DevOps задач"

1. Есть скрипт:
```
#!/usr/bin/env python3
a = 1
b = '2'
c = a + b
```
Какое значение будет присвоено переменной c?
```
В данном примере будет ошибка, тк строки с числами не складываются "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
```
Как получить для переменной c значение '12'?
```
Либо переменной a присвоить строковое значение a = '1' либо преобразовать в строку a = str(a)
```
Как получить для переменной c значение 3?
```
Как вариант b = int(b)
```
2. Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?
3. Доработать скрипт так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.

```
#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
        break
```
4. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: drive.google.com, mail.google.com, google.com.
```
#!/usr/bin/env python3

import socket
import time

HOSTS = {}
HOSTS['google.com'] = socket.gethostbyname('google.com')
HOSTS['drive.google.com'] = socket.gethostbyname('drive.google.com')
HOSTS['mail.google.com'] = socket.gethostbyname('mail.google.com')

while True:    
    for SRV in HOSTS.keys():
        LAST_IP = HOSTS.get(SRV)
        CURRENT_IP = socket.gethostbyname(SRV)    
        if CURRENT_IP == LAST_IP:
            print(f'{SRV} - {CURRENT_IP}')
        else:
            print(f'[ERROR] {SRV} IP mismatch: {LAST_IP} - {CURRENT_IP}')
            HOSTS[SRV] = CURRENT_IP
    print()
    time.sleep( 5 )
```
