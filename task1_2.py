from tkinter import *
import graphics as gr
import random as random
import math
import time


root = Tk()
root.geometry('1000x1000')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


clicks = 0
missed = 0
points = 0
    
def tick():
    # Pеализует периодические (Т = 2 с) появление круга и последующее его удаление. Выводит количество points, missed.
    root.after(2000, tick)
    global clicks
    clicks = 0
    
    draw_circle_wherever()
    
    canv.create_text(20, 350, text = "Points:", font = "Verdana 12", anchor = "w")
    canv.create_text(100, 350, text = points, font = "Verdana 18", anchor = "w")
    canv.create_text(20, 380, text = "Missed:", font = "Verdana 18", anchor = "w")
    canv.create_text(100, 350, text = missed, font = "Verdana 18", anchor = "w")
    canv.delete(ALL)
    
    # куда надо поставить root.after(2000, tick)

    
def draw_circle_wherever():
    global x_circle, y_circle, radius
    x_circle = random.randint(150, 650)
    y_circle = random.randint(150, 650)
    radius = random.randint(1, 150)
    red = random.randint(100, 255)
    green = random.randint(100, 255)
    blue = random.randint(100, 255)
    canv.create_oval(x_circle - radius, y_circle - radius, x_circle + radius, y_circle + radius, fill = gr.color_rgb(red, green, blue))


def left_click(signal):
    # 
    global points, missed, clicks
    x = signal.x
    y = signal.y
    global x_circle, y_circle
    if (x - x_circle)^2 + (y - y_circle)^2 <= radius^2 and clicks == 0:
        points += 1
    else:
        missed += 1
    clicks += 1


# спросить про root after, почему я не могу написать просто tick()


# Нажатием кнопки вызываю соответств. функцию
canv.bind('<Button-1>', left_click)
canv.pack(fill=BOTH, expand=1)


root.after_idle(tick) # функция tick вызывается после всех отложенных операций
mainloop()
