#Author: Spencer Korb
#Date: 04/16/2019
#Purpose: read sensor readings and push the values into the firebase DB

import RPi.GPIO as GPIO         # GPIO library
import time                     # time library
import board                    # data values to be transmitted to sensor
import busio                    # input/output for data connection with sensor
import adafruit_vl53l0x         # library containing methods for sensor interaction
import requests
import json

#set up GPIO for LED control on board
GPIO.setmode(GPIO.BCM)      # set up GPIO 
GPIO.setup(18, GPIO.OUT)    # set GPIO number 18 for output (3.3v-high, 0v-low)

#variables
TIME_TO_PASS = 1                                        # time constant between HTTP requests
URL = 'https://cosc365-981cd.firebaseio.com/run.json'   # DB URL
data = {"close" :   0,                                  # close: 0 = false, 1 = true
        "dist"  :   0}                                  # dist: 0-255
flag = False                                            # flag to determine operation end on exception thrown
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

#take reading from sensor, interpret closeness, PUT onto DB

## get post from the DB (to be commented out once PUT is ensured to work) ####
#print("performing initial values via GET")                                  #
#r = requests.get(url = URL)                                                 #
#try:                                                                        #
#    data["close"] = json.loads(r.text)["close"]                             #
#    data["dist"] = json.loads(r.text)["dist"]                               #
#except:                                                                     #
#    print("An error has occurred : application ending")                     #
#    flag = True                                                             #
#finally:                                                                    #
#    print(r)                                                                #
#    print("close = {} : dist = {}".format(data["close"], data["dist"]))     #
#                                                                            #
#time.sleep(TIME_TO_PASS)                                                    #
##############################################################################

## get reading and PUT data into the DB while no exceptions are thrown ######
while(flag != True):                                                        #
                                                                            #
#put new data into previous PUT                                             #
                                                                            #
##test data for PUT###########                                              #
#data = {"close" :   0,      #                                              #
#        "dist"  :   125}    #                                              #
##############################                                              #
                                                                            #
## read from the sensor, perform closeness logic, set values in data ####   #
    data["dist"] = vl53.range                                           #   #
    if(data["dist"] < 255):                                             #   #
        data["close"] = True                                            #   #
        GPIO.output(18, GPIO.HIGH)                                      #   #
    else:                                                               #   #
        data["close"] = False                                           #   #
        GPIO.output(18, GPIO.LOW)                                       #   #
#########################################################################   #
                                                                            #
## PUT data onto the DB #########################################           #
#    print("performing PUT")                                    #           #
    try:                                                        #           #
        r = requests.put(url = URL, data = json.dumps(data))    #           #
    except:                                                     #           #
        print("An error has occurred : application ending")     #           #
        flag = True                                             #           #
    finally:                                                    #           #
#        print(r)                                               #           #
## wait TIME_TO_PASS before next PUT ############################           #
        time.sleep(TIME_TO_PASS)                                #           #
#################################################################           #
                                                                            #
#############################################################################
