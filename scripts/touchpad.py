#!/usr/bin/env python2
import os, subprocess

def synclient(source):   
    statefile = '/tmp/synclient.tmp'

    if not os.path.exists(statefile):
        os.system("synclient -l > %s" % statefile)
   
    state = open(statefile,'rb')

    for line in state:
        for word in line.split():
            if word == source:
                setting = line.split()
                if setting[2] == "0":
                    os.system("synclient %s=1" % setting[0])
                elif setting[2] == "1":
                    os.system("synclient %s=0" % setting[0])
    state.close()
    os.system("rm %s" % statefile)
    os.system("synclient -l > %s" % statefile)                
                



    
synclient("TouchpadOff")