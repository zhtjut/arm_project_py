'''

@author: Zxh
'''
from parameter import Parameter
import json

p=Parameter()
# data='''{
#             "update_time":"%s",
#            "plant_parameter_setting":{
#                                 "time1":"%s",
#                                 "temperature1":"%s",
#                                 "time2":"%s",
#                                 "temperature2":"%s",
#                                 "time3":"%s",
#                                 "temperature3":"%s",
#                                 "time4":"%s",
#                                 "temperature4":"%s"
#                                       },
#            "co2_parameter_setting":{
#                                 "co2_upper_limit":"%s",
#                                 "co2_lower_limit":"%s"
#                                     },
#            "cooling_fans":{
#                           "cooling_start_temperature":"%s",
#                           "cooling_stop_temperature":"%s"
#                           },
#            "roof_vent_parameter_setting":{
#                                 "expect_humidity":"%s",
#                                 "humidity_influence_range_of_air_temperature":"%s",
#                                 "low_humidity_influence_on_air_temperature":"%s",
#                                 "high_humidity_influence_on_air_temperature":"%s",
#                                 "expect_light":"%s",
#                                 "light_influence_on_air_temperature_slope":"%s",
#                                 "high_light_influence_on_temperature":"%s",
#                                 "low_light_influence_on_temperature":"%s",
#                                 "frost_temperature":"%s",
#                                 "indoor_temperature_lower_limit":"%s",
#                                 "roof_vent_wind_speed_upper_limit":"%s",
#                                 "roof_vent_rain_upper_limit":"%s"
#                                           },
#            "heating_parameter_setting":{
#                                 "heating_start_lowest_temperature":"%s",
#                                 "heating_stop_highest_temperature":"%s"
#                                         },
#             "thermal_screen_parameter_setting":{
#                                         "month_to_open_thermal_screen":"%s",
#                                         "month_to_close_thermal_screen":"%s",
#                                         "time_to_open_thermal_screen":"%s",
#                                         "time_to_close_thermal_screen":"%s"
#                                                },
#            "side_vent_parameter_setting":{
#                                     "temperature_to_open_side":"%s",
#                                     "wait_time_to_open":"%s",
#                                     "rain_upper_limit_to_close":"%s"
#                                           },
#            "other_parameter_setting":{
#                              "upper_limit_light_to_open_out_shade_screen" :"%s" ,
#                              "upper_limit_light_to_open_in_shade_screen" :"%s",
#                              "soil_humidity_to_start_irrigation":"%s",
#                              "soil_humidity_to_stop_irrigation":"%s",
#                              "temperature_to_open_fogging":"%s",
#                              "temperature_to_open_cooling_pad":"%s"
#                                       },
#             "lighting_setting":{
#                             "month_to_open_lighting":"%s",
#                             "month_to_close_lighting":"%s",
#                             "period1_start_lighting":"%s",
#                             "period1_stop_lighting":"%s",
#                             "period2_start_lighting":"%s",
#                             "period2_stop_lighting":"%s",
#                             "radiation1_to_open_lighting":"%s",
#                             "radiation2_to_open_lighting":"%s"
#                                 }
#                                     
#         }
#         
#         '''

data=p.build_to_json()
# print data

obj=json.loads(data)
print obj['plant_parameter_setting']
keys=obj.keys()
print keys
for key in keys:
    value=obj.get(key)
    print value


