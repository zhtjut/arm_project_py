class Indoor:
    '''the object of indoor climate'''

    def __init__(self):
        self.__temperature = 0
        self.__humidity = 0
        self.__radiation = 0
        self.__co2 = 0

    def set_temperature(self, temperature):
        self.__temperature = temperature

    def set_humidity(self, hum):
        self.__humidity = hum

    def set_radiation(self, rad):
        self.__radiation = rad

    def set_co2(self, co2):
        self.__co2 = co2

    def get_temperature(self):
        return self.__temperature

    def get_humidity(self):
        return self.__humidity

    def get_radiation(self):
        return self.__radiation

    def get_co2(self):
        return self.__co2
