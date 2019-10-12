import Adafruit_DHT
sensor = 11
pin = 4
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print("Humidity={}%; Temperature={}C".format(humidity, temperature))