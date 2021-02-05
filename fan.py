from gpiozero import CPUTemperature
import RPi.GPIO as GPIO
from time import sleep, strftime, time

pin =2
cpu = CPUTemperature()
    # Set up input pin
    
    # set bcm pin mode 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
        # Create an Infinite Loop
while True:
            print(cpu.temperature)
            # set pin to off initial
            GPIO.output(pin, GPIO.LOW)
            if cpu.temperature > 40:
                GPIO.output(pin, GPIO.HIGH)
                (sleep(5))
            else:
                GPIO.output(pin, GPIO.LOW)
                (sleep(10))