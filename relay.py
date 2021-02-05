import sys
print(sys.path)

import RPi.GPIO as GPIO
from time import sleep
pin =4
    # Set up input pin
    
    # set bcm pin mode 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
 #  turn on relay in revese mode so sety pin to low
GPIO.output(pin, GPIO.LOW)
(sleep(5))
  #  turn off relay in revese mode so sety pin to low
GPIO.output(pin, GPIO.HIGH)         