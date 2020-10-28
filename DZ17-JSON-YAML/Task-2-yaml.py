#!/usr/bin/env python3

import socket
import time
import yaml

# HOSTS = {'google.com': socket.gethostbyname('google.com'),
#          'drive.google.com': socket.gethostbyname('drive.google.com'),
#          'mail.google.com': socket.gethostbyname('mail.google.com')}

with open('hosts.yaml') as YFILE:
    HOSTS = yaml.safe_load(YFILE)

while True:    
    for SRV in HOSTS.keys():
        LAST_IP = HOSTS.get(SRV)
        CURRENT_IP = socket.gethostbyname(SRV)    
        if CURRENT_IP == LAST_IP:
            print(f'{SRV} - {CURRENT_IP}')
        else:
            print(f'[ERROR] {SRV} IP mismatch: {LAST_IP} - {CURRENT_IP}')
            HOSTS[SRV] = CURRENT_IP
            with open('hosts.yaml', 'w') as YFILE:
                yaml.dump(HOSTS, YFILE)           
    print()    
    time.sleep(5)
