#!/usr/bin/env python3

import socket
import time
import json


HOSTS = {'google.com': socket.gethostbyname('google.com'),
         'drive.google.com': socket.gethostbyname('drive.google.com'),
         'mail.google.com': socket.gethostbyname('mail.google.com')}

while True:    
    for SRV in HOSTS.keys():
        LAST_IP = HOSTS.get(SRV)
        CURRENT_IP = socket.gethostbyname(SRV)    
        if CURRENT_IP == LAST_IP:
            print(f'{SRV} - {CURRENT_IP}')
        else:
            print(f'[ERROR] {SRV} IP mismatch: {LAST_IP} - {CURRENT_IP}')
            HOSTS[SRV] = CURRENT_IP
    print()
    time.sleep(5)
