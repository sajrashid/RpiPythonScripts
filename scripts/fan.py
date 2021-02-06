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
            while cpu.temperature > 40:
                (sleep(1))
                print(cpu.temperature)
                 # To test the value of a pin use the .input method
                pin_is_off = GPIO.input(pin)  # Returns 0 if OFF or 1 if ON
                if pin_is_off == 0: # true if 1 (ON)
                   print(cpu.temperature)
                   GPIO.output(pin, GPIO.HIGH)
            GPIO.output(pin, GPIO.LOW)
            (sleep(10))
