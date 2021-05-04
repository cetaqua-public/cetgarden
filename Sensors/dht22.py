#Sensor for temperature and humidity
class DHT22:

    def __init__(self, data_collector, keyword_temp: str, keyword_hum: str):
        self.__data_collector = data_collector
        self.__count = 0
        self.__keyword_temp = keyword_temp
        self.__keyword_hum = keyword_hum

    def getMeasure(self):
        self.__data_collector.add_data("H" + str(self.__count), self.__keyword_hum)
        self.__data_collector.add_data("T" + str(self.__count), self.__keyword_temp)
        self.__count += 1