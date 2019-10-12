import Adafruit_DHT
import time
from datetime import datetime

# specify sensor type and pin number
sensor = 11
pin = 4

# get the current date & time and create a log file
now = datetime.now()
now_string = now.strftime("%d%m%Y%H%M%S")
filename = "temperature_humidity_log_" + now_string
log = open(filename,'w')

# initialise a counter for the loop
count = 0

while count < 100:
    # take a reading, print to the log, then sleep for 5 seconds
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    reading_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    log.write(reading_time + "    Temperature=" + str(int(temperature)) + ", Humidity=" + str(int(humidity)) + "%\n")
    time.sleep(5)

log.close()