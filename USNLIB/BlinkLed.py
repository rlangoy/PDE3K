from machine import Timer, Pin
import time

#Define a function to blink a LED
def blink(led):
     led.value(not led.value())

from machine import Pin

lRedGnd = Pin(15, Pin.OUT)  # Rød LED Catode (-)
lRedGnd.off()               # set pin to "off" (low) level

lRedOn  = Pin(13, Pin.OUT)  # Rød LED Anode  (+)

#Construct a virtual (id=-1) timer
blinkTimer = Timer(-1)
#Setup the timer to call the custom blink function at a regular interval of 0.5 second
blinkTimer.init(period=500, mode=Timer.PERIODIC, callback=lambda t:blink(lRedOn))