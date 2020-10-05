#!/usr/bin/env python3

import socket
import time

HOSTS = {}
HOSTS['google.com'] = socket.gethostbyname('google.com')
HOSTS['drive.google.com'] = socket.gethostbyname('drive.google.com')
HOSTS['mail.google.com'] = socket.gethostbyname('mail.google.com')

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
    time.sleep( 5 )
