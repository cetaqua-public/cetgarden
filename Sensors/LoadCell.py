import RPi.GPIO as GPIO
from hx711 import HX711

class LoadCellSensor:

    def __setup_hx711(self, referenceUnits: float):
        self.__hx.set_reference_unit(referenceUnits)
        self.__hx.reset()
        self.__hx.tare()

    def __init__(self, data_collector, keyword: str, referenceUnits: float, dt_pin: int, sck_pin: int, num_measure: int):
        self.__data_collector = data_collector
        self.__count = 0
        self.__keyword = keyword
        self.__hx = HX711(dt_pin, sck_pin)
        self.__setup_hx711(referenceUnits)
        self.__num_measure = num_measure

    def getMeasure(self):
        val = self.__hx.get_weight(self.__num_measure)
        self.__hx.power_down()
        self.__hx.power_up()
        #return val
        #send data to database

    
