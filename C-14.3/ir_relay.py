import socket
import RPi.GPIO as GPIO
import time

relay = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)

SOCKPATH = '/var/run/lirc/lircd'
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print ('starting up on %s' % SOCKPATH)
sock.connect(SOCKPATH)

def next_key():
    while True:
        clear_socket = sock.recv(128)
        data = sock.recv(128)
        if data:
            break
    ir_data = data.split()
    btn_name = ir_data[2]
    btn_name = btn_name.decode("utf-8")
    return btn_name
    
while True:
    button = next_key()
    if button == 'BTN_1':
        print('Relay ON')
        GPIO.output(relay, GPIO.HIGH)
    elif button == 'BTN_2':
        print('Relay OFF')
        GPIO.output(relay, GPIO.LOW)
    elif button == 'BTN_OK':
        print('Program Exiting...')
        GPIO.cleanup()
        raise SystemExit()
    else:
        print('Button not recognized')