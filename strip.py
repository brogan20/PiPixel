import time
import datetime
from neopixel import *

NUM_LED = 30

off = Color(0, 0, 0)

# Time of school periods (2:35 dismissal)
first_start = datetime.time(7, 25)
first_end = datetime.time(8, 12)
second_start = datetime.time(8, 17)
second_end = datetime.time(9, 4)
third_start = datetime.time(9, 9)
third_end = datetime.time(10, 2)
fourth_start = datetime.time(10, 7)
fourth_end = datetime.time(10, 59)
fifth_start = datetime.time(11, 3)
fifth_end = datetime.time(11, 55)
sixth_start = datetime.time(11, 59)
sixth_end = datetime.time(12, 51)
seventh_start = datetime.time(12, 56)
seventh_end = datetime.time(1, 43)
eighth_start = datetime.time(1, 48)
eighth_end = datetime.time(2, 35)


def school_day(current_time, class_time, passing):
    """Change the pattern throughout the school day so different patterns happen during class,
     and others during passing period"""
    if (first_start <= current_time <= first_end
            or second_start <= current_time <= second_end
            or third_start <= current_time <= third_end
            or fourth_start <= current_time <= fourth_end
            or fifth_start <= current_time <= fifth_end
            or sixth_start <= current_time <= sixth_end
            or seventh_start <= current_time <= seventh_end
            or eighth_start <= current_time <= eighth_end):
        class_time()
    else:
        passing()


def strip_with_ring(strip_pattern, ring_pattern):
    ring_pattern()
    strip_pattern()


def turn_off(pixels):
    """Turn off all the pixels"""
    for i in range(pixels):
        pixels.setPixelColor(i, off)
    pixels.show()


def color_wipe(pixels, color, wait_ms=250):
    """Wipe color across display a pixel at a time."""
    for i in range(pixels):
        pixels.setPixelColor(i, color)
        pixels.show()
        time.sleep(wait_ms / 1000.0)


def flash(pixels, color, wait_ms=500):
    """Flash pixels on and off at a set rate"""
    for i in range(pixels):  # On
        pixels.setPixelColor(i, color)
    pixels.show()
    time.sleep(wait_ms/1000)

    turn_off(pixels)
    time.sleep(wait_ms/1000)
