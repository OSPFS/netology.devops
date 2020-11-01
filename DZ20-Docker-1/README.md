#### Домашняя работа к занятию "5.3. Контейнеризация на примере Docker"

* Задача 1

```
По задаче 1, думаю всё можно запустить в докере, но возможны разные варианты.
```

* Задача 2

https://hub.docker.com/repository/docker/kundulun/netology-apache

* Задача 3

```
docker run -v /Users/sander/git/Netology/netology.devops/DZ20-Docker-1/info:/share/info --name centos -dt centos
docker exec -it centos bash
[root@23494dbbed7a /]# cd /share/info/
[root@23494dbbed7a info]# ls
[root@23494dbbed7a info]# echo sdsaf >test.txt
[root@23494dbbed7a info]# exit

docker run -v /Users/sander/git/Netology/netology.devops/DZ20-Docker-1/info:/info --name debian -dt debian:latest
docker exec -it debian bash
root@7aaf24452d75:/# ls -lah /info/
total 12K
drwxr-xr-x 4 root root  128 Nov  1 07:49 .
drwxr-xr-x 1 root root 4.0K Nov  1 07:52 ..
-rw-r--r-- 1 root root    7 Nov  1 07:49 ddd.txt
-rw-r--r-- 1 root root    6 Nov  1 07:47 test.txt
root@7aaf24452d75:/info# cat ddd.txt
sffsdsa
root@7aaf24452d75:/info# cat test.txt
sdsaf
sffsdsaroot@7aaf24452d75:/info# exit
```
