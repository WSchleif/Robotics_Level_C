import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

GPIO.output(21, GPIO.HIGH)
time.sleep(3)
GPIO.output(21, GPIO.LOW)

GPIO.cleanup()