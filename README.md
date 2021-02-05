# RpiPythonScripts
Various Python Scripts for PI

## Switching Mosfet
fan.py

Using IRF520 0-24V MOS Driver Module 

[IRF520 AliExpress Link](https://www.aliexpress.com/item/32790603826.html?spm=a2g0s.9042311.0.0.27424c4dygk8ae) 

Example - 

[Raspberry PI GPIO refrence](https://pinout.xyz/)

OR

[Raspberry PI GPIO refrence](https://osoyoo.com/2017/06/26/introduction-of-raspberry-pi-gpio/)


![alt text](https://github.com/sajrashid/RpiPythonScripts/blob/main/images/irf520.jfif "IRF520")

Connect  DC input (max 24v)  to VIN & GND

Connect load to output V+ & V-

Connect GPIO pin 2 to SIG

Connect GPIO GND pin(6 or any GND pin)

## Switching Relay

Connect 3.3v Pin (1) from RPI to VCC on Relay

Connect Gnd to Gnd

Connect GPIO BCM pin 4 (actual pin 7)
![alt text](https://github.com/sajrashid/RpiPythonScripts/blob/main/images/relaywiring.PNG "Relay Wiring")

[See vid here for wiring](http://www.youtube.com/watch?v=p7wmzAzDX-Q&t=2m44s)  caution shows 5v, wiring is same apart from use 3.3v as above from pin 1

Connect Load to to NO or NC & Common









