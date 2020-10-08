#### Домашняя работа к занятию "4.3. Языки разметки JSON и YAML"

1. Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```
{ "info" : "Sample JSON output from our service\t",
    "elements" :[
        { "name" : "first",
        "type" : "server",
        "ip" : 7175 
        },
        { "name" : "second",
        "type" : "proxy",
        "ip : 71.78.22.43
        }
    ]
}
```
Нужно найти и исправить все ошибки, которые допускает наш сервис

```
{
  "info": "Sample JSON output from our service",
  "elements": [
    {
      "name": "first",
      "type": "server",
      "ip": "10.0.1.1"
    },
    {
      "name": "second",
      "type": "proxy",
      "ip": "71.78.22.43"
    }
  ]
}
```
2. В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: { "имя сервиса" : "его IP"}. Формат записи YAML по одному сервису: - имя сервиса: его IP. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.
```
JSON:

#!/usr/bin/env python3

import socket
import time
import json

with open('hosts.json') as JFILE:
    HOSTS = json.load(JFILE)   

while True:    
    for SRV in HOSTS.keys():
        LAST_IP = HOSTS.get(SRV)
        CURRENT_IP = socket.gethostbyname(SRV)    
        if CURRENT_IP == LAST_IP:
            print(f'{SRV} - {CURRENT_IP}')
        else:
            print(f'[ERROR] {SRV} IP mismatch: {LAST_IP} - {CURRENT_IP}')
            HOSTS[SRV] = CURRENT_IP
            with open('hosts.json', 'w') as JFILE:
                json.dump(HOSTS, JFILE, indent=2)           
    print()    
    time.sleep(5)
```
```
YAML:

#!/usr/bin/env python3

import socket
import time
import yaml

with open('hosts.yaml') as YFILE:
    HOSTS = yaml.safe_load(YFILE)

while True:    
    for SRV in HOSTS.keys():
        LAST_IP = HOSTS.get(SRV)
        CURRENT_IP = socket.gethostbyname(SRV)    
        if CURRENT_IP == LAST_IP:
            print(f'{SRV} - {CURRENT_IP}')
        else:
            print(f'[ERROR] {SRV} IP mismatch: {LAST_IP} - {CURRENT_IP}')
            HOSTS[SRV] = CURRENT_IP
            with open('hosts.yaml', 'w') as YFILE:
                yaml.dump(HOSTS, YFILE)           
    print()    
    time.sleep(5)
```
