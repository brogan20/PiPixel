import calendar
from patterns import *

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
zee = datetime.date(2019, 2, 3)

# Initialize the pixels
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()


while True:
    current_date = datetime.datetime.today()
    # The current day, weekday, and time at each iteration
    day = current_date.date()
    time = current_date.time()

    if time >= datetime.time(17) or time <= datetime.time(5):
        """Turn the pixels off between 5PM and 5AM"""
        turn_off(strip)
    elif day == christmas:
        """Run special pattern for Christmas"""
        # todo - make special christmas pattern
        school_day(time,
                   color_wipe(strip, Color(255, 255, 0)),
                   color_wipe(strip, Color(255, 255, 0)))
    elif day == zee:
        flash(strip, Color(255, 20, 147), 1000)
    else:
        """Run everyday an event isn't taking place"""
        school_day(time,
                   color_wipe(strip, Color(255, 255, 0)),
                   color_wipe(strip, Color(255, 255, 0)))