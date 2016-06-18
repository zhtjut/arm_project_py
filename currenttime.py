

import time
def get_current_time():
    #linux time String
#     return time.strftime("%d %h %Y %H:%M:%S" , time.localtime(time.time()))

    #windows time String
    return time.strftime("%Y-%m-%d %X" , time.localtime(time.time())) 
#     return "2016-16-16 12:21"
if __name__ == '__main__':
    print get_current_time()