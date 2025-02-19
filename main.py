from tkinter import *
from tkinter import Label


words_before = 0


from twilio.twiml.voice_response import Start


def check_field():
    text = text_field.get("1.0", "end-1c")
    text_length = len(text)
    return text_length


def count_time():
    """Checks if new words are added every 10 seconds. If not, clears the text field."""
    global words_before
    new_count = check_field()

    if new_count > words_before:
        words_before = new_count  # Update word count
        print(new_count)
    else:
        clean_field()
        words_before = 0  # Reset count after clearing

    root.after(5000, count_time)

def clean_field():
    text_field.delete("1.0", "end")


# region UI
root = Tk()
root.title("Word Vanish")
root.minsize(500, 300)
root.config(padx=30, pady=30)

window_title = Label(text="Practice your writing")
window_title.grid(column=0, row=0, columnspan=3)

text_field = Text(width=60, height=10, pady=10, padx=10)
text_field.grid(column=0, row=2)

button_start = Button(text='Start', anchor='center', width=10, command=count_time)
button_start.grid(column=0, row=3, pady=(5, 5), padx=(15, 5), sticky="e")

root.mainloop()
# endregion
