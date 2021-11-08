#!/usr/bin/python3

from guizero import App, Text, TextBox, PushButton, Picture, Window
import time

add_uri = 10
take_uri = -10
uri_num = 0
my_name = 0

def set_uri():
    uri_num += 10
    uri_show.value = uri_num.value


def say_my_name():
	my_name+=add_uri
    welcome_message.value = my_name.value


# def emergency_land():

# 	window.visible = True
# 	time.sleep(2)


app = App(title="emergency landing pi")
app.set_full_screen()	

welcome_message = Text(app, text="radio uri:", size=32, font="Times New Roman", color="black")

radio_uri = Text(app, text="radio://0/"+ str(uri_num) +"/2M", size=32, font="Times New Roman", color="black")

# uri_show = Text(app, text = uri_num, size=32, font="Times New Roman", color="black")
# uri = TextBox(app, height=50)
#update_text = PushButton(app, command=set_uri, text="add_uri")
welcome_message = Text(app, text="Welcome to my app", size=32, font="Times New Roman", color="black")
# my_name = TextBox(app, width=30)

my_name = Text(app, text=str(my_name))
update_text = PushButton(app, command=say_my_name, text="Display my name")

# window = Window(app, visible=False)

# Picture(window, image="newimage.png",width=100, height=100,grid=[500,500])

app.display()