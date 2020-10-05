#!/usr/bin/env python3

import socket
import time

LAST = socket.gethostbyname('mail.google.com')

while True:
    HOST = socket.gethostbyname('mail.google.com')    
    if HOST == LAST:
        print(f'mail.google.com - {HOST}')
    else:
        print(f'[ERROR] {HOST} IP mismatch: {LAST} - {HOST}')        
    LAST = HOST
    time.sleep( 5 )


