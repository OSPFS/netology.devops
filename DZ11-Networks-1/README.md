### Домашняя работа к занятию "3.6. Компьютерные сети, лекция 1"

2. Узнайте о том, сколько действительно независимых (не пересекающихся) каналов есть в разделяемой среде WiFi при работе на 2.4 ГГц. Стандарты с полосой 5 ГГц более актуальны, но регламенты на 5 ГГц существенно различаются в разных странах, а так же не раз обновлялись. В качестве дополнительного вопроса вне зачета, попробуйте найти актуалый ответ и на этот вопрос.
```
Wi-Fi 2.4 GHz - 3 неперекрывающихся канала: 1, 6, 11

Частотные полосы и каналы WiFi в 5 GHz
Базовая мировая практика, которая может существенно изменяться по странам.

UNII-1:                    5150 – 5250 MHz (доступно 4 частотных канала WiFi)
UNII-2:                    5250 – 5350 MHz (доступно 4 частотных канала WiFi)
UNII-2 Extended:           5470 – 5725 MHz (доступно 11 частотных каналов WiFi)
UNII-3:                    5725 – 5825 MHz (доступно 4 частотных канала WiFi)

PS. Взято с http://wi-life.ru/texnologii/wi-fi/wi-fi-frequency-bands-and-channels
```
3. Адрес канального уровня – MAC адрес – это 6 байт, первые 3 из которых называются OUI – Organizationally Unique Identifier или уникальный идентификатор организации. Какому производителю принадлежит MAC 38:f9:d3:55:55:79?
```
38-F9-D3	Apple, Inc.
```
4. Каким будет payload TCP сегмента, если Ethernet MTU задан в 9001 байт, размер заголовков IPv4 – 20 байт, а TCP – 32 байта?
```
8949
```
5. Может ли во флагах TCP одновременно быть установлены флаги SYN и FIN при штатном режиме работы сети? Почему да или нет?
```
При штатном режиме, такой ситуации быть не должно, тк SYN отвечает за начальную установку TCP соединения,
а FIN за завершение.
```
6. ss -ula sport = :53 Почему в State присутствует только UNCONN, и может ли там присутствовать, например, TIME-WAIT?
```
Нет, тк это udp и он не создает сессий, пришел пакет - хоршо, не пришел - проблемы приложения
```
7. Обладая знаниями о том, как штатным образом завершается соединение (FIN от инициатора, FIN-ACK от ответчика, ACK от инициатора), опишите в каких состояниях будет находиться TCP соединение в каждый момент времени на клиенте и на сервере при завершении. 
```
      HOST A                            HOST B
1)  ESTABLISHED                      ESTABLISHED
2)  FIN-WAIT-1  -->   FIN,ACK   -->  CLOSE-WAIT
3)  FIN-WAIT-2  <--   ACK       <--  CLOSE-WAIT
4)  TIME-WAIT   <--   FIN,ACK   <--  LAST-ACK
5)  TIME-WAIT   -->   ACK       -->  CLOSED
6)  CLOSED  
```
8. TCP порт – 16 битное число. Предположим, 2 находящихся в одной сети хоста устанавливают между собой соединения. Каким будет теоретическое максимальное число соединений, ограниченное только лишь параметрами L4, которое параллельно может установить клиент с одного IP адреса к серверу с одним IP адресом? Сколько соединений сможет обслужить сервер от одного клиента? А если клиентов больше одного?
```
Максимально число портов, которые может слушать сервер 65536, если клиент устанавливает соединение с одним
сервисом на каком-то определенном порту, то максимальное число соединений 65536 от одного клиента на один
открытй поорт сервера. Если клиент устанавливает соединения по всем возможным портам на сервере, то 65536
клиента * 65536 сервера = 4 294 967 296 соединений возможно между одним клиентом и сервером. А если клиентов
больше одного, то N * 65536^2
```
9. Может ли сложиться ситуация, при которой большое число соединений TCP на хосте находятся в состоянии TIME-WAIT? Если да, то является ли она хорошей или плохой? Подкрепите свой ответ пояснением той или иной оценки.
```
Может, ожидание потерявщихся пакетов 2*MSL=60 сек по умолчанию. Ситуация не очень хорошая
тк занимает свободные TCP порты. На высоконагруженном сервере можно уменьшить время ожидания
выставив net.ipv4.tcp_fin_timeout = 15 например.
```
10. Чем особенно плоха фрагментация UDP относительно фрагментации TCP?
```
Не будет повторной отправки пакета, я думаю.
```
11. Если бы вы строили систему удаленного сбора логов, то есть систему, в которой несколько хостов отправяют на центральный узел генерируемые приложениями логи (предположим, что логи – текстовая информация), какой протокол транспортного уровня вы выбрали бы и почему? Проверьте ваше предположение самостоятельно, узнав о стандартном протоколе syslog.
```
Если доставка текстовых логов, то TCP, тк для нас важно получить все записи журналов. А если бы собирал
метрики мониторинга то UDP, там небольшая потеря данных не критична. syslog умеет и по TCP и по UDP 
```
12. Сколько портов TCP находится в состоянии прослушивания на вашей виртуальной машине с Ubuntu, и каким процессам они принадлежат?
```
3 порта 111, 53, 22

root@vm1:~# ss -nlpt
State    Recv-Q   Send-Q      Local Address:Port       Peer Address:Port   Process
LISTEN   0        4096              0.0.0.0:111             0.0.0.0:*       users:(("rpcbind",pid=625,fd=4),("systemd",pid=1,fd=35))
LISTEN   0        4096        127.0.0.53%lo:53              0.0.0.0:*       users:(("systemd-resolve",pid=627,fd=13))
LISTEN   0        128               0.0.0.0:22              0.0.0.0:*       users:(("sshd",pid=885,fd=3))
LISTEN   0        4096                 [::]:111                [::]:*       users:(("rpcbind",pid=625,fd=6),("systemd",pid=1,fd=37)) # IPv6
LISTEN   0        128                  [::]:22                 [::]:*       users:(("sshd",pid=885,fd=4))                            # IPv6
root@vm1:~#
```
13. Какой ключ нужно добавить в tcpdump, чтобы он начал выводить не только заголовки, но и содержимое фреймов в текстовом виде? А в текстовом и шестнадцатиричном?
```
-A текст
-X HEX+TEXT
```
1.  Попробуйте собрать дамп трафика с помощью tcpdump на основном интерфейсе вашей виртуальной машины и посмотреть его через tshark или Wireshark (можно ограничить число пакетов -c 100). Встретились ли вам какие-то установленные флаги Internet Protocol (не флаги TCP, а флаги IP)?
```
Только Don' fragment, всего три бита идёт под флаги:
bit 0: Reserved; must be zero.[note 1]
bit 1: Don't Fragment (DF)
bit 2: More Fragments (MF)
```
Как на самом деле называется стандарт Ethernet, фреймы которого попали в ваш дамп?
```
Попали фреймы версии Ethernet II
Какой стандарт в дампе не нашел, но судя по выводу:

[ sander@iMac-Home ~ ]$ ifconfig en0
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=50b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV,CHANNEL_IO>
	ether 78:7b:8a:e1:b3:62
	inet 10.0.1.111 netmask 0xffffff00 broadcast 10.0.1.255
	inet6 fe80::1436:ba8e:cced:a403%en0 prefixlen 64 secured scopeid 0x4
	inet6 2001:470:28:b72::111 prefixlen 64
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect (1000baseT <full-duplex,flow-control>)
	status: active

media: 1000baseT - это стандарт IEEE 802.3ab (1000BASE-T, Gigabit Ethernet: 1 Гбит/с (125 Мбайт/с) по витой паре 5-й категории)
```
Можно ли где-то в дампе увидеть OUI?
```
Wireshark показывает во фрейме Ethernet:
в поле Address: RealtekU_12:35:02
```
