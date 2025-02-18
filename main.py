from tkinter import *
from tkinter import Label

# region UI
root = Tk()
root.title("Word Vanish")
root.minsize(500, 300)
root.config(padx=30, pady=30)

window_title = Label(text="Practice your writing")
window_title.grid(column=0, row=0, columnspan=3)

text_field = Text(width=60, height=10, pady=10, padx=10)
text_field.grid(column=0, row=2)

root.mainloop()
# endregion
