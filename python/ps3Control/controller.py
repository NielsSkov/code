#!/usr/bin/env python

import os
import sys
import subprocess
import re
import socket
import time

proc = subprocess.Popen(['xboxdrv', '--detach-kernel-driver'],stdout=subprocess.PIPE)

searching = 0

dataClean = []

HOST = '25.42.123.26'
PORT = 9000

while True:
    while True:
        try:
            boatServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            boatServer.connect((HOST,PORT))
            break
        except:
            print 'attempting to connect to server'
            time.sleep(1)

    for line in iter(proc.stdout.readline,''):
        data = line.rstrip()

        #dataBin = 0|(ord('$')<<(21*8))

        if data.startswith('X1:'):  #this is a beautiful regular expression which extracts
                                    #the values of the button-presses, good luck! :D
            buttonValues = re.match('(?:X1\:\s*)(\d+)(?:\s*Y1\:\s*)(\d+)(?:\s*X2\:\s*)(\d+)(?:\s*Y2\:\s*)(\d+)(?:\s*du\:\s*)(\d+)(?:\s*dd\:\s*)(\d+)(?:\s*dl\:\s*)(\d+)(?:\s*dr\:\s*)(\d+)(?:\s*select\:\s*)(\d+)(?:\s*ps\:\s*)(\d+)(?:\s*start\:\s*)(\d+)(?:\s*L3\:\s*)(\d+)(?:\s*R3\:\s*)(\d+)(?:\s*\/\\\:\s*)(\d+)(?:\s*O\:\s*)(\d+)(?:\s*X\:\s*)(\d+)(?:\s*\[\]\:\s*)(\d+)(?:\s*L1\:\s*)(\d+)(?:\s*R1\:\s*)(\d+)(?:\s*L2\:\s*)(\d+)(?:\s*R2\:\s*)(\d+)',data)
          
            dataClean = ['$']
            try:
                for j in range(1,22):
                    dataInt = int(buttonValues.group(j))
                    print dataInt,
                    dataClean.append(chr(dataInt))
                    #dataBin = dataBin|(dataInt<<((21-j)*8))
                    #dataClean = str(unichar(dataInt))

                dataClean=''.join(dataClean)
            except:
                print 'failed to read'

            print ''
            print buttonValues.group()
            
            try:
                #print bin(dataClean)[2:].zfill(8*21+6)
                boatServer.send(dataClean)
            except:
                print 'failed to send'
                break

            if searching == 1:
                print ''
                searching = 0
        else:
            if searching == 0:
                sys.stdout.write('searching ...')
                sys.stdout.flush()
                searching = 1
            else:
                sys.stdout.write('.')
                sys.stdout.flush()

proc.kill()


