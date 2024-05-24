import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor
from time import sleep

LED_PIN = 5
TEMP_Threshold = 27.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

sensor = W1ThermSensor()

try:
        while True:
                temp = sensor.get_temperature()
                print("Current temp is: " + str(temp))

                if temp > TEMP_Threshold:
                        GPIO.output(LED_PIN, GPIO.HIGH)
                        print("LED High")
                else:
                        GPIO.output(LED_PIN, GPIO.LOW)

                sleep(1)

except KeyboardInterrupt:
        print("Program terminated")

finally:
        GPIO.cleanup()