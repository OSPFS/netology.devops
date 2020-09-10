### Домашняя работа к занятию "3.3. Операционные системы, лекция 1"

1. Какой системный вызов делает команда cd? В прошлом ДЗ мы выяснили, что cd не является самостоятельной программой, это shell builtin, поэтому запустить strace непосредственно на cd не получится. Тем не менее, вы можете запустить strace на /bin/bash -c 'cd /tmp'. В этом случае вы увидите полный список системных вызовов, которые делает сам bash при старте. Вам нужно найти тот единственный, который относится именно к cd.
```
chdir("/tmp")
```
2. Используя strace выясните, где находится база данных file на основании которой она делает свои догадки.
```
openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3
```
3. Предположим, приложение пишет лог в текстовый файл. Этот файл оказался удален (deleted в lsof), однако возможности сигналом сказать приложению переоткрыть файлы или просто перезапустить приложение – нет. Так как приложение продолжает писать в удаленный файл, место на диске постепенно заканчивается. Основываясь на знаниях о перенаправлении потоков предложите способ обнуления открытого удаленного файла (чтобы освободить место на файловой системе).
```
Сомневаюсь, но может так:

cd /proc/PNUM/fd
echo -n >4 
```
4. Занимают ли зомби-процессы какие-то ресурсы в ОС (CPU, RAM, IO)?
```
нет, только записи в таблице процессов
```
5. В iovisor BCC есть утилита opensnoop. На какие файлы вы увидели вызов open за первую секунду работы утилиты?
```
root@vagrant:/usr/share/bcc/tools# /usr/share/bcc/tools/opensnoop
PID    COMM               FD ERR PATH
1013   vminfo              6   0 /var/run/utmp
662    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
662    dbus-daemon        18   0 /usr/share/dbus-1/system-services
662    dbus-daemon        -1   2 /lib/dbus-1/system-services
3547   opensnoop          -1   2 /usr/lib/python2.7/encodings/ascii.x86_64-linux-gnu.so
3547   opensnoop          -1   2 /usr/lib/python2.7/encodings/ascii.so
3547   opensnoop          -1   2 /usr/lib/python2.7/encodings/asciimodule.so
3547   opensnoop          12   0 /usr/lib/python2.7/encodings/ascii.py
3547   opensnoop          13   0 /usr/lib/python2.7/encodings/ascii.pyc
679    irqbalance          6   0 /proc/interrupts
679    irqbalance          6   0 /proc/stat
679    irqbalance          6   0 /proc/irq/20/smp_affinity
679    irqbalance          6   0 /proc/irq/0/smp_affinity
679    irqbalance          6   0 /proc/irq/1/smp_affinity
679    irqbalance          6   0 /proc/irq/8/smp_affinity
679    irqbalance          6   0 /proc/irq/12/smp_affinity
679    irqbalance          6   0 /proc/irq/14/smp_affinity
679    irqbalance          6   0 /proc/irq/15/smp_affinity
1013   vminfo              6   0 /var/run/utmp
662    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
662    dbus-daemon        18   0 /usr/share/dbus-1/system-services
662    dbus-daemon        -1   2 /lib/dbus-1/system-services
1013   vminfo              6   0 /var/run/utmp
662    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
662    dbus-daemon        18   0 /usr/share/dbus-1/system-services
662    dbus-daemon        -1   2 /lib/dbus-1/system-services
679    irqbalance          6   0 /proc/interrupts
679    irqbalance          6   0 /proc/stat
679    irqbalance          6   0 /proc/irq/20/smp_affinity
679    irqbalance          6   0 /proc/irq/0/smp_affinity
679    irqbalance          6   0 /proc/irq/1/smp_affinity
679    irqbalance          6   0 /proc/irq/8/smp_affinity
679    irqbalance          6   0 /proc/irq/12/smp_affinity
679    irqbalance          6   0 /proc/irq/14/smp_affinity
679    irqbalance          6   0 /proc/irq/15/smp_affinity
1013   vminfo              6   0 /var/run/utmp
662    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
662    dbus-daemon        18   0 /usr/share/dbus-1/system-services
662    dbus-daemon        -1   2 /lib/dbus-1/system-services
1013   vminfo              6   0 /var/run/utmp
662    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
662    dbus-daemon        18   0 /usr/share/dbus-1/system-services
662    dbus-daemon        -1   2 /lib/dbus-1/system-services
679    irqbalance          6   0 /proc/interrupts
679    irqbalance          6   0 /proc/stat
679    irqbalance          6   0 /proc/irq/20/smp_affinity
679    irqbalance          6   0 /proc/irq/0/smp_affinity
679    irqbalance          6   0 /proc/irq/1/smp_affinity
679    irqbalance          6   0 /proc/irq/8/smp_affinity
679    irqbalance          6   0 /proc/irq/12/smp_affinity
679    irqbalance          6   0 /proc/irq/14/smp_affinity
679    irqbalance          6   0 /proc/irq/15/smp_affinity
1484   vi                 -1   2 /home/vagrant/.viminfo
1484   vi                  3   0 /home/vagrant/.viminfo
1013   vminfo              6   0 /var/run/utmp
662    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
662    dbus-daemon        18   0 /usr/share/dbus-1/system-services
662    dbus-daemon        -1   2 /lib/dbus-1/system-services
1013   vminfo              6   0 /var/run/utmp
662    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
662    dbus-daemon        18   0 /usr/share/dbus-1/system-services
662    dbus-daemon        -1   2 /lib/dbus-1/system-services
```
6. Какой системный вызов использует uname -a? Приведите цитату из man по этому системному вызову, где описывается альтернативное местоположение в /proc, где можно узнать версию ядра и релиз ОС.
```
Вызов uname, так же можно посмотреть в /proc/sys/kernel/

vagrant@vagrant:/proc/sys/kernel$ cat osrelease
4.15.0-112-generic
vagrant@vagrant:/proc/sys/kernel$ cat version
#113-Ubuntu SMP Thu Jul 9 23:41:39 UTC 2020
```
7. Чем отличается последовательность команд через ; и через && в bash?
```
Через ; бдут выполняться последовательно не смотря на ошибку предыдущей команды, 
а через && команда выполнится только если предыдущая завершилась успешно. 
```
Есть ли смысл использовать в bash &&, если применить set -e?
```
Так как set -e подразумевает выход из скрипта при выполнении любой команды с не 0-м кодом возврата, то скорее всего нет.
Конструкция test -d /tmp/some_dir && echo Hi выдаст только код возврата 0 от последней команды
```
8. Из каких опций состоит режим bash set -euxo pipefail и почему его хорошо было бы использовать в сценариях?
```
Не понял только -o pipefile
```
9.  Используя -o stat для ps, определите, какой наиболее часто встречающийся статус у процессов в системе. В man ps ознакомьтесь (/PROCESS STATE CODES) что значат дополнительные к основной заглавной буквы статуса процессов. Его можно не учитывать при расчете (считать S, Ss или Ssl равнозначными).
```
vagrant@vagrant:~$ ps -axf -o stat|grep -c S
55
vagrant@vagrant:~$ ps -axf -o stat|grep -c I
48
Больше всего в состоянии sleep и idle kernel threads (появилось в ядре 4.14)
```