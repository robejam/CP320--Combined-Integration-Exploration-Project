import RPi.GPIO as GPIO 
import time

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
						
def move_clockwise():
    for row in stepper_sequence:
        GPIO.output(stepper_pins,row)
        time.sleep(0.01)

def move_counterclockwise():
    for row in reversed (stepper_sequence):
        GPIO.output(stepper_pins,row)
        time.sleep(0.01)

val = input("Enter a value: ")
while input != "q":
   val = int(val)
   if val  < -10:
        move_counterclockwise()
   elif val > 10:
        move_clockwise()
   val = input("Enter a value: ")
GPIO.cleanup()

