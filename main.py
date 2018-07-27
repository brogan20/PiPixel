import datetime
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

# Initialize the pixels
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()


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


while True:
    date = datetime.datetime.today()
    # The current day, weekday, and time at each iteration
    day = date.date()
    weekday = calendar.day_name(date)
    time = date.time()

    if time >= datetime.time(17) or time <= datetime.time(5):
        """Turn the pixels off between 5PM and 5AM"""
        clear(strip)
    elif date == christmas:
        """Run special pattern for Christmas"""
        school_day(time,
                   color_wipe(strip, Color(255, 255, 0)),
                   color_wipe(strip, Color(255, 255, 0)))
    else:
        """Run everyday """
        school_day(time,
                   color_wipe(strip, Color(255, 255, 0)),
                   color_wipe(strip, Color(255, 255, 0)))