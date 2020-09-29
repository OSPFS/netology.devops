#!/usr/bin/env bash
echo -n > access.log
webs=(nic.ru yandex.ru mail.russs)
count=0

while ((1==1))
do
  for i in ${webs[@]}
  do
    curl -m 2 -s -o /dev/null http://$i     
      if (($?!=0)); then
         echo "$(date) $i is down" | tee access.log
         exit
      fi
  done
sleep 2
done
