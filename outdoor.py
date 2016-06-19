# coding=utf-8
import json
import urllib
from currenttime import get_current_time


class Outdoor(object):
    update_time = "just now"
    temperature = "0"
    humidity = "0"
    radiation = "0"
    co2 = "0"
    wind_direction = "no wind"
    wind_speed = "0"
    rain = "0"
    atmosphere = "0"
    bad_weather="true"

    def set_outdoor(self, update_time1, temperature1, humidity1, radiation1, co21, wind_direction1, wind_speed1,
                    rain1, atmosphere1):
        self.update_time = update_time1
        self.temperature = temperature1
        self.humidity = humidity1
        self.radiation = radiation1
        self.co2 = co21
        self.wind_direction = wind_direction1
        self.wind_speed = wind_speed1
        self.rain = rain1
        self.atmosphere = atmosphere1

    def build_json(self):
        return '''
        {
            "outdoor":{
                "temperature":"%s",
                "humidity":"%s",
                "radiation":"%s",
                "co2":"%s",
                "wind_direction":"%s",
                "wind_speed":"%s",
                "rain":"%s",
                "atmosphere":"%s",
                "update_time":"%s"
            }
        }''' \
               % (self.temperature, self.humidity, self.radiation, self.co2, self.wind_direction,
                  self.wind_speed, self.rain, self.atmosphere, self.update_time)

    def get_weather_from_api(self):
        url = 'https://api.heweather.com/x3/weather?city=jiading&key=8924d0a789dd4e348982cfe7f721267c'
        data = urllib.urlopen(url).read()
        wea_json = json.loads(data)
        wea_json = wea_json['HeWeather data service 3.0'][0]
        update_time = get_current_time()
        temperature = str(wea_json['now']['tmp'])
        humidity = str(wea_json['now']['hum'])
        radiation = 'not included'
        co2 = 'not included'
        wind_direction = wea_json['now']['wind']['dir']
        wind_speed = str(wea_json['now']['wind']['spd'])
        rain = wea_json['now']['pcpn']
        if (float(rain)) > 1.0:
            rain = 'true'  # raining
        else:
            rain = 'false'  # no rain
        atmosphere = str(wea_json['now']['pres'])
        self.set_outdoor(update_time, temperature, humidity, radiation, co2, wind_direction, wind_speed, rain,
                         atmosphere)
#         test
# a=Outdoor()
# a.get_weather_from_api()
# print(a.build_json())
