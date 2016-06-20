'''
Created on 2016年6月19日

@author: Zxh
'''
from indoor import Indoor
from outdoor import Outdoor
from control import Control
from parameter import Parameter
from currenttime import get_current_hour, get_current_month,get_time,get_current_time


now_time="9"
temperature_set_temp0="0"
temperature_set_temp1="1"
temperature_set_temp2="2"
side_wait_time="0"

lighting_open_time=0
lighting_open_time2=0
lighting_stop_time=0
lighting_stop_time2=0
lighting_stop_time3=0

def init():
    global node0,outdoor,control,parameter
    node0=Indoor('node0')
    outdoor=Outdoor()
    control=Control()
    parameter=Parameter()
    

#indoor temperature humidity, light
def roof_vent_control():
    if outdoor.get_bad_weather()=="true":
        control.set_roof_vent_north("off")
        control.set_roof_vent_south("off")
    else:
        if now_time >= parameter.get_time_1() and now_time < parameter.get_time_2():
            temperature_set_temp0=parameter.get_temperature_1()
        elif now_time >= parameter.get_time_2() and now_time < parameter.get_time_3():
            temperature_set_temp0=parameter.get_temperature2
        elif now_time >= parameter.get_time_3() and now_time < parameter.get_time_4():
            temperature_set_temp0=parameter.get_temperature3
        else:
            temperature_set_temp0=parameter.get_temperature4  
        
        #humidity influence on temperature
        if node0.get_humidity()<=(parameter.get_expect_humidity()-5-parameter.get_humidity_influence_range_of_air_temperature()):
            temperature_set_temp1=temperature_set_temp0+parameter.get_low_humidity_influence_on_air_temperature()
        elif node0.get_humidity()<=(parameter.get_expect_humidity()-5):
            tmpt=(parameter.get_expect_humidity()-5-node0.get_humidity())*parameter.get_low_humidity_influence_on_air_temperature()/parameter.get_humidity_influence_range_of_air_temperature()
            temperature_set_temp1=temperature_set_temp0+tmpt
        elif node0.get_humidity()>=(parameter.get_expect_humidity()+5):
            tmpt=(node0.get_humidity()-parameter.get_expect_humidity()-5)*parameter.get_high_humidity_influence_on_air_temperature()/(100-5-parameter.get_expect_humidity())
            temperature_set_temp1=temperature_set_temp0+tmpt
        else:
            temperature_set_temp1=temperature_set_temp0
            
        #light influence on temperature
        if outdoor.get_radiation()<parameter.get_expect_light:
            temperature_set_temp2=temperature_set_temp1
        else:
            temperature_set_temp2=temperature_set_temp1-parameter.get_light_influence_on_air_temperature_slope()*(outdoor.get_radiation()-parameter.get_expect_light())
        
        if temperature_set_temp2>(temperature_set_temp1+parameter.get_low_light_influence_on_temperature()):
            temperature_set_temp2=temperature_set_temp1+parameter.get_low_light_influence_on_temperature()
        elif temperature_set_temp2<(temperature_set_temp1-parameter.get_high_light_influence_on_temperature()):
            temperature_set_temp2=temperature_set_temp1-parameter.get_high_light_influence_on_temperature()
            
        if temperature_set_temp2<"0":
            temperature_set_temp2="0"
        
        if outdoor.get_temperature()<=parameter.get_frost_temperature():
            control.set_roof_vent_north("off")
            control.set_roof_vent_south("off")
        elif outdoor.get_temperature()<=parameter.get_indoor_temperature_lower_limit():    
            #small angle  小角度
            control.set_roof_vent_north("on")
            control.set_roof_vent_south("on")
        elif outdoor.get_temperature()<=temperature_set_temp2:
            #open all  半开
            control.set_roof_vent_north("on")
            control.set_roof_vent_south("on")
        else:
            #  全开
            control.set_roof_vent_north("on")
            control.set_roof_vent_south("on")
        
def get_side_wait_time():
    if node0.temperature>(temperature_set_temp2+parameter.get_temperature_to_open_side()):
        if side_wait_time<parameter.get_wait_time_to_open_side():
            side_wait_time +=1
        
def side_vent_control():
    if outdoor.get_bad_weather()=="true":
        control.set_side_vent("off")
    
    elif control.__cooling_pad=="on":
        control.set_side_vent("on")
    elif control.__roof_vent_north=="on" and control.__roof_vent_south=="on":
        if side_wait_time<parameter.get_wait_time_to_open_side():
            control.set_side_vent("off")
        elif side_wait_time>parameter.get_wait_time_to_open_side() and side_wait_time<2*parameter.get_wait_time_to_open_side():
            #应该是半开，需要修改
            control.set_side_vent("on")
        else:
            control.set_side_vent("on")
    else:
        control.set_side_vent("off")
        
