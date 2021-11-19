import Adafruit_DHT
import time

#DHT_SENSOR = Adafruit_DHT.DHT11
#DHT_PIN = 4

while True:
    sensor = Adafruit_DHT.DHT11
    pin = 4
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    if humidity is not None and temperature is not None:
        print("Temp: - Hum: ", temperature, humidity)
    else:
        print("Sensor failure. Check wiring.")
    time.sleep(1)
