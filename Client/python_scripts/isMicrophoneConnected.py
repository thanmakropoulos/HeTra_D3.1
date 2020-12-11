import ctypes
from ctypes import *
import sys

winmm= windll.winmm

r = winmm.waveInGetNumDevs()

if r == 0:
    print(0)
    sys.stdout.flush()
elif r != 0:
    print(1)
    sys.stdout.flush()