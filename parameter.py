'''

@author: Zxh
'''
from currenttime import get_current_time
class Parameter(object):
    def __init__(self):
        self.update_time="0"
        self.__time1="0"
        self.__temperature1="0"
        self.__time2="0"
        self.__temperature2="0"
        self.__time3="0"
        self.__temperature3="0"
        self.__time4="0"
        self.__temperature4="0"
        
        self.__co2_upper_limit="0"
        self.__co2_lower_limit="0"
        
        self.__cooling_start_temperature="0"
        self.__cooling_stop_temperature="0"
        
        self.__expect_humidity="0"
        self.__humidity_influence_range_of_air_temperature="0"
        self.__low_humidity_influence_on_air_temperature="0"
        self.__high_humidity_influence_on_air_temperature="0"
        self.__expect_light="0"
        self.__light_influence_on_air_temperature_slope="0"
        self.__high_light_influence_on_temperature="0"
        self.__low_light_influence_on_temperature="0"
        self.__frost_temperature="0"
        self.__indoor_temperature_lower_limit="0"
        self.__roof_vent_wind_speed_upper_limit="0"
        self.__roof_vent_rain_upper_limit="0"
        
        self.__heating_start_lowest_temperature="0"
        self.__heating_stop_highest_temperature="0"
        
        self.__month_to_open_thermal_screen="0"
        self.__month_to_close_thermal_screen="0"
        self.__time_to_open_thermal_screen="0"
        self.__time_to_close_thermal_screen="0"
        
        self.__temperature_to_open_side="0"
        self.__wait_time_to_open_side="0"
        self.__rani_upper_limit_to_close="0"
        
        self.__upper_limit_light_to_open_shade_screen_out="0"
        self.__upper_limit_light_to_open_shade_screen_in="0"
        self.__soil_humidity_to_start_irrigation="0"
        self.__soil_humidity_to_stop_irrigation="0"
        self.__temperature_to_open_fogging="0"
        self.__temperature_to_open_cooling_pad="0"

        self.__month_to_open_lighting="0"
        self.__month_to_close_lighting="0"
        self.__period1_start_lighting="0"
        self.__period1_stop_lighting="0"
        self.__period2_start_lighting="0"
        self.__period2_stop_lighting="0"
        self.__radiation1_to_open_lighting="0"
        self.__radiation2_to_open_lighting="0"
        
        self.__roof_vent_open_time="0"
        self.__side_vent_time="0"
        self.__shade_screen_out_time="0"
        self.__shade_screen_in_time="0"
        self.__thermal_screen_open_time="0"

    def get_time_1(self):
        return self.__time1


    def get_temperature_1(self):
        return self.__temperature1


    def get_time_2(self):
        return self.__time2


    def get_temperature_2(self):
        return self.__temperature2


    def get_time_3(self):
        return self.__time3


    def get_temperature_3(self):
        return self.__temperature3


    def get_time_4(self):
        return self.__time4


    def get_temperature_4(self):
        return self.__temperature4


    def get_co_2_upper_limit(self):
        return self.__co2_upper_limit


    def get_co_2_lower_limit(self):
        return self.__co2_lower_limit


    def get_cooling_start_temperature(self):
        return self.__cooling_start_temperature


    def get_cooling_stop_temperature(self):
        return self.__cooling_stop_temperature


    def get_expect_humidity(self):
        return self.__expect_humidity


    def get_humidity_influence_range_of_air_temperature(self):
        return self.__humidity_influence_range_of_air_temperature


    def get_low_humidity_influence_on_air_temperature(self):
        return self.__low_humidity_influence_on_air_temperature


    def get_high_humidity_influence_on_air_temperature(self):
        return self.__high_humidity_influence_on_air_temperature


    def get_expect_light(self):
        return self.__expect_light


    def get_light_influence_on_air_temperature_slope(self):
        return self.__light_influence_on_air_temperature_slope


    def get_high_light_influence_on_temperature(self):
        return self.__high_light_influence_on_temperature


    def get_low_light_influence_on_temperature(self):
        return self.__low_light_influence_on_temperature


    def get_frost_temperature(self):
        return self.__frost_temperature


    def get_indoor_temperature_lower_limit(self):
        return self.__indoor_temperature_lower_limit


    def get_roof_vent_wind_speed_upper_limit(self):
        return self.__roof_vent_wind_speed_upper_limit


    def get_roof_vent_rain_upper_limit(self):
        return self.__roof_vent_rain_upper_limit


    def get_heating_start_lowest_temperature(self):
        return self.__heating_start_lowest_temperature


    def get_heating_stop_highest_temperature(self):
        return self.__heating_stop_highest_temperature


    def get_month_to_open_thermal_screen(self):
        return self.__month_to_open_thermal_screen


    def get_month_to_close_thermal_screen(self):
        return self.__month_to_close_thermal_screen


    def get_time_to_open_thermal_screen(self):
        return self.__time_to_open_thermal_screen


    def get_time_to_close_thermal_screen(self):
        return self.__time_to_close_thermal_screen


    def get_temperature_to_open_side(self):
        return self.__temperature_to_open_side


    def get_wait_time_to_open_side(self):
        return self.__wait_time_to_open_side


    def get_rani_upper_limit_to_close(self):
        return self.__rani_upper_limit_to_close


    def get_upper_limit_light_to_open_shade_screen_out(self):
        return self.__upper_limit_light_to_open_shade_screen_out


    def get_upper_limit_light_to_open_shade_screen_in(self):
        return self.__upper_limit_light_to_open_shade_screen_in


    def get_soil_humidity_to_start_irrigation(self):
        return self.__soil_humidity_to_start_irrigation


    def get_soil_humidity_to_stop_irrigation(self):
        return self.__soil_humidity_to_stop_irrigation


    def get_temperature_to_open_fogging(self):
        return self.__temperature_to_open_fogging


    def get_temperature_to_open_cooling_pad(self):
        return self.__temperature_to_open_cooling_pad


    def get_month_to_open_lighting(self):
        return self.__month_to_open_lighting


    def get_month_to_close_lighting(self):
        return self.__month_to_close_lighting


    def get_period_1_start_lighting(self):
        return self.__period1_start_lighting


    def get_period_1_stop_lighting(self):
        return self.__period1_stop_lighting


    def get_period_2_start_lighting(self):
        return self.__period2_start_lighting


    def get_period_2_stop_lighting(self):
        return self.__period2_stop_lighting


    def get_radiation_1_to_open_lighting(self):
        return self.__radiation1_to_open_lighting


    def get_radiation_2_to_open_lighting(self):
        return self.__radiation2_to_open_lighting


    def get_roof_vent_open_time(self):
        return self.__roof_vent_open_time


    def get_side_vent_time(self):
        return self.__side_vent_time


    def get_shade_screen_out_time(self):
        return self.__shade_screen_out_time


    def get_shade_screen_in_time(self):
        return self.__shade_screen_in_time


    def get_thermal_screen_open_time(self):
        return self.__thermal_screen_open_time


    def set_time_1(self, value):
        self.__time1 = value


    def set_temperature_1(self, value):
        self.__temperature1 = value


    def set_time_2(self, value):
        self.__time2 = value


    def set_temperature_2(self, value):
        self.__temperature2 = value


    def set_time_3(self, value):
        self.__time3 = value


    def set_temperature_3(self, value):
        self.__temperature3 = value


    def set_time_4(self, value):
        self.__time4 = value


    def set_temperature_4(self, value):
        self.__temperature4 = value


    def set_co_2_upper_limit(self, value):
        self.__co2_upper_limit = value


    def set_co_2_lower_limit(self, value):
        self.__co2_lower_limit = value


    def set_cooling_start_temperature(self, value):
        self.__cooling_start_temperature = value


    def set_cooling_stop_temperature(self, value):
        self.__cooling_stop_temperature = value


    def set_expect_humidity(self, value):
        self.__expect_humidity = value


    def set_humidity_influence_range_of_air_temperature(self, value):
        self.__humidity_influence_range_of_air_temperature = value


    def set_low_humidity_influence_on_air_temperature(self, value):
        self.__low_humidity_influence_on_air_temperature = value


    def set_high_humidity_influence_on_air_temperature(self, value):
        self.__high_humidity_influence_on_air_temperature = value


    def set_expect_light(self, value):
        self.__expect_light = value


    def set_light_influence_on_air_temperature_slope(self, value):
        self.__light_influence_on_air_temperature_slope = value


    def set_high_light_influence_on_temperature(self, value):
        self.__high_light_influence_on_temperature = value


    def set_low_light_influence_on_temperature(self, value):
        self.__low_light_influence_on_temperature = value


    def set_frost_temperature(self, value):
        self.__frost_temperature = value


    def set_indoor_temperature_lower_limit(self, value):
        self.__indoor_temperature_lower_limit = value


    def set_roof_vent_wind_speed_upper_limit(self, value):
        self.__roof_vent_wind_speed_upper_limit = value


    def set_roof_vent_rain_upper_limit(self, value):
        self.__roof_vent_rain_upper_limit = value


    def set_heating_start_lowest_temperature(self, value):
        self.__heating_start_lowest_temperature = value


    def set_heating_stop_highest_temperature(self, value):
        self.__heating_stop_highest_temperature = value


    def set_month_to_open_thermal_screen(self, value):
        self.__month_to_open_thermal_screen = value


    def set_month_to_close_thermal_screen(self, value):
        self.__month_to_close_thermal_screen = value


    def set_time_to_open_thermal_screen(self, value):
        self.__time_to_open_thermal_screen = value


    def set_time_to_close_thermal_screen(self, value):
        self.__time_to_close_thermal_screen = value


    def set_temperature_to_open_side(self, value):
        self.__temperature_to_open_side = value


    def set_wait_time_to_open_side(self, value):
        self.__wait_time_to_open_side = value


    def set_rani_upper_limit_to_close(self, value):
        self.__rani_upper_limit_to_close = value


    def set_upper_limit_light_to_open_shade_screen_out(self, value):
        self.__upper_limit_light_to_open_shade_screen_out = value


    def set_upper_limit_light_to_open_shade_screen_in(self, value):
        self.__upper_limit_light_to_open_shade_screen_in = value


    def set_soil_humidity_to_start_irrigation(self, value):
        self.__soil_humidity_to_start_irrigation = value


    def set_soil_humidity_to_stop_irrigation(self, value):
        self.__soil_humidity_to_stop_irrigation = value


    def set_temperature_to_open_fogging(self, value):
        self.__temperature_to_open_fogging = value


    def set_temperature_to_open_cooling_pad(self, value):
        self.__temperature_to_open_cooling_pad = value


    def set_month_to_open_lighting(self, value):
        self.__month_to_open_lighting = value


    def set_month_to_close_lighting(self, value):
        self.__month_to_close_lighting = value


    def set_period_1_start_lighting(self, value):
        self.__period1_start_lighting = value


    def set_period_1_stop_lighting(self, value):
        self.__period1_stop_lighting = value


    def set_period_2_start_lighting(self, value):
        self.__period2_start_lighting = value


    def set_period_2_stop_lighting(self, value):
        self.__period2_stop_lighting = value


    def set_radiation_1_to_open_lighting(self, value):
        self.__radiation1_to_open_lighting = value


    def set_radiation_2_to_open_lighting(self, value):
        self.__radiation2_to_open_lighting = value


    def set_roof_vent_open_time(self, value):
        self.__roof_vent_open_time = value


    def set_side_vent_time(self, value):
        self.__side_vent_time = value


    def set_shade_screen_out_time(self, value):
        self.__shade_screen_out_time = value


    def set_shade_screen_in_time(self, value):
        self.__shade_screen_in_time = value


    def set_thermal_screen_open_time(self, value):
        self.__thermal_screen_open_time = value

        

   
    

    
    
        
    def build_to_json(self):    
        return  '''{
            "update_time":"%s"
           "plant_parameter_setting":{
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
                                "expect_humidity":"%s",
                                "humidity_influence_range_of_air_temperature":"%s",
                                "low_humidity_influence_on_air_temperature":"%s",
                                "high_humidity_influence_on_air_temperature":"%s",
                                "expect_light":"%s",
                                "light_influence_on_air_temperature_slope":"%s",
                                "high_light_influence_on_temperature":"%s",
                                "low_light_influence_on_temperature":"%s",
                                "frost_temperature":"%s",
                                "indoor_temperature_lower_limit":"%s",
                                "roof_vent_wind_speed_upper_limit":"%s",
                                "roof_vent_rain_upper_limit":"%s"
                                          },
           "heating_parameter_setting":{
                                "heating_start_lowest_temperature":"%s",
                                "heating_stop_highest_temperature":"%s"
                                        },
           "thermal_screen_parameter_setting":{
                                        "month_to_open_thermal_screen":"%s",
                                        "month_to_close_thermal_screen":"%s",
                                        "time_to_open_thermal_screen":"%s",
                                        "time_to_close_thermal_screen":"%s"
                                               },
           "side_vent_parameter_setting":{
                                    "temperature_to_open_side":"%s",
                                    "wait_time_to_open":"%s",
                                    "rain_upper_limit_to_close":"%s"
                                          },
           "other_parameter_setting":{
                             "upper_limit_light_to_open_out_shade_screen" :"%s" ,
                             "upper_limit_light_to_open_in_shade_screen" :"%s",
                             "soil_humidity_to_start_irrigation":"%s",
                             "soil_humidity_to_stop_irrigation":"%s",
                             "temperature_to_open_fogging":"%s",
                             "temperature_to_open_cooling_pad":"%s"
                                      },
            "lighting_setting":{
                            "month_to_open_lighting":"%s",
                            "month_to_close_lighting":"%s",
                            "period1_start_lighting":"%s",
                            "period1_stop_lighting":"%s",
                            "period2_start_lighting":"%s",
                            "period2_stop_lighting":"%s",
                            "radiation1_to_open_lighting":"%s",
                            "radiation2_to_open_lighting":"%s"
                                },
             "time_that_full_open_to_full_close":{
                                "roof_vent_open_time":"%s"",
                                "side_vent_open_time":"%s"",
                                "shade_screen_out_open_time":"%s"",
                                "shade_screen_in_open_time":"%s"",
                                "thermal_screen_open_time":"%s""
                             }
           }                
           '''\
           %(get_current_time(),
             self.__time1,
                self.__temperature1,
                self.__time2,
                self.__temperature2,
                self.__time3,
                self.__temperature3,
                self.__time4,
                self.__temperature4,
                
                self.__co2_upper_limit,
                self.__co2_lower_limit,
                
                self.__cooling_start_temperature,
                self.__cooling_stop_temperature,
                
                self.__expect_humidity,
                self.__humidity_influence_range_of_air_temperature,
                self.__low_humidity_influence_on_air_temperature,
                self.__high_humidity_influence_on_air_temperature,
                self.__expect_light,
                self.__light_influence_on_air_temperature_slope,
                self.__high_light_influence_on_temperature,
                self.__low_light_influence_on_temperature,
                self.__frost_temperature,
                self.__indoor_temperature_lower_limit,
                self.__roof_vent_wind_speed_upper_limit,
                self.__roof_vent_rain_upper_limit,
                
                self.__heating_start_lowest_temperature,
                self.__heating_stop_highest_temperature,
                
                self.__month_to_open_thermal_screen,
                self.__month_to_close_thermal_screen,
                self.__time_to_open_thermal_screen,
                self.__time_to_close_thermal_screen,
                
                self.__temperature_to_open_side,
                self.__wait_time_to_open_side,
                self.__rani_upper_limit_to_close,
                
                self.__upper_limit_light_to_open_shade_screen_out,
                self.__upper_limit_light_to_open_shade_screen_in,
                self.__soil_humidity_to_start_irrigation,
                self.__soil_humidity_to_stop_irrigation,
                self.__temperature_to_open_fogging,
                self.__temperature_to_open_cooling_pad,
        
                self.__month_to_open_lighting,
                self.__month_to_close_lighting,
                self.__period1_start_lighting,
                self.__period1_stop_lighting,
                self.__period2_start_lighting,
                self.__period2_stop_lighting,
                self.__radiation1_to_open_lighting,
                self.__radiation2_to_open_lighting,
                
                self.__roof_vent_open_time,
                self.__side_vent_time,
                self.__shade_screen_out_time,
                self.__shade_screen_in_time,
                self.__thermal_screen_open_time
            )
#test
if __name__=='__main__':
#     print Parameter().get_co2_lower_limit()
    test=Parameter()
#     d="d"
#     test.set__side_vent_time(d)
    print test.get_co_2_lower_limit()
#     print test.build_to_json()