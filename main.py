from indoor import Indoor
from control import Control

from flask import Flask, request, json
from flask import abort
from flask import redirect

import time

app = Flask(__name__)

node0 = Indoor()
print "temperature", node0.get_temperature()
print "humidity", node0.get_humidity()
print "radiation", node0.get_radiation()
print "co2", node0.get_co2()
node0.set_temperature(20.0)
node0.set_humidity(80.0)
node0.set_radiation(8000)
node0.set_co2(500)
print "temperature", node0.get_temperature()
print "humidity", node0.get_humidity()
print "radiation", node0.get_radiation()
print "co2", node0.get_co2()
c = Control()


def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


print get_now_time()


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/indoor')
def get_indoor():
    return '''{"indoor": {"node_0": {"update_time": "%s",
    "temperature": "%s","relative_humidity": "%s",
    "radiation": "%s","co2": "%s"}}}''' \
           % (get_now_time(), node0.get_temperature(), node0.get_humidity(), node0.get_radiation(), node0.get_co2())


@app.route('/control', methods=['GET', 'POST'])
def control():
    if request.method == 'POST':
        data = request.data
        obj = json.loads(data)
        keys = obj.keys()
        json_response = "{"
        for key in keys:
            if key in Control.tri_states_actuators:
                value = obj.get(key)
                if value in Control.tri_states:
                    setattr(c, "_Control__" + key, value)  # relay
                    print key, getattr(c, "_Control__" + key)
                    json_response += '''"%s" : "%s",''' % (key, value)
                else:
                    print value, "illegal state"
            elif key in Control.bi_states_actuators:
                value = obj.get(key)
                if value in Control.bi_states:
                    setattr(c, "_Control__" + key, value)  # relay
                    print key, getattr(c, "_Control__" + key)
                    json_response += '''"%s" : "%s",''' % (key, value)
                else:
                    print value, "illegal state"
            else:
                print key, "illegal actuator"
        json_response += '''"%s" : "%s",''' % ("status", "success")
        json_response += '''"%s" : "%s"''' % ("update_time", get_now_time())
        json_response += "}"
        return json_response
    else:
        return '''{
        "actuator": {
        "update_time":"%s",
        "tri_state": {"roof_vent_south": "%s",
            "roof_vent_north": "%s",
            "side_vent": "%s","shade_screen_out": "%s",
            "shade_screen_in": "%s","thermal_screen": "%s"},
        "bi_state": {
            "cooling_pad": "%s","fogging": "%s",
            "heating": "%s","co2": "%s",
            "lighting_1": "%s","lighting_2": "%s",
            "irrigation": "%s"}}}''' \
               % (get_now_time(), c.get_roof_vent_south(), c.get_roof_vent_north(),
                  c.get_side_vent(), c.get_shade_screen_out(), c.get_shade_screen_in(),
                  c.get_thermal_screen(), c.get_cooling_pad(), c.get_fogging(), c.get_heating(),
                  c.get_co2(), c.get_lighting_1(), c.get_lighting_2(), c.get_irrigation())


@app.route('/hi')
def change():
    node0.set_temperature(30.0)
    return '<h1>set temp from 20 to 30</h1>'


if __name__ == '__main__':
    app.run('0.0.0.0', '8020')
