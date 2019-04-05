import spidev
import time
lr_channel = 1
ud_channel = 0

spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1250000

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
	

while True:
	lr_pos = read_channel(lr_channel)
	ud_pos = read_channel(ud_channel)
	abs_x = abs_x_pos(lr_pos)
	abs_y = abs_y_pos(ud_pos)
	print("X: {} Y: {}".format(abs_x, abs_y))
	time.sleep(0.1)

spi.close()

