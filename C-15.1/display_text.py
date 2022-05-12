import time
import Adafruit_SSD1306
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont

disp = Adafruit_SSD1306.SSD1306_128_64(rst=None)
disp.begin()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('/usr/shar/fonts/truetype/freefont/FreeSans.ttf', 18)

try:
    while True:
        draw.text((0, 0), 'Hello from', font=font, fill=255)
        draw.text((0, 22), '42 Electronics', font=font, fill=255)
        draw.text((0, 44), '\u263A \u263A \u263A \u263A \u263A', font=font, fill=255)
        disp.image(image)
        disp.display()
    
except KeyboardInterrupt:
    disp.clear()
    disp.display()
    SystemExit()