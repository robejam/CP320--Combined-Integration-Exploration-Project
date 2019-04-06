#Parallax 2-Axis Joystick (#27800) 
#https://www.parallax.com/product/27800

import RPi.GPIO as GPIO
import spidev
import time
lr_channel = 1
ud_channel = 0

spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1350000

GPIO.setmode(GPIO.BCM)
stepper_pins=[12,13,18,19]

GPIO.setup(stepper_pins,GPIO.OUT)

stepper_sequence=[]
stepper_sequence.append([GPIO.HIGH, GPIO.LOW, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.HIGH, GPIO.HIGH, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.HIGH, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.HIGH, GPIO.HIGH,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.HIGH,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.HIGH,GPIO.HIGH])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.LOW,GPIO.HIGH])
stepper_sequence.append([GPIO.HIGH, GPIO.LOW, GPIO.LOW,GPIO.HIGH])

def move_clockwise(slp):
    for row in stepper_sequence:
        GPIO.output(stepper_pins,row)
        time.sleep(slp)

def move_counterclockwise(slp):
    for row in reversed (stepper_sequence):
        GPIO.output(stepper_pins,row)
        time.sleep(slp)		

def read_channel(adc_channel):
    adc=spi.xfer2([1,(8+adc_channel)<<4,0])
    data=((adc[1]&3)<<8) +adc[2]
    return data

def abs_x_pos(lr_pos):
    if lr_pos > 516:
        abs_pos = lr_pos - 516
    elif lr_pos < 516:
        abs_pos = -1*(516-lr_pos)
    else:
        abs_pos = 0
    return abs_pos

def abs_y_pos(ud_pos):
    if ud_pos > 506:
        abs_pos = ud_pos - 506
    elif ud_pos < 506:
        abs_pos = -1*(506-ud_pos)
    else:
        abs_pos = 0
    return abs_pos

def sleep(val):
# Determines stepper sleep time based on the current position of the joystick
# The further the joystick is moved, the faster the motor moves. This is caused
# by the linear equation in the function based on the points (0,0.1) & (500, 0.01)
# from joystick data.
    val = abs(val)
    slp = -0.00018 * val + 0.1
    return slp

try:		
    while True:
        lr_pos = read_channel(lr_channel)
        ud_pos = read_channel(ud_channel)
        abs_x = abs_x_pos(lr_pos)
        abs_y = abs_y_pos(ud_pos)
        val = abs_x
        slp = sleep(val)
        print("X: {} Y: {}, slp: {}".format(abs_x, abs_y, slp))
        if val  < -10:
            move_clockwise(slp)
        elif val > 10:
            move_counterclockwise(slp)
except KeyboardInterrupt:
    pass   
spi.close()
GPIO.cleanup()
