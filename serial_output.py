'''

@author: Zxh
'''
import serial
from time import sleep
import binascii

def println(value):
    print value

serialport = serial.Serial("com6",9600,timeout=2)

def send_command(data):
    data=bytes(bytearray.fromhex(data))
    serialport.write(data)
#     print time.time()
    while serialport.inWaiting()>0:
        pass
    print 'output correct'
    recv=serialport.readline()
    recv=binascii.b2a_hex(recv)
    return recv
    # sleep(0.03)


def query_all_state(Query):
    recv=send_command(Query)
    return recv
    
