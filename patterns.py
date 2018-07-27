import time

from neopixel import *


def color_wipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def clear(strip):
    for i in range(strip.numPixels):
        strip.setPixelColor(Color(0,0,0,0))
    strip.show()
