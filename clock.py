from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)  # config() is used to change the text of the label
    label.after(1000, time)  # after 1000ms, call time() again to update the time display


label = Label(root, font=("ds-digital", 80, "bold"), background="black", foreground="cyan")  # create a label with font, background and foreground color

# pack() is used to display the label,
# anchor is used to align the label to the center,
# fill is used to fill the label to the whole window,
# expand is used to expand the label to the whole window
label.pack(anchor="center", fill="both", expand=1)

time()

mainloop()  # we call mainloop() to run the application
