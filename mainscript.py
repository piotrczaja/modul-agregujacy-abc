#!/usr/bin/python3

from datetime import datetime

from lib.modula.modula import modulA
from lib.modulb.modulb import modulB
from lib.modulc.modulc import modulC

now = datetime.now()

def timestampwykonania():
    godzina = now.strftime("%H:%M:%S")
    data = now.strftime("%m.%d.%Y")
    print("Sktypt wykonany: ", data, " o godzinie ", godzina)

modulA()
modulB()
modulC()
timestampwykonania()


