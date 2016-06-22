'''

@author: Zxh
'''
from scheduler import Scheduler
# print "_Control__"+'co2_upper_limit'
# p=Parameter()
# print getattr(p,'_Parameter__'+'co2_upper_limit')
# p.set_shade_screen_out_time("5")
# wait_and_stop("shade_screen_out",p.get_shade_screen_out_time(),"half")
# sleep(5)
# print 'b'
x=1;
def test():
    global x
    x+=1
    print x

def hehe():
    global x
    if (x==10):
        print 'geme over'
        x=0;
        print x
    else:
        print 'wait'
s1=Scheduler(2,test)
s2=Scheduler(1,hehe)
x=5
while 1:
    s1.start()
    s2.start()
s1.stop()
s2.start()   
