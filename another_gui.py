#!/usr/bin/python3
from guizero import App, Text, TextBox, PushButton
import RPi.GPIO as GPIO
import time
import send_emergency_land
#import cflib.crtp

eland_pin = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(eland_pin, GPIO.IN)

set_button_pressed = False
# Method to display the greeting
def display_greeting(action):
    global name
    name += 10 * action
    text.value = "radio://0/" + str(name) + "/2M"

def set_uri():
    global name
    uri = str(text.value)
    set_text = Text(app, text="", size=32, font="Times New Roman", color="black")
    set_text.value = "SET"
    eland_text = Text(app, text="press the e-land button", size=8, font="Times New Roman", color="black")
    set_button_pressed = True

    ### activate eland pins
    #option 1: add a thread that will do the following and a thread that will check for buttons press
    #option 2: find another way to do it wihtout using an infinity loop/ find a way to bypass "app.display()"
    # time.sleep(0.5)
    # while(True):
    #     time.sleep(0.2)
    #     if(GPIO.input(eland_pin)==GPIO.LOW):
    #         print("activated emergency landing!")
    #         print(uri)
    #         print(type(uri))
    #         send_emergency_land.main(uri)
    #         time.sleep(3)
    #     else:
    #         print("...")


# Set up the app
app = App(title="emergency landing pi")
app.set_full_screen()	
name = 0
text = Text(app, text="set uri", size=32, font="Times New Roman", color="black")
if(set_button_pressed == False):
    button = PushButton(app, lambda: display_greeting(1), text="Plus", align ="right", width = 10, height = 3)
    button = PushButton(app, lambda: display_greeting(-1), text="Minus", align ="left", width = 10, height = 3)
    button = PushButton(app, lambda: set_uri(), text="Set", align ="bottom", width = 10, height = 3)

app.display()