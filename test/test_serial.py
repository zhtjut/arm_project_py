'''

@author: Zxh
'''
'''
Created on 2016年6月14日

@author: Zxh
'''
import serial
from time import sleep
import binascii

serialport = serial.Serial("com1",9600,timeout=1)
# data="FE050000FF009835"
# data="0xFE0x050x000x000xFF0x000x980x35"
str="FE 05 00 07 00 00 68 04"
d=bytes.fromhex(str)
serialport.write(d)
while True:
    serialport.write(d)
#     serialport.write(data.encode(encoding='utf_8', errors='strict'))
    receive=serialport.readall()
    print(type(receive))
    print(receive)
#     ss=str(binascii.b2a_hex(receive))[2:-1] 
#     print(ss)
#     print(receive)
#     if receive=='':
#         print('kong')
#     else:
#         print(serialport.readall().decode(encoding='utf_8', errors='strict'))
serialport.close()
#     finally:
#         serialport.close()
