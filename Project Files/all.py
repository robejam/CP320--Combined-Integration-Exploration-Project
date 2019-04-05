#Parallax 2-Axis Joystick (#27800) 
#https://www.parallax.com/product/27800

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont
import time
import VL53L0X
import RPi.GPIO as GPIO
import spidev
import time

lr_channel = 1
ud_channel = 0

OLED_ADDRESS = 0x3C
OLED_PORT = 1
OLED_WIDTH = 128
OLED_HEIGHT = 32
OLED_ROTATE = 2

JOYSTICK_SPEED_HZ = 1250000
#JOYSTICK_SPEED_HZ = 1350000

MM_TO_CM = 10
TEXT_X_COORD = 10
TEXT_Y_COORD = 2
DISTANCE_X_COORD = 10
DISTANCE_Y_COORD = 15
SCREEN_COLOUR = "black"
SCREEN_OUTLINE = "white"
TEXT_COLOUR = "white"

# Create a VL53L0X object
tof = VL53L0X.VL53L0X()

# OLED
serial = i2c(port=OLED_PORT, address=OLED_ADDRESS)
device = ssd1306(serial, width=OLED_WIDTH, height=OLED_HEIGHT, rotate=OLED_ROTATE)

# Joystick
spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = JOYSTICK_SPEED_HZ

# Stepper Motor
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

# Determines stepper sleep time based on the current position of the joystick
# The further the joystick is moved, the faster the motor moves
def sleep(val):
    val = abs(val)
    slp = -0.00018*val + 0.1
    
    return slp

# Start sensor ranging
tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

# Font for the OLED display
font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 12)

print("Welcome")
measurement = input("How would you like to output distance? (cm or mm) ")
print("Type Ctrl+C to quit")
try:		
    while True:
        lr_pos = read_channel(lr_channel)
        ud_pos = read_channel(ud_channel)
        abs_x = abs_x_pos(lr_pos)
        abs_y = abs_y_pos(ud_pos)
        val = abs_x
        slp = sleep(val)
        #print("X: {} Y: {}".format(abs_x, abs_y))
        if abs_x  < -10:
            move_clockwise(slp)
        elif abs_x > 10:
            move_counterclockwise(slp)
        distance = tof.get_distance()
        if (distance > 0):
            #print ("%d mm, %d cm" % (distance, (distance/10)))
            with canvas(device) as draw:
               draw.rectangle(device.bounding_box, outline=SCREEN_OUTLINE, fill=SCREEN_COLOUR)
               if (measurement == "cm"):
                   distance = (distance/MM_TO_CM)
               draw.text((TEXT_X_COORD,TEXT_Y_COORD), "Distance:", font=font, fill=TEXT_COLOUR)
               draw.text((DISTANCE_X_COORD,DISTANCE_Y_COORD), str(distance) + " " + measurement, font=font, fill=TEXT_COLOUR)
except KeyboardInterrupt:
    pass

#Clean up functions
print("Goodbye")
tof.stop_ranging()
spi.close()
GPIO.cleanup()
