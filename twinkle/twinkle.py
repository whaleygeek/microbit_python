from microbit import *
from neopixel import *
import random

n = NeoPixel(pin0, 8)

while True:
    i=random.randrange(8)
    r=random.randrange(255)
    g=random.randrange(255)
    b=random.randrange(255)
    n[i]=(r,g,b)
    n.show()
    sleep(10)

