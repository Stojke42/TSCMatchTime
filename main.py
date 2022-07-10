import math
import tkinter.font as font
from datetime import datetime
from tkinter import *

root = Tk(className=" TSC Time counter")
root.geometry("500x200")
root.resizable(False,False)
myFont = font.Font(weight="bold")
minutes = "00"
seconds = "00"
start_time = 0
donothing = False

clicked = True
buttontext = "Start"
poluvreme = 1


def inttime2strtime(time):
    if time < 10:
        return f"0{time}"
    else:
        return f"{time}"


def sec2time(sec):
    global poluvreme
    if poluvreme == 1:
        return inttime2strtime(math.floor(sec / 60)), inttime2strtime(sec % 60)
    else:
        return inttime2strtime(math.floor(sec / 60) + 45), inttime2strtime(sec % 60)
    # return minutes,seconds


def xinc():
    global donothing, start_time, minutes, seconds

    if donothing and start_time == 0:
        myLabel2.config(text=f"{minutes}:{seconds}",font="bold")
        file = open("Time2OBS.txt", "w")
        file.write(f"{minutes}:{seconds}")
        file.close()
        myLabel2.after(100, xinc)
        start_time = datetime.now()
        deltatime = datetime.now() - start_time
        minutes, seconds = sec2time(deltatime.seconds)

    elif donothing and start_time != 0:
        myLabel2.config(text=f"{minutes}:{seconds}",font="bold")
        file = open("Time2OBS.txt", "w")
        file.write(f"{minutes}:{seconds}")
        file.close()
        myLabel2.after(100, xinc)
        deltatime = datetime.now() - start_time
        minutes, seconds = sec2time(deltatime.seconds)
    else:
        myLabel2.config(text=f"Press button to start counting..",font="bold")
        file = open("Time2OBS.txt", "w")
        file.write(f"")
        file.close()
        myLabel2.after(100, xinc)


def onclick():
    global clicked, donothing, start_time, minutes, seconds, poluvreme
    poluvreme = 1
    if clicked:
        clicked = False
        Buttontext = "Stop"
        ButtonDisable = "disabled"
        myButton["text"] = Buttontext
        myButton2["state"] = ButtonDisable
        donothing = True
    else:
        minutes = "00"
        seconds = "00"
        start_time = 0
        clicked = True
        Buttontext = "Start First half time"
        ButtonDisable = "active"
        myButton["text"] = Buttontext
        myButton2["state"] = ButtonDisable
        donothing = False


def onclick2():
    global clicked, donothing, start_time, minutes, seconds, poluvreme
    poluvreme = 2
    if clicked:
        clicked = False
        Buttontext = "Stop"
        ButtonDisable = "disabled"
        myButton2["text"] = Buttontext
        myButton["state"] = ButtonDisable
        donothing = True
    else:
        minutes = "45"
        seconds = "00"
        start_time = 0
        clicked = True
        Buttontext = "Start Second half time"
        ButtonDisable = "active"
        myButton2["text"] = Buttontext
        myButton["state"] = ButtonDisable
        donothing = False


myLabel2 = Label(root)
myButton = Button(root, text="Start First half time", state="active", width=30, height=2, command=onclick)
myButton['font'] = myFont
myButton2 = Button(root, text="Start Second half time", state="active", width=30, height=2, command=onclick2)
myButton2['font'] = myFont
myLabel2.place(relx=0.5, rely=0.1, anchor=CENTER)
myButton.place(relx=0.5, rely=0.4, anchor=CENTER)
myButton2.place(relx=0.5, rely=0.7, anchor=CENTER)
xinc()

root.mainloop()
