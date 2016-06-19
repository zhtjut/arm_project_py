'''
Created on 2016年6月19日

@author: Zxh
'''
from indoor import Indoor
from outdoor import Outdoor
from control import Control
from parameter import Parameter
from currenttime import get_current_hour, get_current_month


now_time="9"
temperature_set_temp0="0"
temperature_set_temp1="1"
temperature_set_temp2="2"
side_wait_time="0"

def init():
    global node0,outdoor,control,parameter
    node0=Indoor('node0')
    outdoor=Outdoor
    control=Control
    parameter=Parameter
    

#indoor temperature humidity, light
def roof_vent_control():
    if outdoor.bad_weather=="true":
        control.set_roof_vent_north("off")
        control.set_roof_vent_south("off")
    else:
        if now_time >= parameter.time1 and now_time < parameter.time2:
            temperature_set_temp0=parameter.temperature1
        elif now_time >= parameter.time2 and now_time < parameter.time3:
            temperature_set_temp0=parameter.temperature2
        elif now_time >= parameter.time3 and now_time < parameter.time4:
            temperature_set_temp0=parameter.temperature3
        else:
            temperature_set_temp0=parameter.temperature4  
        
        #humidity influence on temperature
        if node0.get_humidity()<=(parameter.expect_humidity-5-parameter.humidity_influence_range_of_air_temperature):
            temperature_set_temp1=temperature_set_temp0+parameter.low_humidity_influence_on_air_temperature
        elif node0.get_humidity()<=(parameter.expect_humidity-5):
            tmpt=(parameter.expect_humidity-5-node0.get_humidity())*parameter.low_humidity_influence_on_air_temperature/parameter.humidity_influence_range_of_air_temperature
            temperature_set_temp1=temperature_set_temp0+tmpt
        elif node0.get_humidity()>=(parameter.expect_humidity+5):
            tmpt=(node0.get_humidity()-parameter.expect_humidity-5)*parameter.high_humidity_influence_on_air_temperature/(100-5-parameter.expect_humidity)
            temperature_set_temp1=temperature_set_temp0+tmpt
        else:
            temperature_set_temp1=temperature_set_temp0
            
        #light influence on temperature
        if outdoor.radiation<parameter.expect_light:
            temperature_set_temp2=temperature_set_temp1
        else:
            temperature_set_temp2=temperature_set_temp1-parameter.light_influence_on_air_temperature_slope*(outdoor.radiation-parameter.expect_light)
        
        if temperature_set_temp2>(temperature_set_temp1+parameter.low_light_influence_on_temperature):
            temperature_set_temp2=temperature_set_temp1+parameter.low_light_influence_on_temperature
        elif temperature_set_temp2<(temperature_set_temp1-parameter.high_light_influence_on_temperature):
            temperature_set_temp2=temperature_set_temp1-parameter.high_light_influence_on_temperature
            
        if temperature_set_temp2<"0":
            temperature_set_temp2="0"
        
        if outdoor.temperature<=parameter.frost_temperature:
            control.set_roof_vent_north("off")
            control.set_roof_vent_south("off")
        elif outdoor.temperature<=parameter.indoor_temperature_lower_limit:    
            #small angle  小角度
            control.set_roof_vent_north("on")
            control.set_roof_vent_south("on")
        elif outdoor.temperature<=temperature_set_temp2:
            #open all  半开
            control.set_roof_vent_north("on")
            control.set_roof_vent_south("on")
        else:
            #  全开
            control.set_roof_vent_north("on")
            control.set_roof_vent_south("on")
        
def get_side_wait_time():
    if node0.temperature>(temperature_set_temp2+parameter.temperature_to_open_side):
        if side_wait_time<parameter.wait_time_to_open_side:
            side_wait_time +=1
        
def side_vent_control():
    if outdoor.bad_weather=="true":
        control.set_side_vent("off")
    
    elif control.__cooling_pad=="on":
        control.set_side_vent("on")
    elif control.__roof_vent_north=="on" and control.__roof_vent_south=="on":
        if side_wait_time<parameter.wait_time_to_open_side:
            control.set_side_vent("off")
        elif side_wait_time>parameter.wait_time_to_open_side and side_wait_time<2*parameter.wait_time_to_open_side:
            #应该是半开，需要修改
            control.set_side_vent("on")
        else:
            control.set_side_vent("on")
    else:
        control.set_side_vent("off")
        
def shade_screen_out_control():
    if outdoor.bad_weather=="true":
        control.set_shade_screen_out("off")
    elif outdoor.radiation>parameter.upper_limit_light_to_open_shade_screen_out:
        control.set_shade_screen_out("on")
    else:
        control.set_shade_screen_out("off")

def shade_screen_in_control():
    if control.__thermal_screen=="on":
        control.set_shade_screen_in("on")
    elif outdoor.radiation>parameter.upper_limit_light_to_open_shade_screen_in:
        control.set_shade_screen_in("off")
    else:
        control.set_shade_screen_in("on")
        
def thermal_screen_control():
    if outdoor.bad_weather=="true":
        control.set_thermal_screen("off")
    elif control.__fogging=="on":
        control.set_thermal_screen("off")
    else:
        current_hour=get_current_hour()
        current_month=get_current_month()
        if current_month>parameter.month_to_open_thermal_screen and current_month<parameter.month_to_close_thermal_screen:
            if current_hour>parameter.time_to_open_thermal_screen and current_hour<parameter.time_to_close_thermal_screen:
                control.set_thermal_screen("off")    #展开
        else:
            control.set_thermal_screen("on") #折起
         
       
