import time
import board
import busio
import csv
import adafruit_vl53l0x

csvfile = "reads.csv"
flag = False

i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

x = 0
y = 0
delay = 1

while (flag == False):
    print('time: {0}sec '.format(x) + 'range: {0}mm'.format(y))
    y = vl53.range
    x += delay
    time.sleep(delay)
    
    