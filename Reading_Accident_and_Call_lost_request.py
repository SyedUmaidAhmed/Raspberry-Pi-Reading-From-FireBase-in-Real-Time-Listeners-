#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase import firebase
import RPi.GPIO as GPIO
from guizero import App,Text, Picture
import sys
import os
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


from twilio.rest import Client
client = Client("Ahdfhsdhfhdgsfsdde6", "b2hdhahsdasdac5dfe281cf")

mydbUrl='https://mapapp-632423948.firebaseio.com'

cred = credentials.Certificate('mapapp-91a9f-firebase-adminsdk-pr11y-7637428734.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': mydbUrl
})



ref = db.reference('DatabaseEmergencyNumber')
ref2 = db.reference('LatLng')
ref3 = db.reference('DatabaseIncomingNumber')
ref4 = db.reference('HelmetReq')


def listener(event):
    refa = db.reference('DatabaseEmergencyNumber')
    snapshot = refa.order_by_key().limit_to_last(1).get() #EmergencyNo
    for key,val in snapshot.items():
        a=val
    prev_input=0
    input = GPIO.input(24)
    if ((not prev_input) and input):
        print("Button pressed")
        client.messages.create(to=val, 
                       from_="+13343846306", 
                       body="Please call me and tell about message!")
    prev_input=input
    time.sleep(0.05)


def listener3(event):
    refc = db.reference('DatabaseIncomingNumber')
    snapshot = refc.order_by_key().limit_to_last(1).get() #Incoming_call
    for key,val in snapshot.items():
        
        window = tk.Tk()
        window.configure(background='white')
        window.title("Someone is Calling")
        window.geometry("300x300")
        label_1= Label(window,text=val,width=40, height=9,font="Arial")
        label_1.pack()        
        
        path = "tele.gif"

        img = ImageTk.PhotoImage(Image.open(path))
        panel = tk.Label(window, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        window.after(3000, lambda: window.destroy())
        window.mainloop()

def listener4(event):
    refd = db.reference('HelmetReq')    
    snapshot = refd.order_by_key().limit_to_last(1).get() #Incoming_call
#    data = "24.8718N 67.3252E"
#    refe = db.reference('LatLng').push(data)

        
ref = db.reference('DatabaseEmergencyNumber').listen(listener)
ref3 = db.reference('DatabaseIncomingNumber').listen(listener3)
ref4 = db.reference('HelmetReq').listen(listener4)
os.system('navit')
