'''

@author: Zxh
'''
from currenttime import get_current_hour, get_current_month,get_time,get_current_time
from indoor import Indoor
from outdoor import Outdoor
from control import Control
from parameter import Parameter

class auto_run_alogrithm(object):
    now_time="9"
    temperature_set_temp0="0"
    temperature_set_temp1="1"
    temperature_set_temp2="2"
    side_wait_time="0"
        
    lighting_open_time="0"
    lighting_open_time2="0"
    lighting_stop_time="0"
    lighting_stop_time2="0"
    lighting_stop_time3="0"
    node0=Indoor('node')
    outdoor=Outdoor()
    control=Control()
    parameter=Parameter()
    
    def __init__(self,Indoor,Outdoor,Control,Parameter):
        self.node0=Indoor
        self.outdoor=Outdoor
        self.control=Control
        self.parameter=Parameter
    #indoor temperature humidity, light
    def roof_vent_control(self):
        if self.outdoor.get_bad_weather()=="true":
            self.control.set_roof_vent_north("off")
            self.control.set_roof_vent_south("off")
        else:
            if self.now_time >= self.parameter.get_time_1() and self.now_time < self.parameter.get_time_2():
                self.temperature_set_temp0=self.parameter.get_temperature_1()
            elif self.now_time >= self.parameter.get_time_2() and self.now_time < self.parameter.get_time_3():
                self.temperature_set_temp0=self.parameter.get_temperature2
            elif self.now_time >= self.parameter.get_time_3() and self.now_time < self.parameter.get_time_4():
                self.temperature_set_temp0=self.parameter.get_temperature3
            else:
                self.temperature_set_temp0=self.parameter.get_temperature4  
            
            #humidity influence on temperature
            if self.node0.get_humidity()<=(self.parameter.get_expect_humidity()-5-self.parameter.get_humidity_influence_range_of_air_temperature()):
                temperature_set_temp1=self.temperature_set_temp0+self.parameter.get_low_humidity_influence_on_air_temperature()
            elif self.node0.get_humidity()<=(self.parameter.get_expect_humidity()-5):
                tmpt=(self.parameter.get_expect_humidity()-5-self.node0.get_humidity())*self.parameter.get_low_humidity_influence_on_air_temperature()/self.parameter.get_humidity_influence_range_of_air_temperature()
                temperature_set_temp1=self.temperature_set_temp0+tmpt
            elif self.node0.get_humidity()>=(self.parameter.get_expect_humidity()+5):
                tmpt=(self.node0.get_humidity()-self.parameter.get_expect_humidity()-5)*self.parameter.get_high_humidity_influence_on_air_temperature()/(100-5-self.parameter.get_expect_humidity())
                temperature_set_temp1=self.temperature_set_temp0+tmpt
            else:
                temperature_set_temp1=self.temperature_set_temp0
                
            #light influence on temperature
            if self.outdoor.get_radiation()<self.parameter.get_expect_light:
                self.temperature_set_temp2=temperature_set_temp1
            else:
                self.temperature_set_temp2=temperature_set_temp1-self.parameter.get_light_influence_on_air_temperature_slope()*(self.outdoor.get_radiation()-self.parameter.get_expect_light())
            
            if self.temperature_set_temp2>(temperature_set_temp1+self.parameter.get_low_light_influence_on_temperature()):
                self.temperature_set_temp2=temperature_set_temp1+self.parameter.get_low_light_influence_on_temperature()
            elif self.temperature_set_temp2<(temperature_set_temp1-self.parameter.get_high_light_influence_on_temperature()):
                self.temperature_set_temp2=temperature_set_temp1-self.parameter.get_high_light_influence_on_temperature()
                
            if self.temperature_set_temp2<"0":
                self.temperature_set_temp2="0"
            
            if self.outdoor.get_temperature()<=self.parameter.get_frost_temperature():
                self.control.set_roof_vent_north("off")
                self.control.set_roof_vent_south("off")
            elif self.outdoor.get_temperature()<=self.parameter.get_indoor_temperature_lower_limit():    
                #small angle  
                self.control.set_roof_vent_north("on")
                self.control.set_roof_vent_south("on")
            elif self.outdoor.get_temperature()<=self.temperature_set_temp2:
                #open all
                self.control.set_roof_vent_north("on")
                self.control.set_roof_vent_south("on")
            else:
                #  
                self.control.set_roof_vent_north("on")
                self.control.set_roof_vent_south("on")
            
    def get_side_wait_time(self):
        if self.node0.temperature>(self.temperature_set_temp2+self.parameter.get_temperature_to_open_side()):
            if self.side_wait_time<self.parameter.get_wait_time_to_open_side():
                self.side_wait_time+=1
            
    def side_vent_control(self):
        if self.outdoor.get_bad_weather()=="true":
            self.control.set_side_vent("off")
        
        elif self.control.__cooling_pad=="on":
            self.control.set_side_vent("on")
        elif self.control.__roof_vent_north=="on" and self.control.__roof_vent_south=="on":
            if self.side_wait_time<self.parameter.get_wait_time_to_open_side():
                self.control.set_side_vent("off")
            elif self.side_wait_time>self.parameter.get_wait_time_to_open_side() and self.side_wait_time<2*self.parameter.get_wait_time_to_open_side():
                #half open
                self.control.set_side_vent("on")
            else:
                self.control.set_side_vent("on")
        else:
            self.control.set_side_vent("off")
            
    def shade_screen_out_control(self):
        if self.outdoor.get_bad_weather()=="true":
            self.control.set_shade_screen_out("off")
        elif self.outdoor.get_radiation()>self.parameter.get_upper_limit_light_to_open_shade_screen_out():
            self.control.set_shade_screen_out("on")
        else:
            self.control.set_shade_screen_out("off")
    
    def shade_screen_in_control(self):
        if self.control.__thermal_screen=="on":
            self.control.set_shade_screen_in("on")
        elif self.outdoor.get_radiation()>self.parameter.get_upper_limit_light_to_open_shade_screen_in():
            self.control.set_shade_screen_in("off")
        else:
            self.control.set_shade_screen_in("on")
            
    def thermal_screen_control(self):
        if self.outdoor.get_bad_weather()=="true":
            self.control.set_thermal_screen("off")
        elif self.control.__fogging=="on":
            self.control.set_thermal_screen("off")
        else:
            current_hour=get_current_hour()
            current_month=get_current_month()
            if current_month>self.parameter.get_month_to_open_thermal_screen() and current_month<self.parameter.get_month_to_close_thermal_screen():
                if current_hour>self.parameter.get_time_to_open_thermal_screen() and current_hour<self.parameter.get_time_to_close_thermal_screen():
                    self.control.set_thermal_screen("off")    #open
            else:
                self.control.set_thermal_screen("on") #
                
                
    def heating_control(self):  #ok
        if self.self.node0.get_temperature()<self.self.parameter.get_heating_start_lowest_temperature():
                self.control.set_heating("on")
        elif self.self.node0.get_temperature()>self.self.parameter.get_heating_stop_highest_temperature():
                self.control.set_heating("off")   
                
    def fogging_control(self):
        if self.node0.get_temperature()>self.parameter.get_temperature_to_open_fogging()+1:
            self.control.set_fogging("on")
            # if control.get_thermal_screen()=="on"
            #    control.set_thermal_screen("off")
        elif self.node0.get_temperature()<self.parameter.get_temperature_to_open_fogging()-1:
            self.control.set_fogging("off")
    
    def cooling_pad_control(self):
        if self.node0.get_temperature()>self.parameter.get_temperature_to_open_cooling_pad()+1:
            self.control.set_cooling_pad("on")
        elif self.node0.get_temperature()<self.parameter.get_temperature_to_open_cooling_pad()-1:
            self.control.set_cooling_pad("off")
    
    def co2_control(self):
        if self.node0.get_co2()<self.parameter.get_co_2_lower_limit():
            self.control.set_co2("on")
        elif self.node0.get_co2()>self.parameter.get_co_2_upper_limit():
            self.control.set_co2("off")
    
    def irrigation_control(self):            
        pass
    
    
    def lighting_control(self):
        while True:
            if self.control.get_lighting_1()=="off" and self.control.get_lighting_2()=="off":
                if get_current_month()>self.parameter.get_month_to_open_lighting() and get_current_month()<self.parameter.get_month_to_close_lighting():
                    if get_current_time()>self.parameter.get_period_1_start_lighting() and get_current_time()<self.parameter.get_period_1_stop_lighting():
                        if self.outdoor.get_radiation()<self.parameter.get_radiation_1_to_open_lighting():
                            self.control.set_lighting_1("on")
                            lighting_open_time=get_time()
                    elif get_current_time()>self.parameter.get_period_2_start_lighting() and get_current_time()<self.parameter.get_period_2_stop_lighting():
                        if self.outdoor.get_radiation()<self.parameter.get_radiation_2_to_open_lighting():
                            self.control.set_lighting_1("on")
                            lighting_open_time2=get_time()
    
            elif self.control.get_lighting_1()=="on" and self.control.get_lighting_2()=="off":
                t1=int(get_time()-lighting_open_time)
                t2=int(get_time()-lighting_open_time2)
                if t1>1750 and t1<1850:
                    self.control.set_lighting_2("on")
                if t2>1750 and t2<1850:
                    self.control.set_lighting_2("on")
    
            elif self.control.get_lighting_1()=="on" and self.control.get_lighting_2()=="on":
                if get_current_time()>self.parameter.get_period_1_start_lighting() and get_current_time()<self.parameter.get_period_1_stop_lighting():
                    if self.outdoor.get_radiation()>self.parameter.get_radiation_1_to_open_lighting():
                        self.control.set_lighting_1("off")
                        lighting_stop_time=get_time()
                elif get_current_time()>self.parameter.get_period_2_start_lighting() and get_current_time()<self.parameter.get_period_2_stop_lighting():
                    if self.outdoor.get_radiation()>self.parameter.get_radiation_2_to_open_lighting():
                        self.control.set_lighting_1("off")
                        lighting_stop_time2=get_time()
                else:
                    self.control.set_lighting_1("off")
                    lighting_stop_time3=get_time()
    
            elif self.control.get_lighting_1()=="off" and self.control.get_lighting_2()=="on":
                t3=get_time()-lighting_stop_time3
                t4=get_time()-lighting_stop_time2
                t5=get_time()-lighting_stop_time
                if t3>1750 and t3<1850:
                    self.control.set_lighting_2("off")
                if t4>1750 and t4<1850:
                    self.control.set_lighting_2("off")
                if t5>1750 and t5<1850:
                    self.control.set_lighting_2("off")

    def get_node_0(self):
        return self.node0


    def get_outdoor(self):
        return self.outdoor


    def get_control(self):
        return self.control


    def get_parameter(self):
        return self.parameter


    def set_node_0(self, value):
        self.node0 = value


    def set_outdoor(self, value):
        self.outdoor = value


    def set_control(self, value):
        self.control = value


    def set_parameter(self, value):
        self.parameter = value

