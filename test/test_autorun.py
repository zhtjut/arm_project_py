'''
Created on 2016/06/20

@author: Zxh
'''
from indoor import Indoor
from outdoor import Outdoor
from control import Control
from parameter import Parameter
from autorun import auto_run_alogrithm
node0=Indoor('node0')
outdoor=Outdoor()
control=Control()
parameter=Parameter()
parameter.set_heating_start_lowest_temperature("20")
parameter.set_heating_stop_highest_temperature("30")
node0.set_temperature("15")
auto=auto_run_alogrithm(node0,outdoor,control,parameter)
auto.heating_control()
print auto.control.get_heating()
print auto.get_control().build_json()

