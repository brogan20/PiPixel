import time
import datetime
from neopixel import *

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


def color_wipe(strip, color, wait_ms=250):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def turn_off(strip):
    """Turn off all the pixels"""
    for i in range(strip.numPixels):
        strip.setPixelColor(i, off)
    strip.show()


def flash(strip, color, wait_ms=500):
    """Flash pixels on and off at a set rate"""
    for i in range(strip.numPixels):  # On
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms/1000)

    turn_off(strip)
    time.sleep(wait_ms/1000)


def wheel(wheel_pos):
    wheel_pos = 255 - wheel_pos
    if wheel_pos < 85:
        return Color(255 - wheel_pos * 3, 0, wheel_pos * 3)
    elif wheel_pos < 170:
        wheel_pos -= 85
        return Color(0, wheel_pos * 3, 255 - wheel_pos * 3)
    else:
        wheel_pos -= 170
        return Color(wheel_pos * 3, 255 - wheel_pos * 3, 0)


def rainbow_cycle(strip, wait_ms=50):
    for j in range(256 * 5):
        for i in range(strip.numPixels):
            strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000)


def flag(strip, wait_ms=100):
    for i in range(strip.numPixels):
        for blue in range(strip.numPixels/4):
            if blue % 3 == 0:
                strip.setPixelColor((blue + i) % strip.numPixels, Color(0, 0, 0, 255))
            else:
                strip.setPixelColor((blue + i) % strip.numPixels, Color(0, 0, 255, 0))
        for red in range(strip.numPixels - strip.numPixels/4):
            if red % 2 == 0:
                strip.setPixelColor((red + i + 10) % 40, Color(255, 0, 0, 0))
            else:
                strip.setPixelColor((red + i + 10) % 40, Color(0, 0, 0, 255))
        strip.show()
        time.sleep(wait_ms/1000)
