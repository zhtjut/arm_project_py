'''

@author: Zxh
'''
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import sqlite3
import os
from currenttime import get_current_time
from contextlib import closing
from parameter import Parameter

app=Flask(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'greenhouse.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
    ))

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db=connect_db()
    return g.sqlite_db

def close_db():
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()    

def save_db_indoor(Indoor):
    with app.app_context():
        db=get_db()
        db.execute('insert into indoor(node_number,update_time,temperature,humidity,radiation,co2) values(?,?,?,?,?,?)',
                    [Indoor.name,get_current_time(),Indoor.get_temperature(),Indoor.get_humidity(),Indoor.get_radiation(),Indoor.get_co2()])
        db.commit()
    print 'indoor save success'    
    
def save_db_outdoor(Outdoor):
    with app.app_context():
        db=get_db()
        db.execute('insert into outdoor(update_time,temperature,humidity,radiation,co2,wind_direction,wind_speed,rain_snow,atmosphere)\
                   values(?,?,?,?,?,?,?,?,?)', [get_current_time(),Outdoor.temperature,Outdoor.humidity,Outdoor.radiation,Outdoor.co2,Outdoor.wind_direction,\
                                                Outdoor.wind_speed,Outdoor.rain,Outdoor.atmosphere])
        db.commit()
    print 'outdoor save success'

def save_db_control(Control):
    with app.app_context():
        db=get_db()
        db.execute('insert into control_state(update_time,roof_vent_south,roof_vent_north,side_vent,shade_screen_out,shade_screen_in,thermal_screen,\
        cooling_pad,fogging,heating,co2,lighting_1,lighting_2,irrigation) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
        [get_current_time(),Control.get_roof_vent_south(),Control.get_roof_vent_north(),Control.get_side_vent(),Control.get_shade_screen_out(),Control.get_shade_screen_in(),\
         Control.get_thermal_screen(),Control.get_cooling_pad(),Control.get_fogging(),Control.get_heating(),Control.get_co2(),Control.get_lighting_1(),Control.get_lighting_2(),Control.get_irrigation()])
        db.commit()
    print 'control save success'

def save_db_parameter(Parameter):
    with app.app_context():
        db=get_db()
        db.execute('insert into parameter(time1,temperature1,time2,temperature2,time3,temperature3,time4,temperature4, co2_upper_limit,co2_lower_limit, cooling_start_temperature,cooling_stop_temperature,\
                    expect_humidity,humidity_influence_range_of_air_temperature,low_humidity_influence_on_air_temperature,high_humidity_influence_on_air_temperature,expect_light,light_influence_on_air_temperature_slope,high_light_influence_on_temperature,low_light_influence_on_temperature,frost_temperature,\
                    indoor_temperature_lower_limit,roof_vent_wind_speed_upper_limit,roof_vent_rain_upper_limit, heating_start_lowest_temperature,heating_stop_highest_temperature, month_to_open_thermal_screen,month_to_close_thermal_screen,time_to_open_thermal_screen,time_to_close_thermal_screen, temperature_to_open_side,\
                    wait_time_to_open_side,rani_upper_limit_to_close, upper_limit_light_to_open_shade_screen_out,upper_limit_light_to_open_shade_screen_in,soil_humidity_to_start_irrigation,soil_humidity_to_stop_irrigation,temperature_to_open_fogging,temperature_to_open_cooling_pad,\
                    month_to_open_lighting,month_to_close_lighting,time_to_close_lighting,time_to_close_lihting,radiatiopn_to_open_lighting,radiation_to_close_lihting) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',\
                    [Parameter.get_time_1(),Parameter.get_temperature_1(),Parameter.get_time_2(),Parameter.get_temperature_2(),Parameter.get_time_3(),Parameter.get_temperature_3(),Parameter.get_time_4(),Parameter.get_temperature_4(),Parameter.get_co2_upper_limit(),Parameter.get_co2_lower_limit(),
                     Parameter.get_cooling_start_temperature(),Parameter.get_cooling_stop_temperature(),
                     Parameter.get_expect_humidity(),Parameter.get_humidity_influence_range_of_air_temperature(),Parameter.get_low_humidity_influence_on_air_temperature(),Parameter.get_high_humidity_influence_on_air_temperature(),Parameter.get_expect_light(),Parameter.get_light_influence_on_air_temperature_slope(),
                     Parameter.get_high_light_influence_on_temperature(),Parameter.get_low_light_influence_on_temperature(),Parameter.get_frost_temperature(),Parameter.get_indoor_temperature_lower_limit(),Parameter.get_roof_vent_wind_speed_upper_limit(),Parameter.get_roof_vent_rain_upper_limit(),
                     Parameter.get_heating_start_lowest_temperature(),Parameter.get_heating_stop_highest_temperature(),Parameter.get_month_to_open_thermal_screen(),Parameter.get_month_to_close_thermal_screen(),Parameter.get_time_to_open_thermal_screen(),Parameter.get_time_to_close_thermal_screen(),
                     Parameter.get_temperature_to_open_side(),
                     Parameter.get_wait_time_to_open_side(),
                     Parameter.get_rani_upper_limit_to_close(),
                     Parameter.get_upper_limit_light_to_open_shade_screen_out(),
                     Parameter.get_upper_limit_light_to_open_shade_screen_in(),
                     Parameter.get_soil_humidity_to_start_irrigation(),
                     Parameter.get_soil_humidity_to_stop_irrigation(),
                     Parameter.get_temperature_to_open_fogging(),
                     Parameter.get_temperature_to_open_cooling_pad(),
                     Parameter.get_month_to_open_lighting(),
                     Parameter.get_month_to_close_lighting(),
                     Parameter.get_time_to_close_lighting(),
                     Parameter.get_time_to_close_lihting(),
                     Parameter.get_radiatiopn_to_open_lighting(),
                     Parameter.get_radiation_to_close_lihting()])
        db.commit()
        print 'parameter save success'
def get_db_parameter(Parameter):
    conn=sqlite3.connect('greenhouse.db')
    cursor=conn.execute('select * from parameter where id=(select max(id))')
    for row in cursor:
        pass
    Parameter.set_parameter(Parameter,row[1], row[2], row[3], row[4], row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],
                            row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],
                            row[28],row[29],row[30],row[31],row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40],
                            row[41],row[42],row[43],row[44],row[45])   
    print Parameter.build_to_json() 
    conn.close()
    print 'get parameter success'
if __name__ == '__main__':
    p=Parameter
    get_db_parameter(p)
#     init_db()
#     p=Parameter()
#     print p.get_co2_lower_limit()
#     save_db_parameter(p)
#      out=Outdoor()
#      with app.app_context():
#          db=get_db()
#          db.execute('''insert into outdoor(update_time,temperature,humidity,radiation,co2,wind_direction,wind_speed,rain_snow,atmosphere)\
#                         values(?,?,?,?,?,?,?,?,?)''', [out.update_time,out.temperature,out.humidity,out.radiation,out.co2,out.wind_direction,\
#                                                      out.wind_speed,out.rain,out.atmosphere])
#          db.commit()
#      print(out.classtoJson())   