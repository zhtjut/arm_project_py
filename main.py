# coding=utf-8

from currenttime import get_current_time
from flask import Flask, request
from outdoor import Outdoor
from control import Control
from indoor import Indoor
from scheduler import Scheduler
from parameter import Parameter
from database import save_db_indoor, save_db_outdoor, save_db_control, get_db_parameter, save_db_parameter
from autorun import auto_run_main, get_side_wait_time
import json

app = Flask(__name__)

node0 = Indoor('node_0')
outdoor = Outdoor()
c = Control()
p = Parameter()
get_db_parameter(p)  # init parameter from database
control_method = "computer"


def update_indoor():
    #     save_db_indoor(node0)
    print 'indoor updated', get_current_time()


def update_outdoor():
    outdoor.get_weather_from_api()
    #     save_db_outdoor(outdoor)
    print 'outdoor updated', get_current_time()


def update_control():
    #     save_db_control(c)
    print 'control updated', get_current_time()


scheduler1 = Scheduler(2000, update_outdoor)
scheduler2 = Scheduler(3000, update_indoor)
scheduler3 = Scheduler(5000, update_control)
update_outdoor()  # init outdoor from internet
scheduler1.start()
scheduler2.start()
scheduler3.start()


def auto_running():
    global node0, c, outdoor, p
    auto_run_main(node0, outdoor, c, p)


auto = Scheduler(10, auto_running)
wait_time = Scheduler(1, get_side_wait_time)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/indoor')
def get_indoor():
    return node0.build_json()


@app.route('/outdoor')
def response_outdoor():
    return outdoor.build_json()


@app.route('/control', methods=['GET', 'POST'])
def control():
    if request.method == 'POST':
        try:
            data = request.data
            return c.handle_post(data)
        except ValueError:
            return "get currently control state success"
    else:
        return c.build_json()


@app.route('/auto', methods=['GET', 'POST'])
def auto_run():
    global control_method
    if request.method == 'POST':
        data = request.data
        obj = json.loads(data)
        model = obj['model']
        if model == 'auto':
            if control_method != 'auto':
                auto_running()
                get_side_wait_time()
                wait_time.start()
                auto.start()
        else:
            if control_method == 'auto':
                auto.stop()
                wait_time.stop()
        control_method = model
        return model
    else:
        return 'get request null'


@app.route('/computer')
def computer_control():
    global control_method, auto
    return 'computer control'


@app.route('/parameter', methods=['GET', 'POST'])
def parameter():
    global p
    if request.method == 'GET':
        return p.build_to_json()
    else:
        data = request.data
        p.handle_post_parameter(data)
        save_db_parameter(p)
        return 'save success'


if __name__ == '__main__':
    app.run('0.0.0.0', '8020')
    scheduler1.stop()
    scheduler2.stop()
    scheduler3.stop()
