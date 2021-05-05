# cetgarden

Software para monitorización de cultivo hidropónico

# Dependencias
**Schedule:** pip3 install schedule

**Base de datos mongo:** pip3 install pymongo 

**DHT22:** 

pip3 install adafruit-circuitpython-dht (libreria de python)

sudo apt-get install libgpiod2

**PiCamera:**

sudo apt-get install python3-picamera

# Conexion DHT22 en Rpi 4B
Con el comando pinout desde la terminal de la rpi obtenemos un mapa de los GPIO
- Conectar positivo a alimentación 5V de la rpi
- Conectar salido del sensor (patilla central marcada como "out") al GPIO4
- Conectar negativo a tierra 
