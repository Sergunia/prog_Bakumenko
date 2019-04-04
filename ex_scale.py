from tkinter import *

root = Tk()


def time_handler ():
    global freeze
    speed = scale1.get()
    if speed == 0:
        print()
        freeze = True
    else:
        print ("Значение скорости: ", speed)
        sleep_dt = 1100 - 100*speed
        root.after(sleep_dt, time_handler)


def
    
speed_scale = Scale(root, orient=HORIZONTAL, length=300, from_=0, to=10, tickinterval=1, resolution=1,
                    button1 = Button(root, text="Получить значение")
speed_scale.pack()
speed_scale.set(1)
root.after(10, time_handler)
speed_scale.bind("")

root.mainloop()
