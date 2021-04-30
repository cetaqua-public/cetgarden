from Sensors.Temperature import TemperatureSensor
from Sensors.LoadCell import LoadCellSensor
from Sensors.Humidity import HumiditySensor
from Cam.Camera import Camera
from DB.DataCollector import DataCollector
from Routiner.routiner import Routiner
import time

if __name__ == "__main__":
    # Routiner time parameters for each sensor and camera
    camera_routiner_hours = None
    temp_sensor_routiner_hours = 3/3600
    load_cell_sensor_routiner_hours = 10/3600
    humidity_sensor_routiner_hours = 4/3600

    #Create keywords and subset of keywords
    keywords = ["Temperatura", "Humedad", "Celda Carga", "Imagenes"]
    subSetKeywords = ["Temperatura", "Humedad", "Celda Carga"]

    #Create DataCollector to coordinate data reception
    data_collector = DataCollector(keywords, subSetKeywords)

    # Create Temperature sensor, load cell sensor and camera object
    camera = Camera(data_collector)
    temp_sensor = TemperatureSensor(data_collector, "Temperatura")
    load_cell_sensor = LoadCellSensor(data_collector, "Celda Carga")
    humidity_sensor = HumiditySensor(data_collector, "Humedad")

    # Create routine for each sensor
    camera_routiner = Routiner(camera_routiner_hours, camera.take_photo)
    temp_sensor_routiner = Routiner(temp_sensor_routiner_hours, temp_sensor.getMeasure, first_launch=True)
    load_cell_sensor_routiner = Routiner(load_cell_sensor_routiner_hours, load_cell_sensor.getMeasure, first_launch=True)
    humidity_sensor_routine = Routiner(humidity_sensor_routiner_hours, humidity_sensor.getMeasure, first_launch=True)

    # start each routiner thread
    #camera_routiner.start()
    temp_sensor_routiner.start()
    load_cell_sensor_routiner.start()
    humidity_sensor_routine.start()

    ## Dont close main until all routiners end
    # camera_routiner.join()
    # temp_sensor_routiner.join()
    # load_cell_sensor_routiner.join()
    # humidity_sensor_routine.join()

    while True:
        print(data_collector.get_data())
        time.sleep(5)