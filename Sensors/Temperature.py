class TemperatureSensor:

    def __init__(self, data_collector, keyword: str):
        self.__data_collector = data_collector
        self.__count = 0
        self.__keyword = keyword

    def getMeasure(self):
        self.__data_collector.add_data("T" + str(self.__count), self.__keyword)
        self.__count += 1
