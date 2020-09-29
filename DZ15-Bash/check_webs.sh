#!/usr/bin/env bash
echo -n > access.log
webs=(nic.ru yandex.ru mail.ru)
count=0

while (($count<5))
do
  for i in ${webs[@]}
  do
    curl -m 2 -s -o /dev/null http://$i     
      if (($?==0)); then
         echo "$(date) $i Ok." | tee -a access.log
      fi
  done
  let "count+=1"
done
