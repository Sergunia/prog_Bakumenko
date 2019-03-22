from tkinter import *
import random
import graphics as gr

root = Tk()
width = 800
height = 800
root.geometry('400x400')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
balls_amount = 10
balls = []


class Ball:
    def __init__(self, x, y, vx, vy, colour, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.vx = vx
        self.vy = vy
        self.colour = colour
        self.shape = canv.create_oval(self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius,
                         fill=gr.color_rgb(100, 100, blue))

    def draw_a_ball(self):
        self.x = random.randint(100, 700)
        self.y = random.randint(100, 700)
        self.radius = random.randint(5, 80)
        blue = random.randint(50, 255)
        canv.create_oval(self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius,
                         fill=gr.color_rgb(100, 100, blue))


for i in range(balls_amount):
    ball = Ball()
    balls.append(ball)


def tick_handler():
    global balls
    for j in range(len(balls)):
        x_ball, y_ball, dx_ball, dy_ball, circle_ball = balls[j]
        x_ball += dx_ball
        y_ball += dy_ball
        if x_ball < 0:
            dx_ball = -dx_ball
            x_ball = 0
        elif x_ball > width - R:
            dx_ball = -dx_ball
            x_ball = width - R
        if y_ball < 0:
            dy_ball = -dy_ball
            y_ball = 0
        elif y_ball > height - R:
            dy_ball = -dy_ball
            y_ball = height - R
        balls[j] = [x_ball, y_ball, dx_ball, dy_ball, circle_ball]
        canv.move(circle_ball, dx_ball, dy_ball)


def time_handler():
    global freeze
    speed = speed_scale.get()
    if speed == 0:
        freeze = True
        return
    tick_handler()
    sleep_dt = 1100 - 100 * speed
    root.after(sleep_dt, time_handler)


def unfreezer(event):
    global freeze
    if freeze:
        speed = speed_scale.get()
        if speed != 0:
            freeze = False
            root.after(0, time_handler)


speed_scale = Scale(root, orient=HORIZONTAL, length=300, from_=0, to=10, tickinterval=1, resolution=1)

speed_scale.pack()
speed_scale.set(1)
freeze = False
root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)

root.mainloop()