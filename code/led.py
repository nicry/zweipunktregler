import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor
from time import sleep
import datetime

LED_PIN = 5
temp_threshold = 25.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

sensor = W1ThermSensor()

def log_temp(temp):
    with open("temp_log.txt", "a") as log_file:
        log_file.write(str(datetime.datetime.now()) + " " + str(temp) + "\n")

try:
    while True:
        temp = sensor.get_temperature()
        print("Current temp is: " + str(temp))
        log_temp(temp)
        if temp > temp_threshold:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
        sleep(1)

except KeyboardInterrupt:
        print("Program terminated")

finally:
        GPIO.cleanup()
