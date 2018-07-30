def eyes(pixels, color):
    for i in range(pixels.numPixels() - 30):
        pixels.setPixelColor(i + 30, color)
    pixels.show()
