"""
Experimenting with RGBLEDs for digital clothing

0 to 65025 for PWM 
"""
from picozero import RGBLED
from time import sleep
from machine import Pin, PWM
    

#rgb = RGBLED(red = 9, green = 10, blue = 11)


red = PWM(Pin(9))
green = PWM(Pin(10))
blue = PWM(Pin(11))

red.freq(100)
green.freq(100)
blue.freq(100)


# Pretty bloody close to white but also now white 
red.duty_u16(15000)
green.duty_u16(0)
blue.duty_u16(0)

"""
while True:
    for duty in range(30000, 65025):
        red.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 30000, -1):
        red.duty_u16(duty)
        sleep(0.0001)
"""