from tkinter import *

root = Tk()

def my_button_handler(event):
    var.set(1)
    pass

var = tk.IntVar(root, 1)
label = tk.Label(root, text="Do u wanna marry me", font="Arial 30")
rbutton1 = tk.Radiobutton(root, text='Yes', variable=var, value=1, font="Arial 30")
rbutton2 = tk.Radiobutton(root, text='No', variable=var, value=2, font="Arial 30")
button1 = tk.Button(root, twxt='OK')

for widget in label, rbutton1, rbutton2, button1:
    widget.pack()

button1.bind("
