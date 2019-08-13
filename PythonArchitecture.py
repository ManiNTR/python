#Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS
import struct
print("The python shell run on ",struct.calcsize("P")*8," bit")
