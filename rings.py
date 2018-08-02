import asyncio


strip_pixels = 30


async def fill(strip, color, wait_ms=0):
    """Fill the rings with a solid color pixel by pixel.
    Fills instantaneously when wait_ms = 0.
        """
    for i in range(strip.numPixels - strip_pixels):
        strip.setPixelColor(i + strip_pixels, color)
        strip.show()
        await asyncio.sleep(wait_ms / 1000)
