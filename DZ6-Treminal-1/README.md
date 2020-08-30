* Домашняя работа к занятию "3.1. Работа в терминале, лекция 1"

5,7. Q: Какие ресурсы выделены по-умолчанию?

```
root@vagrant:~# cat /proc/cpuinfo
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 158
model name	: Intel(R) Core(TM) i5-7500 CPU @ 3.40GHz
stepping	: 9
cpu MHz		: 3408.000
cache size	: 6144 KB
physical id	: 0
siblings	: 1
core id		: 0
cpu cores	: 1
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 22
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq monitor ssse3 cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single pti fsgsbase avx2 invpcid rdseed clflushopt md_clear flush_l1d
bugs		: cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit srbds
bogomips	: 6816.00
clflush size	: 64
cache_alignment	: 64
address sizes	: 39 bits physical, 48 bits virtual
power management:

root@vagrant:~# lsblk
NAME                 MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                    8:0    0   64G  0 disk
├─sda1                 8:1    0  512M  0 part /boot/efi
├─sda2                 8:2    0    1K  0 part
└─sda5                 8:5    0 63.5G  0 part
  ├─vgvagrant-root   253:0    0 62.6G  0 lvm  /
  └─vgvagrant-swap_1 253:1    0  980M  0 lvm  [SWAP]

root@vagrant:~# free -h
              total        used        free      shared  buff/cache   available
Mem:          981Mi        86Mi       480Mi       0.0Ki       414Mi       744Mi
Swap:         979Mi          0B       979Mi
```
6. Q: Как добавить оперативной памяти или ресурсов процессора виртуальной машине?
```
Vagrant.configure("2") do |config|
    config.vm.box = "bento/ubuntu-20.04"

    config.vm.provider "virtualbox" do |v|
        v.memory = 4096
        v.cpus = 2
    end
end
```
8. Q: какой переменной можно задать длину журнала history, и на какой строчке manual это описывается?

```
560        HISTSIZE
561               The number of commands to remember in the command history (see HISTORY below).  The default value is 500.
```

Q: что делает директива ignoreboth в bash?
```
Если переменная HISTCONTROL равна inoreboth, то строки начинающиеся с пробела и стоки совпадающие с последней введенной строкой в историю не попадают
```
9. Q: В каких сценариях использования применимы скобки {} и на какой строчке man bash это описано?
```
    207        { list; }
    208               list is simply executed in the current shell environment.  list must be terminated with a newline or semicolon.  This is known as a group command.  The return  status  is  the  exit
    209               status of list.  Note that unlike the metacharacters ( and ), { and } are reserved words and must occur where a reserved word is permitted to be recognized.  Since they do not cause
    210               a word break, they must be separated from list by whitespace or another shell metacharacter.

{ список; } - использется в цикле while, функциях, при замене выражений (например a{d,c,b}e заменяется на 'ade ace abe')
```
10. Q: Основываясь на предыдущем вопросе, как создать однократным вызовом touch 100000 файлов?

```
vagrant@vagrant:~/test$ ls -lah
total 8.0K
drwxrwxr-x 2 vagrant vagrant 4.0K Aug 30 07:49 .
drwxr-xr-x 5 vagrant vagrant 4.0K Aug 30 07:49 ..
vagrant@vagrant:~/test$ touch my_file{1..100000}
vagrant@vagrant:~/test$ ls -lah my_f*|wc -l
100000
vagrant@vagrant:~/test$ ls
my_file1       my_file15999  my_file21999  my_file28     my_file34     my_file40     my_file460    my_file520    my_file5800   my_file6400   my_file7000   my_file76000  my_file82000  my_file88001  my_file94001
my_file10      my_file16     my_file22     my_file280    my_file340    my_file400    my_file4600   my_file5200   my_file58000  my_file64000  my_file70000  my_file76001  my_file82001  my_file88002  my_file94002
```
Q:  А получилось ли создать 300000?
```
vagrant@vagrant:~/test$ rm -rf *
vagrant@vagrant:~/test$ touch my_file{1..300000}
-bash: /usr/bin/touch: Argument list too long
```
11. Q: В man bash поищите по /\[\[ (keyword). Что делает конструкция [[ -d /tmp ]]
```
Что делает конструкция [[ -d /tmp ]] в man bash не нашел, по информации из man test конструкция [[ -d /tmp ]] определяет существует ли файл /tmp и является ли он директорией
```
12. Q: Основываясь на знаниях о просмотре текущих (например, PATH) и установке новых переменных; командах, которые мы рассматривали, добейтесь в выводе type -a bash в виртуальной машине наличия первым пунктом в списке:
```
bash is /tmp/new_path_directory/bash
bash is /usr/local/bin/bash
bash is /bin/bash
```
Answer: 
```
vagrant@vagrant:/$ type -a bash
bash is /usr/bin/bash
bash is /bin/bash

vagrant@vagrant:/$ mkdir /tmp/new_path_directory/
vagrant@vagrant:/$ export PATH=/tmp/new_path_directory/:$PATH
vagrant@vagrant:/$ ln -s /usr/bin/bash /tmp/new_path_directory/bash
vagrant@vagrant:~$ sudo ln -s /usr/bin/bash /usr/local/bin/bash

vagrant@vagrant:~$ type -a bash
bash is /tmp/new_path_directory/bash
bash is /usr/local/bin/bash
bash is /usr/bin/bash
bash is /bin/bash
```

13. Q: Чем отличается планирование команд с помощью batch и at?

```
at - запускает команлы в указанное время, а batch когда средняя загрузка системы (load averege) падает ниже 1.5
```
