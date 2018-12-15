from tkinter import *
import graphics as gr
import random as random


clicks = 0
missed = 0
points = 0

x_circle = 0
y_circle = 0
radius = 0


def main():
    # Нажатием кнопки вызываю соответств. функцию
    root = Tk()
    root.geometry('1000x1000')
    canv = Canvas(root, bg='white')
    canv.pack(fill=BOTH, expand=1)

    print("main")
    canv.bind('<Button-1>', left_click)
    canv.pack(fill=BOTH, expand=1)
    root.after_idle(tick)

    mainloop()


def left_click(signal):
    print("left_click")
    global points, missed, clicks
    x = signal.x
    y = signal.y
    global x_circle, y_circle, radius
    if (x - x_circle) ^ 2 + (y - y_circle) ^ 2 <= radius ^ 2 and clicks == 0:
        points += 1
    elif (x - x_circle) ^ 2 + (y - y_circle) ^ 2 > radius ^ 2 and clicks == 0:
        missed += 1
    clicks += 1


def tick():
    # Pеализует периодические (Т = 2 с) появление круга и последующее его удаление. Выводит количество points, missed.
    print("tick")
    global clicks
    clicks = 0
    canv.delete(ALL)
    draw_circle_wherever()
    canv.create_text(20, 350, text="Points:", font="Verdana 12", anchor="w")
    canv.create_text(100, 350, text=points, font="Verdana 18", anchor="w")
    canv.create_text(20, 380, text="Missed:", font="Verdana 18", anchor="w")
    canv.create_text(130, 380, text=missed, font="Verdana 18", anchor="w")
    root.after(2000, tick)


def draw_circle_wherever():
    print("draw_circle_wherever")
    global x_circle, y_circle, radius
    x_circle = random.randint(150, 650)
    y_circle = random.randint(150, 650)
    radius = random.randint(1, 150)
    red = random.randint(100, 255)
    green = random.randint(100, 255)
    blue = random.randint(100, 255)
    canv.create_oval(x_circle - radius, y_circle - radius, x_circle + radius, y_circle + radius,
                     fill=gr.color_rgb(red, green, blue))


main()
