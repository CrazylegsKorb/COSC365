import RPi.GPIO as GPIO         # GPIO library
import time                     # time library
import board                    # data values to be transmitted to sensor
import busio                    # input/output for data connection with sensor
import os
import csv                      # comma separated values library
import adafruit_vl53l0x         # library containing methods for sensor interaction

try:
    os.remove("reads.csv")      # removes previous data file if it exists
    
finally:
    GPIO.setmode(GPIO.BCM)      # set up GPIO 
    GPIO.setup(18, GPIO.OUT)    # set GPIO number 18 for output (3.3v-high, 0v-low)
    
    csvfile = "reads.csv"       # set output file for csv's
    
    close = False               # flag to determine when something is close to the sensor
    flag = True                 # (could be changed to shut off the sensor after reciving
                                #  out of range readings for several seconds)
                            
    i2c = busio.I2C(board.SCL, board.SDA)
    vl53 = adafruit_vl53l0x.VL53L0X(i2c)

    x = 0   # initial x-data value for graphing  
    y = 0   # initial y-data value for graphing
    delay = .1 # delay for read/write for graphing

    while (flag): # constantly runs (may implement auto sensor shutdown)
        if(vl53.range < 200):
            close = True
            GPIO.output(18, GPIO.HIGH)
        else:
            close = False
            GPIO.output(18, GPIO.LOW)
        print('time: {:= 5.1f}sec '.format(x) + 'range: {:= 5}mm '.format(y) + 'close: '+ str(close))
        y = vl53.range
        data = [x, y]
        x += delay
    
        with open(csvfile, "a")as output:
            writer = csv.writer(output, delimiter=",", lineterminator = '\n')
            writer.writerow(data)
        time.sleep(delay)
    
