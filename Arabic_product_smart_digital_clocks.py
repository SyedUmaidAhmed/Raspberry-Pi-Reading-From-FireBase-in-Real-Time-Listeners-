#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import tkinter as tk
from tkinter import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

mydbUrl='https://prayertimes-arabicclocksfirebaseio.com/'
myAdminId='admin1901'
myPwd='times123'
# Fetch the service account key JSON file contents
cred = credentials.Certificate('prayerTimeKeyvalues.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': mydbUrl
})

primaryKey=''
ref = db.reference('MOSQUE_DETAIL')
snapshot = ref.order_by_child('adminId').equal_to(myAdminId).get()
for value in snapshot.items():
    primaryKey=value[0]
    #print('\n\n\t{0}'.format(value[1]['mosque_name']))


def tick(time1 =''):    
    time2 = time.strftime('%I:%M:%S')
    if time2 != time1:
        time1 = time2
        clock_frame.config(text=time2)
    clock_frame.after(200, tick)

def Heads_namaz():
    heads.config(text="o ﻦﻳﺪﻟﺍ ﺩﺎﻤﻋ ﺓﻼﺼﻟﺃ  ﻢﻠﺳﻭ ﻪﻴﻠﻋ ﷲ ﻰﻠﺻ ﷲ ﻝﻮﺳﺭ ﻝﺎﻗ")



def listener(event):
    ref2 = db.reference('MOSQUE_DETAIL/'+primaryKey)
    snapshot = ref2.get()
    fajar.config(text="ﺮﺠﻓ          {0}".format(snapshot['prayer_times']['fajar']))
    duhr.config(text="ﺮﻬﻇ           {0}".format(snapshot['prayer_times']['zohar']))
    asar.config(text="ﺮﺼﻋ           {0}".format(snapshot['prayer_times']['asar']))
    maghrib.config(text="ﺏﺮﻐﻣ        {0}".format(snapshot['prayer_times']['maghrib']))
    esha.config(text="ﺀﺎﺸﻋ          {0}".format(snapshot['prayer_times']['isha']))
    Jummah.config(text="ﺔﻌﻤﺟ          {0}".format(snapshot['prayer_times']['jumma']))
    

root = tk.Tk()


heads = tk.Label(root, font=('arial 25 bold'),bg ='black', fg='WHITE')
heads.pack(fill='both', expand=1)

clock_frame = tk.Label(root, font=('arial 100 bold'),bg ='black', fg='WHITE')
clock_frame.pack(fill='both', expand=1)

fajar = tk.Label(root, font=('arial 50 bold'),bg = 'black',anchor=N, fg='white')
fajar.pack(fill='both', expand=1)

duhr = tk.Label(root, font=('arial 50 bold'),bg = 'black',anchor=N, fg='white')
duhr.pack(fill='both', expand=1)

asar = tk.Label(root, font=('arial 50 bold'),bg = 'black',anchor=N, fg='white')
asar.pack(fill='both', expand=1)

maghrib = tk.Label(root, font=('arial 50 bold'),bg = 'black',anchor=N, fg='white')
maghrib.pack(fill='both', expand=1)


esha = tk.Label(root, font=('arial 50 bold'),bg = 'black',anchor=N, fg='white')
esha.pack(fill='both', expand=1)


Jummah = tk.Label(root, font=('arial 50 bold'),bg = 'black',anchor=N, fg='white')
Jummah.pack(fill='both', expand=1)




#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.geometry("%dx%d+0+0" % (w, h))
Heads_namaz()

root.attributes('-fullscreen', True)
root.configure(background="lightgreen")
tick()
ref = db.reference('MOSQUE_DETAIL/'+primaryKey).listen(listener)

root.mainloop()
    