def shade_screen_out_control():
    if outdoor.get_bad_weather()=="true":
        control.set_shade_screen_out("off")
    elif outdoor.get_radiation()>parameter.get_upper_limit_light_to_open_shade_screen_out():
        control.set_shade_screen_out("on")
    else:
        control.set_shade_screen_out("off")

def shade_screen_in_control():
    if control.__thermal_screen=="on":
        control.set_shade_screen_in("on")
    elif outdoor.get_radiation()>parameter.get_upper_limit_light_to_open_shade_screen_in():
        control.set_shade_screen_in("off")
    else:
        control.set_shade_screen_in("on")
        
def thermal_screen_control():
    if outdoor.get_bad_weather()=="true":
        control.set_thermal_screen("off")
    elif control.__fogging=="on":
        control.set_thermal_screen("off")
    else:
        current_hour=get_current_hour()
        current_month=get_current_month()
        if current_month>parameter.get_month_to_open_thermal_screen() and current_month<parameter.get_month_to_close_thermal_screen():
            if current_hour>parameter.get_time_to_open_thermal_screen() and current_hour<parameter.get_time_to_close_thermal_screen():
                control.set_thermal_screen("off")    #展开
        else:
            control.set_thermal_screen("on") #折起
            
            
def heating_control():
    if node0.get_temperature()<parameter.get_heating_start_lowest_temperature():
            control.set_heating("on")
    elif node0.get_temperature()>parameter.get_heating_stop_highest_temperature():
            control.set_heating("off")   
            
def fogging_control():
    if node0.get_temperature()>parameter.get_temperature_to_open_fogging()+1:
        control.set_fogging("on")
        # if control.get_thermal_screen()=="on"
        #    control.set_thermal_screen("off")
    elif node0.get_temperature()<parameter.get_temperature_to_open_fogging()-1:
        control.set_fogging("off")

def cooling_pad_control():
    if node0.get_temperature()>parameter.get_temperature_to_open_cooling_pad()+1:
        control.set_cooling_pad("on")
    elif node0.get_temperature()<parameter.get_temperature_to_open_cooling_pad()-1:#此时侧窗是与湿帘风机对应的，所以暂时不需要考虑90度方向的侧窗是否关闭
        control.set_cooling_pad("off")

def co2_control_control():
    if node0.get_co2()<parameter.get_co_2_lower_limit():
        control.set_co2("on")
    elif node0.get_co2()>parameter.get_co_2_upper_limit():
        control.set_co2("off")

def irrigation_control():              
    pass


def lighting_control():#补光策略，在currenttime 加了一个get_time()函数
    while True:
        if control.get_lighting_1()=="off" and control.get_lighting_2()=="off":
            if get_current_month()>parameter.get_month_to_open_lighting() and get_current_month()<parameter.get_month_to_close_lighting():
                if get_current_time()>parameter.get_period_1_start_lighting() and get_current_time()<parameter.get_period_1_stop_lighting():
                    if outdoor.get_radiation()<parameter.get_radiation_1_to_open_lighting():
                        control.set_lighting_1("on")
                        lighting_open_time=get_time()
                elif get_current_time()>parameter.get_period_2_start_lighting() and get_current_time()<parameter.get_period_2_stop_lighting():
                    if outdoor.get_radiation()<parameter.get_radiation_2_to_open_lighting():
                        control.set_lighting_1("on")
                        lighting_open_time2=get_time()

        elif control.get_lighting_1()=="on" and control.get_lighting_2()=="off":
            t1=int(get_time()-lighting_open_time)
            t2=int(get_time()-lighting_open_time2)
            if t1>1750 and t1<1850:
                control.set_lighting_2("on")
            if t2>1750 and t2<1850:
                control.set_lighting_2("on")

        elif control.get_lighting_1()=="on" and control.get_lighting_2()=="on":
            if get_current_time()>parameter.get_period_1_start_lighting() and get_current_time()<parameter.get_period_1_stop_lighting():
                if outdoor.get_radiation()>parameter.get_radiation_1_to_open_lighting():
                    control.set_lighting_1("off")
                    lighting_stop_time=get_time()
            elif get_current_time()>parameter.get_period_2_start_lighting() and get_current_time()<parameter.get_period_2_stop_lighting():
                if outdoor.get_radiation()>parameter.get_radiation_2_to_open_lighting():
                    control.set_lighting_1("off")
                    lighting_stop_time2=get_time()
            else:
                control.set_lighting_1("off")
                lighting_stop_time3=get_time()

        elif control.get_lighting_1()=="off" and control.get_lighting_2()=="on":
            t3=get_time()-lighting_stop_time3
            t4=get_time()-lighting_stop_time2
            t5=get_time()-lighting_stop_time
            if t3>1750 and t3<1850:
                control.set_lighting_2("off")
            if t4>1750 and t4<1850:
                control.set_lighting_2("off")
            if t5>1750 and t5<1850:
                control.set_lighting_2("off")
