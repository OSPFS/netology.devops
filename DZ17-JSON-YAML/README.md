  ### Домашняя работа к занятию "4.3. Языки разметки JSON и YAML"

1. Мы выгрузили JSON, который получили через API запрос к нашему сервису:
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
Нужно найти и исправить все ошибки, которые допускает наш сервис

```
{ "info": "Sample JSON output from our service",
    "elements": [
        { "name": "first",
        "type": "server",
        "ip": "10.0.1.1"
        },
        { "name": "second",
        "type": "proxy",
        "ip": "71.78.22.43"
        }
    ]
}
```

