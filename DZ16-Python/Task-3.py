#!/usr/bin/env python3

import socket
import os.path

HOSTS = ('drive.google.com', 'mail.google.com', 'google.com')

for HOST in HOSTS:
    IP = socket.gethostbyname('mail.google.com')
    LOG_FILE = open("host.log","r")
    OLD_IP = LOG_FILE.read()
    LOG_FILE.close()
    
    if IP == OLD_IP:
        print(f'mail.google.com - {IP}')
    else:
        print(f'[ERROR] mail.google.com IP mismatch: {OLD_IP} - {IP}')
        LOG_FILE = open("host.log","w")
        LOG_FILE.write(IP)
    