#!/usr/bin/env python3

import os

def child():
    print('\nA new child ',  os.getpid())
    os._exit(0)  

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            pids = (os.getpid(), newpid)
            print("parent: %d, child: %d\n" % pids)
            print("q for quit / c for new fork")
        if input() == 'c': 
            continue
        else:
            break

parent()

