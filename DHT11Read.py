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

# initialise a counter for the loop and variables for tracking temp & humidity
count = 0
max_temp = -50
min_temp = 50
temp_sum = 0
max_humidity = 0
min_humidity = 100
humidity_sum = 0

while count < 100:
    # take a reading from the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    # print the reading to the log file in the required format
    reading_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    log.write(reading_time + "    Temperature=" + str(int(temperature)) + ", Humidity=" + str(int(humidity)) + "%\n")
    # check temp & humidity and log an alert if necessary
    if temperature > 21:
        log.write(reading_time + "    It is very hot\n")
    elif temperature < 20:
        log.write(reading_time + "    It is cold\n")
    if humidity > 66:
        log.write(reading_time + "    Humidity is very high\n")
    elif humidity > 65:
        log.write(reading_time + "    Humidity is high\n")
    # check if temp & humidity are a new max or min
    if humidity < min_humidity:
        min_humidity = humidity
    if humidity > max_humidity:
        max_humidity = humidity
    if temperature < min_temp:
        min_temp = temperature
    if temperature > max_temp:
        max_temp = temperature
    # add values to the temp & humidity sums
    temp_sum += temperature
    humidity_sum += humidity
    # increment the loop counter and then sleep for 5 seconds
    count += 1
    time.sleep(5)

# calculate statistics and print a summary
log.write("\n******SUMMARY******\n")
log.write("Average Temperature: " + str(int(temp_sum)/100) + "\n")
log.write("Max Temperature: " + str(int(max_temp)) + "\n")
log.write("Min Temperature: " + str(int(min_temp)) + "\n")
log.write("Average Humidity: " + str(int(humidity_sum)/100) + "\n")
log.write("Max Humidity: " + str(int(max_humidity)) + "\n")
log.write("Min Humidity: " + str(int(min_humidity)) + "\n")

log.close()