'''
Created on 2016年6月18日

@author: Zxh
'''
class Parameter(object):
    def __init__(self):
        self.time1="0"
        self.temperature1="0"
        self.time2="0"
        self.temperature2="0"
        self.time3="0"
        self.temperature3="0"
        self.time4="0"
        self.temperature4="0"
        
        self.co2_upper_limit="0"
        self.co2_lower_limit="0"
        
        self.cooling_start_temperature="0"
        self.cooling_stop_temperature="0"
        
        self.excepte_humidity="0"
        self.humidity_influence_range="0"
        self.low_humidity_influence_on_temperature="0"
        self.high_humidity_influence_on_temperature="0"
        self.expect_light="0"
        self.light_influence_on_tempurature_slop="0"
        self.light_influence_on_temperature="0"
        self.frost_temperature="0"
        self.indoor_temperature_lower_limit="0"
        self.roof_vent_wind_speed_upper_limit="0"
        self.roof_vent_rain_upper_limit="0"
        
        self.hearting_start_lowest_temperature="0"
        self.hearting_stop_highest_temperature="0"
        
        self.open_month="0"
        self.stop_month="0"
        self.open_time="0"
        self.stop_time="0"
        
        self.open_temperature_setting="0"
        self.wait_time_to_open="0"
        self.rani_upper_limit_to_close="0"
        
        self.upper_limit_light_to_open_shade_screen_out="0"
        self.upper_limit_light_to_open_shade_screen_in="0"
        self.light_to_open_lighting="0"
        self.soil_humidity_to_start_irrigation="0"
        self.soil_humidity_to_stop_irrigation="0"
        self.temperature_to_open_fogging="0"
        self.light_start_time="0"
        self.light_stop_time="0"
        self.temperature_to_open_cooling_pad="0"

    def set_parameter(self, time1, temperature1, time2, temperature2, time3, temperature3, time4, temperature4, co2_upper_limit, co2_lower_limit, cooling_start_temperature, cooling_stop_temperature, excepte_humidity, humidity_influence_range, low_humidity_influence_on_temperature, high_humidity_influence_on_temperature, expect_light, light_influence_on_tempurature_slop, light_influence_on_temperature, frost_temperature, indoor_temperature_lower_limit, roof_vent_wind_speed_upper_limit, roof_vent_rain_upper_limit, hearting_start_lowest_temperature, hearting_stop_highest_temperature, open_month, stop_month, open_time, stop_time, open_temperature_setting, wait_time_to_open, rani_upper_limit_to_close, upper_limit_light_to_open_shade_screen_out, upper_limit_light_to_open_shade_screen_in, light_to_open_lighting, soil_humidity_to_start_irrigation, soil_humidity_to_stop_irrigation, temperature_to_open_fogging, light_start_time, light_stop_time, temperature_to_open_cooling_pad):
        self.time1 = time1
        self.temperature1 = temperature1
        self.time2 = time2
        self.temperature2 = temperature2
        self.time3 = time3
        self.temperature3 = temperature3
        self.time4 = time4
        self.temperature4 = temperature4
        self.co2_upper_limit = co2_upper_limit
        self.co2_lower_limit = co2_lower_limit
        self.cooling_start_temperature = cooling_start_temperature
        self.cooling_stop_temperature = cooling_stop_temperature
        self.excepte_humidity = excepte_humidity
        self.humidity_influence_range = humidity_influence_range
        self.low_humidity_influence_on_temperature = low_humidity_influence_on_temperature
        self.high_humidity_influence_on_temperature = high_humidity_influence_on_temperature
        self.expect_light = expect_light
        self.light_influence_on_tempurature_slop = light_influence_on_tempurature_slop
        self.light_influence_on_temperature = light_influence_on_temperature
        self.frost_temperature = frost_temperature
        self.indoor_temperature_lower_limit = indoor_temperature_lower_limit
        self.roof_vent_wind_speed_upper_limit = roof_vent_wind_speed_upper_limit
        self.roof_vent_rain_upper_limit = roof_vent_rain_upper_limit
        self.hearting_start_lowest_temperature = hearting_start_lowest_temperature
        self.hearting_stop_highest_temperature = hearting_stop_highest_temperature
        self.open_month = open_month
        self.stop_month = stop_month
        self.open_time = open_time
        self.stop_time = stop_time
        self.open_temperature_setting = open_temperature_setting
        self.wait_time_to_open = wait_time_to_open
        self.rani_upper_limit_to_close = rani_upper_limit_to_close
        self.upper_limit_light_to_open_shade_screen_out = upper_limit_light_to_open_shade_screen_out
        self.upper_limit_light_to_open_shade_screen_in = upper_limit_light_to_open_shade_screen_in
        self.light_to_open_lighting = light_to_open_lighting
        self.soil_humidity_to_start_irrigation = soil_humidity_to_start_irrigation
        self.soil_humidity_to_stop_irrigation = soil_humidity_to_stop_irrigation
        self.temperature_to_open_fogging = temperature_to_open_fogging
        self.light_start_time = light_start_time
        self.light_stop_time = light_stop_time
        self.temperature_to_open_cooling_pad = temperature_to_open_cooling_pad

    def build_to_json(self):    
        return  '''"plant_parameter_setting":{
                                "time1":"%s",
                                "temperature1":"%s",
                                "time2":"%s",
                                "temperature2":"%s",
                                "time3":"%s",
                                "temperature3":"%s",
                                "time4":"%s",
                                "temperature4":"%s",
                                      },
           "co2_parameter_setting":{
                                "co2_upper_limit":"%s",
                                "co2_lower_limit":"%s"
                                    },
           "cooling_fans":{
                          "cooling_start_temperature":"%s",
                          "cooling_stop_temperature":"%s"
                          },
           "roof_vent_parameter_setting":{
                                "excepte_humidity":"%s",
                                "humidity_influence_range":"%s",
                                "low_humidity_influence_on_temperature":"%s",
                                "high_humidity_influence_on_temperature":"%s",
                                "expect_light":"%s",
                                "light_influence_on_tempurature_slop":"%s",
                                "light_influence_on_temperature":"%s",
                                "frost_temperature":"%s",
                                "indoor_temperature_lower_limit":"%s",
                                "roof_vent_wind_speed_upper_limit":"%s",
                                "roof_vent_rain_upper_limit":"%s"
                                          },
           "heating_parameter_setting":{
                                "hearting_start_lowest_temperature":"%s",
                                "hearting_stop_highest_temperature":"%s"
                                        },
           "thermal_screen_parameter_setting":{
                                        "open_month":"%s",
                                        "stop_month":"%s",
                                        "open_time":"%s",
                                        "stop_time":"%s"
                                               },
           "vent_vent_parameter_setting":{
                                    "open_temperature_setting":"%s",
                                    "wait_time_to_open":"%s",
                                    "rani_upper_limit_to_close":"%s"
                                          },
           "other_parameter_setting":{
                             "upper_limit_light_to_open_shade_screen_out" :"%s" ,
                             "upper_limit_light_to_open_shade_screen_in" :"%s",   
                             "light_to_open_lighting":"%s",
                             "soil_humidity_to_start_irrigation":"%s",
                             "soil_humidity_to_stop_irrigation":"%s",
                             "temperature_to_open_fogging":"%s",
                             "light_start_time":"%s",
                             "light_stop_time":"%s",
                             "temperature_to_open_cooling_pad":"%s"
                                      }
                                    
           }        
           '''\
           %(self.time1,self.temperature1,self.time2,self.temperature2,self.time3,self.temperature3,self.time4,self.temperature4,
            self.co2_upper_limit,self.co2_lower_limit,self.cooling_start_temperature,
            self.cooling_stop_temperature,self.excepte_humidity,self.humidity_influence_range,self.low_humidity_influence_on_temperature,
            self.high_humidity_influence_on_temperature,self.expect_light,self.light_influence_on_tempurature_slop,self.light_influence_on_temperature,
            self.frost_temperature,self.indoor_temperature_lower_limit,self.roof_vent_wind_speed_upper_limit,self.roof_vent_rain_upper_limit,
            self.hearting_start_lowest_temperature,self.hearting_stop_highest_temperature,self.open_month,self.stop_month,self.open_time,
            self.stop_time,self.open_temperature_setting,self.wait_time_to_open,self.rani_upper_limit_to_close,
            
            self.upper_limit_light_to_open_shade_screen_out,
            self.upper_limit_light_to_open_shade_screen_in,
            self.light_to_open_lighting,
            self.soil_humidity_to_start_irrigation,
            self.soil_humidity_to_stop_irrigation,
            self.temperature_to_open_fogging,
            self.light_start_time,
            self.light_stop_time,
            self.temperature_to_open_cooling_pad)