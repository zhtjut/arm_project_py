'''
Created on 2016/06/20

@author: Zxh
'''
from indoor import Indoor
from outdoor import Outdoor
from control import Control
from parameter import Parameter
from autorun import autorun_main
node0=Indoor('node0')
outdoor=Outdoor()
control=Control()
parameter=Parameter()

autorun_main(node0,outdoor,control,parameter)