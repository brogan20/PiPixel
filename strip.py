import asyncio
from neopixel import Color


ring_pixels = 24


async def fill(strip, color, wait_ms=0):
    """Fill the strip with a solid color pixel by pixel.
    Fills instantaneously when wait_ms = 0.
    """
    for i in range(strip.numPixels - ring_pixels):
        strip.setPixelColor(i, color)
        strip.show()
        await asyncio.sleep(wait_ms / 1000)


def wheel(wheel_pos):
    wheel_pos = 255 - wheel_pos
    if wheel_pos < 85:
        return Color(255 - wheel_pos * 3, 0, wheel_pos * 3)
    if wheel_pos < 170:
        wheel_pos -= 85
        return Color(0, wheel_pos * 3, 255 - wheel_pos * 3)
    wheel_pos -= 170
    return Color(wheel_pos * 3, 255 - wheel_pos * 3, 0)


async def rainbow_cycle(strip, wait_ms=50):
    for j in range(256*5):
        for i in range(strip.numPixels() - ring_pixels):
            strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        await asyncio.sleep(wait_ms / 1000)

