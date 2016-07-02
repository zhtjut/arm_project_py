'''

@author: Zxh
'''
from time import sleep, ctime
import threading

x=1
def music():
    global x
    while x<40:
        print "I was listening to music. %s" %ctime()
        x+=1
        sleep(1)
        print x
    

def move():
    global x,t2
    while x!=30:
        t2.stop()
if __name__ == '__main__':
    global t2
    t2=threading.Thread(target=music)
    t1=threading.Thread(target=move)
    t1.start()
    t2.start()
    print "all over %s" %ctime()
    
    