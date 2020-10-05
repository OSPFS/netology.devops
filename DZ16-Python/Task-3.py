#!/usr/bin/env python3

import socket
import os.path

LOG_FILE = open("host.log","r")
IP = socket.gethostbyname('mail.google.com')
OLD_IP = LOG_FILE.read()

print(f'Old IP: {OLD_IP}')
print(f'Current IP: {IP}')

LOG_FILE.close()

if IP == OLD_IP:
    print(f'mail.google.com - {IP}')
else:
    print(f'[ERROR] mail.google.com IP mismatch: {OLD_IP} - {IP}')
    LOG_FILE = open("host.log","w")
    LOG_FILE.write(IP)
