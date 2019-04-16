#Author: Spencer Korb
#Date: 04/15/2019
#Purpose: test posting, getting, putting, and deleting to/from a firebase DB

import requests
import time
import json

#variables
TIME_TO_PASS = 10                                    #time constant between HTTP requests
name = []                                           #list of name links to DB child entries
got = []                                            #list of data from DB child entries
URL = 'https://cosc365-981cd.firebaseio.com/test'   #DB URL
data = {'1':"Hello",                                #test data to store into DB
        '2':"World"}
data2 = {'1':"Good",                                #test data #2 to put into old data
         '2':"Bye"}

#make a post to the DB
print("performing POST")
r = requests.post(url = URL+".json", data = json.dumps(data))
try:
    posted = r.text
    namelink = json.loads(posted)
    name.append(namelink["name"])
    postURL = (URL+"/"+name[0])
finally:
    print(r)
try:
    print("the posted URL is:"+posted)
    print(postURL)
    time.sleep(TIME_TO_PASS)

#get post from the DB
    print("performing GET (1)")
    r = requests.get(url = postURL+".json")
    try:
        got.append(json.loads(r.text)[1])
        got.append(json.loads(r.text)[2])
    finally:
        print(r)
        print(got[0]+" "+got[1])
    time.sleep(TIME_TO_PASS)

#put new data into previous post
    print("performing PUT")
    r = requests.put(url = postURL+".json", data = json.dumps(data2))
    print(r)
    time.sleep(TIME_TO_PASS)

#get new put data from the DB
    print("performing GET (2)")
    r = requests.get(url = postURL+".json")
    try:
        got[0] = (json.loads(r.text)[1])
        got[1] = (json.loads(r.text)[2])
    finally:
        print(r)
        print(got[0]+" "+got[1])
    time.sleep(TIME_TO_PASS)
    
#delete post from the DB
    print("performing DELETE")
    r = requests.delete(url = postURL+".json")
    print(r)
    
finally:
    print("completed")
