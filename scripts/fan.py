from gpiozero import CPUTemperature
import RPi.GPIO as GPIO
from time import sleep, strftime, time

cpu = CPUTemperature()
    # Set up input pin
pin =2   
    # set bcm pin mode 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
        # Create an Infinite Loops
while True: # Get Initial PIN State
            # To test the value of a PIN use the .input method
            # Returns 0 if OFF or 1 if ON
            pin_state = GPIO.input(pin)  
            # if the PIN is ON 
            if pin_state == 1: 
                 # Set the initial pin state to OFF 
                GPIO.output(pin, GPIO.LOW)
            print(cpu.temperature)
           
            if cpu.temperature > 45:

                while cpu.temperature > 40:
                    print(cpu.temperature)
                    # Get the current PIN State, Returns 0 if OFF or 1 if ON
                    pin_state = GPIO.input(pin) 
                   
                    # if PIN state false or 0, the PIN if off then turn the pin ON
                    if pin_state == 0: 
                        # Set the PIN state to ON 
                        GPIO.output(pin, GPIO.HIGH)
                    (sleep(1))
                    
            else:
                 (sleep(1))

