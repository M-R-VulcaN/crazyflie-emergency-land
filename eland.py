#!/usr/bin/python3
from guizero import App, Text, TextBox, PushButton
import RPi.GPIO as GPIO
import threading
import time
import send_emergency_land

ELAND_PIN = 40

MIN_RANGE = 20
MAX_RANGE = 30

GPIO.setmode(GPIO.BOARD)
# GPIO.setup(ELAND_PIN, GPIO.IN)
GPIO.setup(ELAND_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

eland_activated = False
stop_eland = False
count = 0

def button_press(action):
    global uri_num
    # if uri_num in range(MIN_RANGE, MAX_RANGE):
    if MIN_RANGE <= uri_num <= MAX_RANGE:
        uri_num += 1 * action
        if uri_num < MIN_RANGE:
            uri_num = MIN_RANGE
        if uri_num > MAX_RANGE:
            uri_num = MAX_RANGE
        text.value = "radio://0/"+str(uri_num)+"/2M"
        # drone_uri = "radio://0/120/E7E7E7E7"+str(uri_num)+"/2M"
        text.size = 32
    else:
        pass

def activate_eland(uri):
    ## uri = "radio://0/80/2M"  ##CHANGE THIS
    ## "radio://0/120/E7E7E7E7"+str(uri_num)+"/2M"
    print("e-land is active! press the e-land button.\nuri: " + str(uri))
    print("Activated!")
    global stop_eland
    while(True):
        if stop_eland:
            print("Diactivated!")
            stop_eland = False
            break

        if(GPIO.input(ELAND_PIN)==GPIO.LOW):
            # try:
            print("activated emergency landing!")
            text.value = "Activated!"
            print(uri)
            if (not send_emergency_land.main(str(uri))):
                print("wrong uri")
                text.value = "URI not found"

            time.sleep(1.5)
            text.value = "radio://0/"+str(uri_num)+"/2M"
        else:
            pass
            # print("...")
    
def set_uri():
    global eland_activated
    eland_activated = not eland_activated # toggle the value True/False
    print(eland_activated)

    global uri_num
    global stop_eland
    # uri = str(text.value)
    uri = "radio://0/120/2M/E7E7E7E7"+str(uri_num)

    t = threading.Thread(target=activate_eland, args=(uri, ))

    if(eland_activated):
        set_text.value = "ON"
        set_text.text_color = "#66FF00"
        eland_text.value = "Activated"
        eland_text.text_color = "#66FF00"

        t.start()
    else:
        set_text.value = "OFF"
        set_text.text_color = "#FF160C"
        eland_text.value = "Disactivated"
        eland_text.text_color = "#FF160C"

        stop_eland = True
        try:
            t.join()
        except Exception as e:
            print(e)
            pass   



# Set up the app
app = App(title="emergency landing pi", bg = "black")
app.set_full_screen()

uri_num = MIN_RANGE
drone_uri = 0

text = Text(app, text="radio://0/"+str(uri_num)+"/2M", size=26, font="Times New Roman", color="white")

button = PushButton(app, lambda: button_press(1), text="Plus", align ="right", width = 10, height = 3)
button.bg = "white"

button = PushButton(app, lambda: button_press(-1), text="Minus", align ="left", width = 10, height = 3)
button.bg = "white"

set_text = Text(app, text="", size=32, font="Times New Roman", color="red")
set_text.focus()

eland_text = Text(app, text="", size=16, font="Times New Roman", color="white")
eland_text.value = "Disactivated"
eland_text.focus()
eland_text.text_color = "#FF160C"

button = PushButton(app, lambda: set_uri(), text="Set", align ="bottom", width = 10, height = 3)
button.bg = "white"

app.display()
