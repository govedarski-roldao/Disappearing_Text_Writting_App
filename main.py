from time import sleep
from tkinter import *
from tkinter import Label
import time

time_left = 10
words_before = 0
words_after = 0

from twilio.twiml.voice_response import Start


def check_field():
    text = text_field.get("1.0", "end-1c")
    words = text.split(" ")
    text_length = len(words)
    return text_length


def count_time():
    global time_left
    global words
    last_count = 0
    while True:
        new_count = check_field()
        if new_count > last_count:




def clean_field():
    global time_left
    text_field.delete("1.0", "end-1c")
    time_left = 10


# region UI
root = Tk()
root.title("Word Vanish")
root.minsize(500, 300)
root.config(padx=30, pady=30)

window_title = Label(text="Practice your writing")
window_title.grid(column=0, row=0, columnspan=3)

text_field = Text(width=60, height=10, pady=10, padx=10)
text_field.grid(column=0, row=2)

button_start = Button(text='Start', anchor='center', width=10, command=check_time)
button_start.grid(column=0, row=3, pady=(5, 5), padx=(15, 5), sticky="e")

root.mainloop()
# endregion
