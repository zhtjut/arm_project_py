# coding=utf-8

from currenttime import get_current_time
from flask import Flask, request
from outdoor import Outdoor
from control import Control
from indoor import Indoor
from scheduler import Scheduler
from parameter import Parameter
from database import save_db_indoor, save_db_outdoor, save_db_control,get_db_parameter,save_db_parameter

app = Flask(__name__)

node0 = Indoor('node_0')
outdoor = Outdoor()
c = Control()
p=Parameter()


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

def update_parameter():
    get_db_parameter()

scheduler1 = Scheduler(2000, update_outdoor)
scheduler2 = Scheduler(3000, update_indoor)
scheduler3 = Scheduler(5000, update_control)
scheduler1.start()
scheduler2.start()
scheduler3.start()


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
            return "你追我，如果你追到我，我就让你你嘿嘿嘿！"
    else:
        return c.build_json()

@app.route('/parameter',methods=['GET','POST'])
def parameter():
    if request.method == 'POST':
        data=request.data
        a=p.handle_post_parameter(data)
        save_db_parameter(a)
        return 'save success'
    else:
        return get_db_parameter()

@app.route('/hi')
def change():
    node0.set_temperature(30.0)
    return '<h1>set temp from 20 to 30</h1>'


if __name__ == '__main__':
    app.run('0.0.0.0', '8020')
    scheduler1.stop()
    scheduler2.stop()
    scheduler3.stop()
