import asyncio
import datetime
import strip
import rings
import _rpi_ws281x as ws
from neopixel import *
from functools import partial

# Config
LED_COUNT = 54
LED_PIN = 18  # GPIO pin - must be PWM
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0
LED_STRIP = ws.SK6812_STRIP_RGBW

# Period times
_first_start = datetime.time(7, 25)
_first_end = datetime.time(8, 12)
_second_start = datetime.time(8, 17)
_second_end = datetime.time(9, 4)
_third_start = datetime.time(9, 9)
_third_end = datetime.time(10, 2)
_fourth_start = datetime.time(10, 7)
_fourth_end = datetime.time(10, 59)
_fifth_start = datetime.time(11, 3)
_fifth_end = datetime.time(11, 55)
_sixth_start = datetime.time(11, 59)
_sixth_end = datetime.time(12, 51)
_seventh_start = datetime.time(12, 56)
_seventh_end = datetime.time(1, 43)
_eighth_start = datetime.time(1, 48)
_eighth_end = datetime.time(2, 35)

# Special days
# Use datetime.date(year, month, day)
christmas = datetime.date(2018, 12, 25)


# Initialize the pixels
pixels = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
pixels.begin()


async def schedule_patterns(*patterns):
    tasks = []
    for pattern in patterns:
        tasks.append(pattern())
    await asyncio.gather(*tasks)


while True:
    current_date = datetime.datetime.today()
    # The current day, weekday, and time at each iteration
    day = current_date.date()
    time = current_date.time()

    if time >= datetime.time(17) or time <= datetime.time(5):
        """Turn the pixels off between 5PM and 5AM"""
        asyncio.run(schedule_patterns(partial(strip.fill, strip, Color(0, 0, 0, 0)),
                                      partial(rings.fill, strip, Color(0, 0, 0, 0))))
    elif day == christmas:
        """Christmas day"""
    elif _first_start <= time <= _first_end:
        """First Period"""
        asyncio.run(schedule_patterns(partial(strip.fill, strip, Color(0, 0, 0, 0)),
                                      partial(rings.fill, strip, Color(0, 0, 0, 0))))
    elif _second_start <= time <= _second_end:
        """Second Period"""
        asyncio.run(schedule_patterns(partial(strip.fill, strip, Color(0, 0, 0, 0)),
                                      partial(rings.fill, strip, Color(0, 0, 0, 0))))
    elif _third_start <= time <= _third_end:
        """Third Period"""
        asyncio.run(schedule_patterns(partial(strip.fill, strip, Color(0, 0, 0, 0)),
                                      partial(rings.fill, strip, Color(0, 0, 0, 0))))
    elif _fourth_start <= time <= _fourth_end:
        """Fourth Period"""
        asyncio.run(schedule_patterns(partial(strip.fill, strip, Color(0, 0, 0, 0)),
                                      partial(rings.fill, strip, Color(0, 0, 0, 0))))
    elif _fifth_start <= time <= _fifth_end:
        """Fifth Period"""
        asyncio.run(schedule_patterns(partial(strip.fill, strip, Color(0, 0, 0, 0)),
                                      partial(rings.fill, strip, Color(0, 0, 0, 0))))
    elif _sixth_start <= time <= _sixth_end:
        """Sixth Period"""
        asyncio.run(schedule_patterns(partial(strip.fill, strip, Color(0, 0, 0, 0)),
                                      partial(rings.fill, strip, Color(0, 0, 0, 0))))
    elif _seventh_start <= time <= _seventh_end:
        """Seventh Period"""
        asyncio.run(schedule_patterns(partial(strip.fill, strip, Color(0, 0, 0, 0)),
                                      partial(rings.fill, strip, Color(0, 0, 0, 0))))
    elif _eighth_start <= time <= _eighth_end:
        """Eighth Period"""
        asyncio.run(schedule_patterns(partial(strip.fill, strip, Color(0, 0, 0, 0)),
                                      partial(rings.fill, strip, Color(0, 0, 0, 0))))
    else:
        """Run during passing period or undefined portions of a day"""
        asyncio.run(schedule_patterns(partial(strip.fill, strip, Color(0, 0, 0, 0)),
                                      partial(rings.fill, strip, Color(0, 0, 0, 0))))
