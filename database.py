'''

@author: Zxh
'''
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import sqlite3
import os
import outdoor
from currenttime import get_current_time
from contextlib import closing

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
    
# if __name__ == '__main__':
#      init_db()
#      out=Outdoor()
#      with app.app_context():
#          db=get_db()
#          db.execute('''insert into outdoor(update_time,temperature,humidity,radiation,co2,wind_direction,wind_speed,rain_snow,atmosphere)\
#                         values(?,?,?,?,?,?,?,?,?)''', [out.update_time,out.temperature,out.humidity,out.radiation,out.co2,out.wind_direction,\
#                                                      out.wind_speed,out.rain,out.atmosphere])
#          db.commit()
#      print(out.classtoJson())   