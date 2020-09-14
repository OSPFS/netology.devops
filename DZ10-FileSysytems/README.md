### Домашняя работа к занятию "3.5. Файловые системы"

2. Могут ли файлы, являющиеся жесткой ссылкой на один объект, иметь разные права доступа и владельца? Почему?
```
Нет т.к. данные о правах хранятся в inode, а жесткая ссылка лишь связывает inode с именем и каталогом
```
4. Используя fdisk, разбейте первый диск на 2 раздела: 2 Гб, оставшееся пространство.
5. Используя sfdisk, перенесите данную таблицу разделов на второй диск.
6. Соберите mdadm RAID1 на паре разделов 2 Гб.
7. Соберите mdadm RAID0 на второй паре маленьких разделов.
8. Создайте 2 независимых PV на получившихся md-устройствах.
9. Создайте общую volume-group на этих двух PV.
10. Создайте LV размером 100 Мб, указав его расположение на PV с RAID0.
11. Создайте mkfs.ext4 ФС на получившемся LV.
12. Смонтируйте этот раздел в любую директорию, например, /tmp/new.
13. Поместите туда тестовый файл, например wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz.
14. Прикрепите вывод lsblk
```
root@vagrant:/# lsblk
NAME                 MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sda                    8:0    0   64G  0 disk
├─sda1                 8:1    0  512M  0 part  /boot/efi
├─sda2                 8:2    0    1K  0 part
└─sda5                 8:5    0 63.5G  0 part
  ├─vgvagrant-root   253:0    0 62.6G  0 lvm   /
  └─vgvagrant-swap_1 253:1    0  980M  0 lvm   [SWAP]
sdb                    8:16   0  2.5G  0 disk
├─sdb1                 8:17   0    2G  0 part
│ └─md0                9:0    0    2G  0 raid1
└─sdb2                 8:18   0  511M  0 part
  └─md1                9:1    0 1018M  0 raid0
    └─VG00-LV--100   253:2    0  100M  0 lvm   /mnt/LV100
sdc                    8:32   0  2.5G  0 disk
├─sdc1                 8:33   0    2G  0 part
│ └─md0                9:0    0    2G  0 raid1
└─sdc2                 8:34   0  511M  0 part
  └─md1                9:1    0 1018M  0 raid0
    └─VG00-LV--100   253:2    0  100M  0 lvm   /mnt/LV100
root@vagrant:/#
```
16. Используя pvmove, переместите содержимое PV с RAID0 на RAID1.
```
root@vagrant:/mnt/LV100# lsblk
NAME                 MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sda                    8:0    0   64G  0 disk
├─sda1                 8:1    0  512M  0 part  /boot/efi
├─sda2                 8:2    0    1K  0 part
└─sda5                 8:5    0 63.5G  0 part
  ├─vgvagrant-root   253:0    0 62.6G  0 lvm   /
  └─vgvagrant-swap_1 253:1    0  980M  0 lvm   [SWAP]
sdb                    8:16   0  2.5G  0 disk
├─sdb1                 8:17   0    2G  0 part
│ └─md0                9:0    0    2G  0 raid1
│   └─VG00-LV--100   253:2    0  100M  0 lvm   /mnt/LV100
└─sdb2                 8:18   0  511M  0 part
  └─md1                9:1    0 1018M  0 raid0
sdc                    8:32   0  2.5G  0 disk
├─sdc1                 8:33   0    2G  0 part
│ └─md0                9:0    0    2G  0 raid1
│   └─VG00-LV--100   253:2    0  100M  0 lvm   /mnt/LV100
└─sdc2                 8:34   0  511M  0 part
  └─md1                9:1    0 1018M  0 raid0
```
17. Сделайте --fail на устройство в вашем RAID1 md.

18. Подтвердите выводом dmesg, что RAID1 работает в деградированном состоянии.
```
[ 5811.081731] md/raid1:md0: Disk failure on sdc1, disabling device.
               md/raid1:md0: Operation continuing on 1 devices.
```
19. Протестируйте целостность файла, несмотря на "сбойный" диск он должен продолжать быть доступен:
```
root@vagrant:/mnt/LV100# gzip -t /mnt/LV100/ls-lR.gz
root@vagrant:/mnt/LV100# echo $?
0
root@vagrant:/mnt/LV100#
```
