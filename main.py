import datetime
import strip
import rings
from neopixel import *
from functools import partial

# Config
LED_COUNT = 30
LED_PIN = 18  # GPIO pin - must be PWM
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0
LED_STRIP = ws.SK6812_STRIP_RGBW

# Special days
# Use datetime.date(year, month, day)
christmas = datetime.date(2018, 12, 25)

# Initialize the pixels
pixels = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
pixels.begin()


while True:
    current_date = datetime.datetime.today()
    # The current day, weekday, and time at each iteration
    day = current_date.date()
    time = current_date.time()

    if time >= datetime.time(17) or time <= datetime.time(5):
        """Turn the pixels off between 5PM and 5AM"""
        print('past')
    elif day == christmas:
        print('christmas')
    else:
        """Default action"""
        print('norm')
        strip.strip_with_ring(partial(strip.color_wipe, pixels, Color(255, 0, 0)),
                              partial(rings.eyes, pixels, Color(255, 0, 0)))
