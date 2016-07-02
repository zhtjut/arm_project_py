'''
@author: Zxh
'''
import threading
result=None

def calc_sth(args=""):
  global result
  #do some calculating
  result=12345
  print 'hehe'
  print args

t=threading.Thread(target=calc_sth())
# t.start()
# t.join()
print('Got result:',result)

