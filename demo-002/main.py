# main.py
import time
from machine import Pin
led=Pin("LED",Pin.OUT)        #create LED object from pin13,Set Pin13 to output

while True:
  led.toggle()
  time.sleep(0.2)
  

  