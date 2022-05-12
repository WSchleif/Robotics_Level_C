import urllib.request
import time
import RPi.GPIO as GPIO

red = 13
green = 19
blue = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

def led_update(red_value,green_value,blue_value):
    GPIO.output(red, red_value)
    GPIO.output(green, green_value)
    GPIO.output(blue, blue_value)
    
try:
    while True:
        feed = urllib.request.urlopen('http://rgb.42electronics.com/color.txt')
        contents = feed.read()
        color = contents.decode("utf-8")
        
        if color == 'red':
            print('Red')
            led_update(1,0,0)
        elif color == 'green':
            print('Green')
            led_u