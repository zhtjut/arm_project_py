import json
from currenttime import get_current_time
from relay_output import tri_state_relay_output, bi_state_relay_output


class Control(object):
    '''the object of tri-state actuators and bi-state'''

    def __init__(self):
        self.__roof_vent_south = "on"
        self.__roof_vent_north = "on"
        self.__side_vent = "on"
        self.__shade_screen_out = "on"
        self.__shade_screen_in = "on"
        self.__thermal_screen = "on"
        self.__cooling_pad = "on"
        self.__fogging = "off"
        self.__heating = "off"
        self.__co2 = "off"
        self.__lighting_1 = "off"
        self.__lighting_2 = "off"
        self.__irrigation = "off"

    def set_roof_vent_south(self, value):
        self.__roof_vent_south = value


    def set_roof_vent_north(self, value):
        self.__roof_vent_north = value


    def set_side_vent(self, value):
        self.__side_vent = value


    def set_shade_screen_out(self, value):
        self.__shade_screen_out = value


    def set_shade_screen_in(self, value):
        self.__shade_screen_in = value


    def set_thermal_screen(self, value):
        self.__thermal_screen = value


    def set_cooling_pad(self, value):
        self.__cooling_pad = value


    def set_fogging(self, value):
        self.__fogging = value


    def set_heating(self, value):
        self.__heating = value


    def set_co_2(self, value):
        self.__co2 = value


    def set_lighting_1(self, value):
        self.__lighting_1 = value


    def set_lighting_2(self, value):
        self.__lighting_2 = value


    def set_irrigation(self, value):
        self.__irrigation = value

    
    
    
    def get_roof_vent_south(self):
        return self.__roof_vent_south

    def get_roof_vent_north(self):
        return self.__roof_vent_north

    def get_side_vent(self):
        return self.__side_vent

    def get_shade_screen_out(self):
        return self.__shade_screen_out

    def get_shade_screen_in(self):
        return self.__shade_screen_in

    def get_thermal_screen(self):
        return self.__thermal_screen

    def get_cooling_pad(self):
        return self.__cooling_pad

    def get_fogging(self):
        return self.__fogging

    def get_heating(self):
        return self.__heating

    def get_co2(self):
        return self.__co2

    def get_lighting_1(self):
        return self.__lighting_1

    def get_lighting_2(self):
        return self.__lighting_2

    def get_irrigation(self):
        return self.__irrigation

    def handle_post(self, data):
        obj = json.loads(data)
        keys = obj.keys()
        json_response = "{"
        for key in keys:
            if key in Control.tri_states_actuators:
                value = obj.get(key)
                if value in Control.tri_states:
                    setattr(self, "_Control__" + key, value)  
                    print key, getattr(self, "_Control__" + key)
                    tri_state_relay_output(key,value)
                    json_response += '''"%s" : "%s",''' % (key, value)
                else:
                    print value, "illegal state"
            elif key in Control.bi_states_actuators:
                value = obj.get(key)
                if value in Control.bi_states:
                    setattr(self, "_Control__" + key, value)  
                    print key, getattr(self, "_Control__" + key)
                    bi_state_relay_output(key,value)
                    json_response += '''"%s" : "%s", ''' % (key, value)
                else:
                    print value, "illegal state"
            else:
                print key, "illegal actuator"
        json_response += '''"status" : "%s", ''' % "success"
        json_response += '''"update_time" : "%s"''' % get_current_time()
        json_response += "}"
        return json_response

    def build_json(self):
        return '''
        {
    "update_time": "2016-06-22 18:52:27",
    "actuator": {
        "tri_state": {
            "roof_vent_south": "off",
            "roof_vent_north": "off",
            "side_vent": "off",
            "shade_screen_out": "off",
            "shade_screen_in": "off",
            "thermal_screen": "off"
        },
        "bi_state": {
            "cooling_pad": "off",
            "fogging": "off",
            "heating": "off",
            "co2": "off",
            "lighting_1": "off",
            "lighting_2": "off",
            "irrigation": "off"
                }
            }
        }''' \
               % (get_current_time(),self.get_roof_vent_south(), self.get_roof_vent_north(), self.get_side_vent(),
                  self.get_shade_screen_out(), self.get_shade_screen_in(),
                  self.get_thermal_screen(), self.get_cooling_pad(), self.get_fogging(), self.get_heating(),
                  self.get_co2(), self.get_lighting_1(), self.get_lighting_2(), self.get_irrigation()
                  )

    tri_states_actuators = ("roof_vent_south", "roof_vent_north", "side_vent",
                            "shade_screen_out", "shade_screen_in", "thermal_screen")

    bi_states_actuators = ("cooling_pad", "fogging", "heating", "co2", "lighting_1", "lighting_2", "irrigation")

    tri_states = ("on", "off", "stop")

    bi_states = ("on", "off")
    
