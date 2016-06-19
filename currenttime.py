import time

local_time=time.localtime(time.time())

def get_current_time():
    #linux time String
#     return time.strftime("%d %h %Y %H:%M:%S" , time.localtime(time.time()))

    #windows time String
    return time.strftime("%Y-%m-%d %X" , local_time) 
#     return "2016-16-16 12:21"
def get_current_month():
    return "%s" %(local_time[1])

def get_current_hour():
    return "%s" % (local_time[3])
if __name__ == '__main__':
    print get_current_time()
    print time.time()
    print time.localtime(time.time())
    print get_current_month()
    print get_current_hour()