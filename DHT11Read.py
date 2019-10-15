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
    # take a reading from the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    # print the reading to the log file in the required format
    reading_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    log.write(reading_time + "    Temperature=" + str(int(temperature)) + ", Humidity=" + str(int(humidity)) + "%\n")
    # check temp & humidity and log an alert if necessary
    if temperature > 22:
        log.write(reading_time + "    It is very hot\n")
    elif temperature < 18:
        log.write(reading_time + "    It is cold\n")
    if humidity > 50:
        log.write(reading_time + "    Humidity is very high\n")
    elif humidity > 30:
        log.write(reading_time + "    Humidity is high\n")
    # increment the loop counter and then sleep for 5 seconds
    count += 1
    time.sleep(5)

log.close()