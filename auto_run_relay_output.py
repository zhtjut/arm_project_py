'''

@author: Zxh
'''
from relay_output import tri_state_relay_output
from time import sleep

roof_state={"open all to close":-1,
            "open half to close":-0.7,
            "open small to close":-0.5,
            "close to open all":1,
            "open small to open all":2,
            "open half to open all":2,
            "close to open small":0.1,
            "open half to open small":1.1,
            "open all to open small":1.1,
            "close to open half":0.5,
            "open small to open half":1.5,
            "open all to open half":1.5,
            "":-1
            }
screen_state={"open to close":-1,
              "":-1,
                "close to open":1}

side_state={"open to close":-1,
            "close to open all":1,
            "close to open half":0.5,
            "open all to open half":1.5,
            "open half to open all":2,
            "":-1
            }

def roof_run_and_stop(time,key):
    value=roof_state.get(key)
#     print 'roof thread start'
    if value < 0:
        tri_state_relay_output('roof_vent_south','off')
        tri_state_relay_output('roof_vent_north','off')
        sleep(time*abs(value))
        tri_state_relay_output('roof_vent_south','stop')
        tri_state_relay_output('roof_vent_north','stop')
    elif value>1:
        tri_state_relay_output('roof_vent_south','off')
        tri_state_relay_output('roof_vent_north','off')
        sleep(time)
        tri_state_relay_output('roof_vent_south','on')
        tri_state_relay_output('roof_vent_north','on')
        sleep(time*(value-1))
        tri_state_relay_output('roof_vent_south','stop')
        tri_state_relay_output('roof_vent_north','stop')
    else:
        tri_state_relay_output('roof_vent_south','on')
        tri_state_relay_output('roof_vent_north','on')
        sleep(time*value)
        tri_state_relay_output('roof_vent_south','stop')
        tri_state_relay_output('roof_vent_north','stop')
        
def side_vent_run_and_stop(time,key):
#     print 'side thread start'
    value=side_state.get(key)
    if value<0:
        tri_state_relay_output("side_vent", "off")
        sleep(time*abs(value))
        tri_state_relay_output("side_vent", "stop")
    elif value>1:
        tri_state_relay_output("side_vent", "off")
        sleep(time)
        tri_state_relay_output("side_vent", "on")
        sleep(time*(value-1))
        tri_state_relay_output("side_vent", "stop")
    else:
        tri_state_relay_output("side_vent", "on")
        sleep(time*value)
        tri_state_relay_output("side_vent", "stop")
    
def shade_screen_out_run_and_stop(time,key):
#     print 'shade screen out thread start'
    value=screen_state.get(key)
    if value<0:
        tri_state_relay_output('shade_screen_out', "off")
        sleep(time)
        tri_state_relay_output('shade_screen_out', "stop")
    else:
        tri_state_relay_output('shade_screen_out', "on")
        sleep(time)
        tri_state_relay_output('shade_screen_out', "stop")

def shade_screen_in_run_and_stop(time,key):
#     print 'shade screen in thread start'
    value=screen_state.get(key)
    if value<0:
        tri_state_relay_output('shade_screen_in', "off")
        sleep(time)
        tri_state_relay_output('shade_screen_in', "stop")
    else:
        tri_state_relay_output('shade_screen_in', "on")
        sleep(time)
        tri_state_relay_output('shade_screen_in', "stop")

def thermal_screen_run_and_stop(time,key):
#     print 'thermal screen thread start'
    value=screen_state.get(key)
    if value<0:
        tri_state_relay_output('thermal_screen',"off")
        sleep(time)
        tri_state_relay_output('thermal_screen',"stop")
    else:
        tri_state_relay_output('thermal_screen',"on")
        sleep(time)
        tri_state_relay_output('thermal_screen',"stop")
