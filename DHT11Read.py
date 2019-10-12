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
    # take a reading and measure how long the reading takes
    start = time.time()
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    elapsed_time = time.time() - start
    # print the reading to the log file in the required format
    reading_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    log.write(reading_time + "    Temperature=" + str(int(temperature)) + ", Humidity=" + str(int(humidity)) + "%\n")
    # sleep for five seconds minus the amount of time the reading took
    time.sleep(5 - elapsed_time)

log.close()