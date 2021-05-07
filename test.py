# Script para comprobar el correcto funcionamiento de medidas de los sensores
# y rutinas de ejecicion de las medidas y envio a la base de datos
from Sensors.dht22 import DHT22
from Sensors.LoadCell import LoadCellSensor
from Cam.Camera import Camera
from DB.DataCollector import DataCollector
from Routiner.routiner import Routiner
import time


if __name__ == "__main__":
    #Database
    db_name = "cetgarden"
    collection = "Andalucia"

    # Routiner time parameters for each sensor and camera
    camera_routiner_hours = 3
    dht22_sensor_routiner_hours = 1
    load_cell_sensor_routiner_hours = 1

    #Create keywords and subset of keywords
    keywords = ["Temperatura", "Humedad", "Celda Carga", "Imagenes"]
    subSetKeywords = ["Temperatura", "Humedad", "Celda Carga"]

    #Create DataCollector to coordinate data reception
    data_collector = DataCollector(db_name, collection, keywords, subSetKeywords)

    # Create Temperature sensor, load cell sensor and camera object
    camera = Camera(data_collector)
    dht22_sensor = DHT22(data_collector, "Temperatura", "Humedad")
    load_cell_sensor = LoadCellSensor(data_collector, "Celda Carga")

    # Create routine for each sensor
    camera_routiner = Routiner(camera_routiner_hours, camera.take_photo, first_launch=True)
    dht22_sensor_routiner = Routiner(dht22_sensor_routiner_hours, dht22_sensor.getMeasure, first_launch=True)
    # load_cell_sensor_routiner = Routiner(load_cell_sensor_routiner_hours, load_cell_sensor.getMeasure, first_launch=True)
    load_cell_sensor_routiner = Routiner(load_cell_sensor_routiner_hours, load_cell_sensor.getSimulatedMeasure, first_launch=True)

    # start each routiner thread
    camera_routiner.start()
    dht22_sensor_routiner.start()
    load_cell_sensor_routiner.start()

    # Dont close main until all routiners end
    camera_routiner.join()
    dht22_sensor_routiner.join()
    load_cell_sensor_routiner.join()