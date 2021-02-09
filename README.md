# RpiPythonScripts
Various Python Scripts for PI

## Switching Mosfet

### fan.py

Using IRF520 0-24V MOS Driver Module 

[IRF520 AliExpress Link](https://www.aliexpress.com/item/32790603826.html?spm=a2g0s.9042311.0.0.27424c4dygk8ae) 

Example - 

[Raspberry PI GPIO refrence](https://pinout.xyz/)

OR

[Raspberry PI GPIO refrence](https://osoyoo.com/2017/06/26/introduction-of-raspberry-pi-gpio/)


![alt text](https://github.com/sajrashid/RpiPythonScripts/blob/master/images/irf520.jfif "IRF520")

Connect  DC input (max 24v)  to VIN & GND

Connect load to output V+ & V-

Connect GPIO pin 2 to SIG

Connect GPIO GND pin(6 or any GND pin)

## Switching 3.3v Relay

### relay.py

Connect 3.3v Pin (1) from RPI to VCC on Relay

Connect Gnd to Gnd

Connect GPIO BCM pin 4 (actual pin 7)
![alt text](https://github.com/sajrashid/RpiPythonScripts/blob/master/images/relaywiring.PNG "Relay Wiring")

[See vid here for wiring](http://www.youtube.com/watch?v=p7wmzAzDX-Q&t=2m44s)  caution shows 5v, wiring is same apart from use 3.3v as above from pin 1

Connect Load to to NO or NC & Common


## SKR to PI serial UART connection using GPIO

[See vid here for wiring](https://www.youtube.com/watch?v=AtW3GqkKUz8-Q&t=14m39s)

Connect RX , TX GND pins from TFT header to PI UART GPIO pins 14 & 15 ensure RX & TX are crossed!!!

[PI UART PINOUT](https://pinout.xyz/pinout/pin8_gpio14)

To power the PI from the printers connect 5v to the Pin 2 on the PI

### Software Config

#### Swapping ports used by GPIO and Bluetooth
sudo nano /boot/config.txt & append
dtoverlay=pi3-miniuart-bt


#### Disable the serial console
sudo nano /boot/cmdline.txt
Look for following string (text) and delete 
console=serial0,115200

#### Raspi-config stuff
sudo raspi-config
Go to 'Interfacing Options'
Then P6 - Serial
Then No
Then Yes
Then go down to finish and reboot.

#### Rebuild your Klipper MCU firmware
unselect "Use USB for communication (instead of serial). 
Flash updated firmware to your board

#### Update your printer.cfg:
serial: /dev/ttyAMA0









