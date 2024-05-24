# Zweipunktregler

## Description

Implementierung eines "Zweipunktreglers" mit einer kleinen Log Erweiterung.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisite](#prerequisite)
- [Code](#code)
- [Screenshots](#screenshots)

## Introduction

Es wird ein Zweipunktregler implementiert, der die Außentemperatur misst und beim Überschreiten der Grenztemperatur die LED anschaltet. Außerdem wird eine Log Datei beschrieben mit Datum, Uhrzeit und anschließend der gemessenen Temperatur.

## Prerequisite

### Components

- 1x DS18B20 Temperatursensor
- 1x Two-Pin LED
- 2x 330 Ohm Widerstände
- Ein paar Male-Male und Male-Female Kabel

### Wiring

Der Temperatursensor und die LED werden Seperat voneinander geschaltet mit jeweils einem Widerstand davor.

Eine sinngemäße Darstellung der LED Schaltung:

![led_wiring](/assets/led_circuit.webp)

Eine sinngemäße Darstellung der Sensor Schaltung:

<p align="center">
  <img src="/assets/sensor_circuit.jpg" alt="sensor_wiring">
</p>

### Libraries

Es sind zwei libraries notwendig, die über **pip** installiert werden können:

```bash
pip install W1ThermSensor RPi.GPIO
```

Die **W1ThermSensor** library erkennt automatisch den 1-Wire angebundenen Sensor.
**RPi.GPIO** ist für gewöhnlich in einem Raspbian Python build inklusiv.

## Code

Inhalt der **led.py** Datei:

```python
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
            print("Turn on cooling")
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            print("Turned off cooling")
        sleep(1)

except KeyboardInterrupt:
        print("Program terminated")

finally:
        GPIO.cleanup()
```

## Screenshots

Output des Python Skripts:

![py_output](/assets/py_output.png)

Output der Log Datei:

![log_output](/assets/log_output.png)
