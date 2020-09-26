### Домашняя работа к занятию "3.8. Компьютерные сети, лекция 3"

1. ipvs. Если при запросе на VIP сделать подряд несколько запросов (например, for i in {1..50}; do curl -I -s 172.28.128.200>/dev/null; done ), ответы будут получены почти мгновенно. Тем не менее, в выводе ipvsadm -Ln еще некоторое время будут висеть активные InActConn. Почему так происходит?
```
Потому что, director не видит обратные пакеты от реала к клиенту, в том числе пакеты с флагами FIN и не знает точно закрыто соединение или нет.
```
2. Конфигурационные файлы показаны в п. 3, а так-же предоставлен рабочий vagrant файл для проверки пп 2 и 3
3. В лекции мы использовали только 1 VIP адрес для балансировки. У такого подхода несколько отрицательных моментов, один из которых – невозможность активного использования нескольких хостов (1 адрес может только переехать с master на standby). Подумайте, сколько адресов оптимально использовать, если мы хотим без какой-либо деградации выдерживать потерю 1 из 3 хостов при входящем трафике 1.5 Гбит/с и физических линках хостов в 1 Гбит/с? Предполагается, что мы хотим задействовать 3 балансировщика в активном режиме (то есть не 2 адреса на 3 хоста, один из которых в обычное время простаивает).
```
Если мы хотим иметь 3 активных хоста, то нам надо иметь и 3 IP адреса. 
Для обеспечения работоспособности каждого адреса, предлагаю следующую конфигурацию keepalived:

root@b1:~# cat /etc/keepalived/keepalived.conf
! Configuration File for keepalived

vrrp_instance VI_1 {
    state MASTER
    interface eth1
    virtual_router_id 55
    priority 102 #used in election, 101 for master & 100 for backup
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass P0S@word2
    }
    virtual_ipaddress {
        10.10.1.10/24
    }
}

vrrp_instance VI_2 {
    state BACKUP
    interface eth1
    virtual_router_id 56
    priority 101 #used in election, 101 for master & 100 for backup
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass P0S@word2
    }
    virtual_ipaddress {
        10.10.1.20/24
    }
}

vrrp_instance VI_3 {
    state BACKUP
    interface eth1
    virtual_router_id 57
    priority 100 #used in election, 101 for master & 100 for backup
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass P0S@word2
    }
    virtual_ipaddress {
        10.10.1.30/24
    }
}
root@b1:~#

root@b2:~# cat /etc/keepalived/keepalived.conf
! Configuration File for keepalived

vrrp_instance VI_1 {
    state BACKUP
    interface eth1
    virtual_router_id 55
    priority 101 #used in election, 101 for master & 100 for backup
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass P0S@word2
    }
    virtual_ipaddress {
        10.10.1.10/24
    }
}

vrrp_instance VI_2 {
    state MASTER
    interface eth1
    virtual_router_id 56
    priority 102 #used in election, 101 for master & 100 for backup
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass P0S@word2
    }
    virtual_ipaddress {
        10.10.1.20/24
    }
}

vrrp_instance VI_3 {
    state BACKUP
    interface eth1
    virtual_router_id 57
    priority 100 #used in election, 101 for master & 100 for backup
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass P0S@word2
    }
    virtual_ipaddress {
        10.10.1.30/24
    }
}
root@b2:~#

root@b3:~# cat /etc/keepalived/keepalived.conf
! Configuration File for keepalived

vrrp_instance VI_1 {
    state BACKUP
    interface eth1
    virtual_router_id 55
    priority 100 #used in election, 101 for master & 100 for backup
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass P0S@word2
    }
    virtual_ipaddress {
        10.10.1.10/24
    }
}

vrrp_instance VI_2 {
    state BACKUP
    interface eth1
    virtual_router_id 56
    priority 101 #used in election, 101 for master & 100 for backup
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass P0S@word2
    }
    virtual_ipaddress {
        10.10.1.20/24
    }
}

vrrp_instance VI_3 {
    state MASTER
    interface eth1
    virtual_router_id 57
    priority 102 #used in election, 101 for master & 100 for backup
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass P0S@word2
    }
    virtual_ipaddress {
        10.10.1.30/24
    }
}
root@b3:~#

И конфигурацию IPVS:

IP Virtual Server version 1.2.1 (size=4096)
Prot LocalAddress:Port Scheduler Flags
  -> RemoteAddress:Port           Forward Weight ActiveConn InActConn
TCP  10.10.1.10:80 rr
  -> 10.10.1.11:80                Route   1      0          0
  -> 10.10.1.12:80                Route   1      0          0
TCP  10.10.1.20:80 rr
  -> 10.10.1.11:80                Route   1      0          0
  -> 10.10.1.12:80                Route   1      0          0
TCP  10.10.1.30:80 rr
  -> 10.10.1.11:80                Route   1      0          0
  -> 10.10.1.12:80                Route   1      0          0
```