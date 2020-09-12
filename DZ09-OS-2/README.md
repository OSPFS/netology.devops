### Домашняя работа к занятию "3.4. Операционные системы, лекция 2"

1. Используя знания из лекции по systemd, создайте самостоятельно простой unit-файл для node_exporter
```
root@vagrant:/etc/systemd/system# cat exporter.service
[Unit]
Description=Node Exporter
After=network.target

[Service]
EnvironmentFile=-/etc/default/exporter
Type=simple
ExecStart=/usr/local/bin/node_exporter $OPTIONS

[Install]
WantedBy=multi-user.target
```
2. Ознакомьтесь с опциями node_exporter и выводом /metrics по-умолчанию. Приведите несколько опций, которые вы бы выбрали для базового мониторинга хоста по CPU, памяти, диску и сети.
```
cpu diskstats meminfo netdev netstat
```
3. Установите в свою виртуальную машину Netdata.
```
Спасибо за наводку, отличный инструмент.
```
4. Можно ли по выводу dmesg понять, осознает ли ОС, что загружена не на настоящем оборудовании, а на системе виртуализации?
```
[    2.365393] systemd[1]: Detected virtualization oracle.
или
[    7.657427] systemd[1]: Detected virtualization kvm.
```
5. 
```
fs.nr_open - Максимальное количество файловых дескрипторов, которые может выделить процесс

sysctl -a|grep fs.nr_open
fs.nr_open = 1048576

ulimit -n

-n	the maximum number of open file descriptors
```
6. Запустите любой долгоживущий процесс (не ls, который отработает мгновенно, а, например, sleep 1h) в отдельном неймспейсе процессов; покажите, что ваш процесс работает под PID 1 через nsenter.
```
root@vagrant:~# lsns
        NS TYPE   NPROCS   PID USER            COMMAND
4026531835 cgroup    111     1 root            /sbin/init
4026531836 pid       110     1 root            /sbin/init
4026531837 user      111     1 root            /sbin/init
4026531838 uts       109     1 root            /sbin/init
4026531839 ipc       111     1 root            /sbin/init
4026531840 mnt        99     1 root            /sbin/init
4026531860 mnt         1    21 root            kdevtmpfs
4026531992 net       111     1 root            /sbin/init
4026532162 mnt         1   460 root            /lib/systemd/systemd-udevd
4026532163 uts         1   460 root            /lib/systemd/systemd-udevd
4026532164 mnt         1   466 systemd-network /lib/systemd/systemd-networkd
4026532183 mnt         1   643 systemd-resolve /lib/systemd/systemd-resolved
4026532184 mnt         4   873 netdata         /usr/sbin/netdata -D
4026532185 mnt         2  1862 root            unshare -f --pid --mount-proc sleep 1h
4026532186 pid         1  1863 root            sleep 1h
4026532249 mnt         1   688 root            /usr/sbin/irqbalance --foreground
4026532250 mnt         1   696 root            /lib/systemd/systemd-logind
4026532251 uts         1   696 root            /lib/systemd/systemd-logind
root@vagrant:~# nsenter --target 1863 --pid --mount
root@vagrant:/# ps ax
    PID TTY      STAT   TIME COMMAND
      1 pts/0    S+     0:00 sleep 1h
     13 pts/1    S      0:00 -bash
     22 pts/1    R+     0:00 ps ax
root@vagrant:/#
```
7. Форк бомба, функция вызывающая сама себя
```
[ 5125.661907] cgroup: fork rejected by pids controller in /user.slice/user-1000.slice/session-6.scope
[ 5135.143076] cgroup: fork rejected by pids controller in /user.slice/user-1000.slice/session-3.scope

cat /sys/fs/cgroup/pids/user.slice/user-1000.slice/pids.max
5020

echo 100500 > /sys/fs/cgroup/pids/user.slice/user-1000.slice/pids.max
```
