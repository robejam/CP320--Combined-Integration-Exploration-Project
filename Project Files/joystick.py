import spidev
import time

LR_CHANNEL = 1
UD_CHANNEL = 0
JOYSTICK_SLEEP_SECONDS = 0.1

NEUTRAL_X_POS = 516
NEUTRAL_Y_POS = 506

spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1250000

def read_channel(adc_channel):
	adc=spi.xfer2([1,(8+adc_channel)<<4,0])
	data=((adc[1]&3)<<8) +adc[2]
	return data

def abs_x_pos(lr_pos):
	if lr_pos > NEUTRAL_X_POS:
		abs_pos = lr_pos - NEUTRAL_X_POS
	elif lr_pos < NEUTRAL_X_POS:
		abs_pos = -1*(NEUTRAL_X_POS-lr_pos)
	else:
		abs_pos = 0
	return abs_pos

def abs_y_pos(ud_pos):
	if ud_pos > NEUTRAL_Y_POS:
		abs_pos = ud_pos - NEUTRAL_Y_POS
	elif ud_pos < NEUTRAL_Y_POS:
		abs_pos = -1*(NEUTRAL_Y_POS-ud_pos)
	else:
		abs_pos = 0
	return abs_pos	

try:
	while True:
		lr_pos = read_channel(LR_CHANNEL)
		ud_pos = read_channel(UD_CHANNEL)
		abs_x = abs_x_pos(lr_pos)
		abs_y = abs_y_pos(ud_pos)
		print("X: {} Y: {}".format(abs_x, abs_y))
		time.sleep(JOYSTICK_SLEEP_SECONDS)
except KeyboardInterrupt:
	pass
		
spi.close()
