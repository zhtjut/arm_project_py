'''

@author: Zxh
'''
import serial
from time import sleep
import binascii
import threading
a=1
serialport = serial.Serial("com6",9600,timeout=2)
mutex=threading.Lock()
def send_command(data):
    global mutex,a
    data=bytes(bytearray.fromhex(data))
    if mutex.acquire():
        serialport.write(data)
        while serialport.inWaiting()>0:
            pass
        print 'output correct  '+str(a)
        recv=serialport.readline()
        recv=binascii.b2a_hex(recv)
        a=a+1
        mutex.release()
    sleep(0.03)
    return recv

def query_all_state(Query):
    recv=send_command(Query)
    return recv
    
