from random import randrange as rnd, choice, randrange
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
from math import *
import time


colors = ['blue', 'green', 'red', 'brown']

root = Tk()
root.geometry('1000x600')
canv = Canvas(root, bg='DeepSkyBlue')
canv.pack(fill=BOTH, expand=1)

img = Image.open("StartButton.png").resize((200, 177), Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)


def create_background():
    global big_hill, canv
    big_hill = canv.create_oval(325, 275, 1800, 1000, fill='DarkGreen', outline='DarkGreen')

    def mount():
        mount_11 = canv.create_polygon(100, 350, 175, 150, 175, 600, fill='gray42', outline='gray42')
        mount_12 = canv.create_polygon(175, 600, 175, 150, 250, 350, fill='gray45', outline='gray45')
        snow_1 = canv.create_polygon(137, 250, 175, 150, 220, 250, 185, 221, 175, 250, 159, 224, fill='white',
                                     outline='white')

        mount_21 = canv.create_polygon(300, 375, 450, 175, 450, 600, fill='gray41', outline='gray41')
        mount_22 = canv.create_polygon(450, 600, 450, 175, 725, 550, fill='gray45', outline='gray45')
        snow_2 = canv.create_polygon(393, 250, 450, 175, 505, 250, 465, 235, 450, 250, 425, 237, fill='white',
                                     outline='white')

        mount_31 = canv.create_polygon(100, 400, 300, 75, 300, 600, fill='gray40', outline='gray40')
        mount_32 = canv.create_polygon(300, 600, 300, 75, 550, 525, fill='gray45', outline='gray45')
        snow_3 = canv.create_polygon(223, 200, 300, 75, 370, 200, 330, 170, 300, 200, 275, 165, fill='white',
                                     outline='white')

        mount_41 = canv.create_polygon(-50, 500, 100, 200, 100, 600, fill='gray41', outline='gray41')
        mount_42 = canv.create_polygon(100, 600, 100, 200, 250, 525, fill='gray45', outline='gray45')
        snow_4 = canv.create_polygon(62, 275, 100, 200, 137, 275, 115, 257, 100, 275, 85, 255, fill='white',
                                     outline='white')

    def forest():
        trunks = [(837.5, 300, 837.5, 312), (600, 350, 600, 363), (775, 425, 775, 450),
                  (900, 375, 900, 392), (700, 365, 700, 380), (975, 300, 975, 312)]
        for begin_x, begin_y, end_x, end_y in trunks:
            trunk = canv.create_line(begin_x, begin_y, end_x, end_y, width=4, fill='Sienna')
        trees = [(825, 300, 837.5, 250, 850, 300), (587, 350, 600, 300, 613, 350), (750, 425, 775, 350, 800, 425),
                 (880, 375, 900, 315, 920, 375), (680, 365, 700, 300, 720, 365), (963, 300, 975, 250, 988, 300)]
        for left_x, left_y, up_x, up_y, right_x, right_y in trees:
            tree = canv.create_polygon(left_x, left_y, up_x, up_y, right_x, right_y,
                                       fill='SpringGreen4', outline='SpringGreen4')

    def create_sun():
        sun = canv.create_oval(900, 100, 1100, -100, fill='gold', outline='gold')
        for end_x, end_y in [(795, 25), (835, 50), (810, 80), (860, 90), (875, 130), (925, 125), (950, 170),
                             (980, 130)]:
            sunray = canv.create_line(1000, 0, end_x, end_y, width=2, fill='gold')

    def create_cloud():
        coord_clouds = [(30, 60), (200, 110), (400, 60), (600, 160), (800, 200)]
        for cloud_x, cloud_y in coord_clouds:
            centers = [(cloud_x, cloud_y), (cloud_x + 20, cloud_y), (cloud_x + 40, cloud_y),
                       (cloud_x + 10, cloud_y - 20), (cloud_x + 30, cloud_y - 20)]
            for circle_x, circle_y in centers:
                r = 20
                Cloud = canv.create_oval(circle_x - r, circle_y - r, circle_x + r, circle_y + r, fill='white',
                                         outline='white')

    create_cloud()
    create_sun()
    mount()
    forest()

    for circle_right, circle_up, circle_left, circle_down in [(-300, 500, 300, 1100),
                                                              (600, 400, 1400, 1200),
                                                              (-50, 425, 950, 1425),
                                                              (600, 300, 3000, 2700)]:
        canv.create_oval(circle_right, circle_up, circle_left, 
                         circle_down, fill="ForestGreen", outline='ForestGreen')


class Ball:
    def __init__(self, balls, x=1100, y=400):
        """СОЗДАЕТ ШАРИК В ОПРЕДЕЛЕННОЙ КООРДИНАТЕ, ЗАДАЕТ ЕГО ОСНОВНЫЕ ПАРАМЕТРЫ"""
        self.x = x
        self.y = y
        self.r = 8
        self.vx = 1
        self.vy = 1
        self.color = choice(colors)
        self.points = 3
        self.id = canv.create_oval(self.x - self.r, self.y - self.r, 
                                   self.x + self.r, self.y + self.r, fill=self.color)
        self.Balls = balls
        '''отвечает за "скорость" исчезновения'''
        self.live = 5
        """пока хз что это"""

        self.bum_time = 1
        self.bum_on = 0
        '''задает скорость ветра по иксу и игреку соответственно и выводит на экран'''
        self.vx_wind = randrange(-15, 15, 10)
        self.vy_wind = randrange(-6, 6, 4)
        show_wind(self.vx_wind, self.vy_wind)
        self.text_wind = ""
        """задает ключевые точки рельефа"""
        self.turn_point_1, self.turn_point_2 = 0, 139 
        self.turn_point_3, self.turn_point_4 = 727, 1000
    
    def paint(self):
        """отвечает за отрисовку шарика в новой коордитате"""
        canv.coords(self.id, self.x - self.r, self.y - self.r, 
                    self.x + self.r, self.y + self.r)

    def move(self):
        y = 0
        """Отвечает за движение шара, расчет его скорости, его удаление"""
        if self.turn_point_1 <= self.x <= self.turn_point_2:
            y = 800 - sqrt(300 ** 2 - self.x ** 2)
        elif self.turn_point_2 <= self.x <= self.turn_point_3:
            y = 925 - sqrt(500 ** 2 - (self.x - 450) ** 2)
        elif self.turn_point_3 <= self.x <= self.turn_point_4:
            y = 800 - sqrt(400 ** 2 - (self.x - 1000) ** 2)

        
        if self.y <= y:
            self.vy += 0.1
            self.y += self.vy + self.vy_wind/100
            self.x += self.vx
            #if self.vx
            self.vx *= (0.999-self.vx_wind/1000)
            self.paint()

        else:
            """уничтожает шарик"""
            self.live -= 1
            if self.live < 0:
                self.kill()
                canv.delete(canv.create_text(650, 100,
                     text=self.text_wind,
                     font=("Times New Roman", 20),
                     fill="black"))

        if self.x > 990:
            """отвечает за поворот шарика при ударе о стену"""
            self.vx = - self.vx / 2
            self.x = 989
        elif self.x < 10:
            self.vx = - self.vx / 2
            self.x = 11

    def kill(self):
        canv.delete(self.id)
        try:
            '''отвечает за удаление шарика для перевода хода'''
            self.Balls.pop(self.Balls.index(self))

        except ArithmeticError:
            pass
        
        
class Gun:
    def __init__(self):
        self.f2_power = 10
        self.x = 10
        self.y = 500
        self.f2_on = 0
        self.on = 1
        self.an = 1
        self.dx = 1
        self.dy = 1
        self.min = 0
        self.max = 0
        self.vx = 0
        self.f = 0
        self.time = 0

        self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 20, 
                                   width=5, fill="purple")
        self.oval = canv.create_oval(self.x - 20, self.y - 20, self.x + 20, 
                                     self.y + 20, fill="pink", outline='purple')
        self.turn_point_1, self.turn_point_2 = 0, 139
        self.turn_point_3, self.turn_point_4 = 727, 1000

    def fire_start(self, event):
        print(event.x, event.y)
        if self.on:
            self.f2_on = 1

    def stop(self):
        self.f2_on = 0
        self.on = 0

    def fire_end(self, event):
        print(event.x, event.y)
        if self.on:
            new_ball = Ball(self.Balls)
            new_ball.r += 5
            new_ball.x = self.x
            new_ball.y = self.y
            new_ball.vx = self.f2_power * cos(self.an) / 9
            new_ball.vy = self.f2_power * sin(self.an) / 9
            self.Balls += [new_ball]
            self.f2_on = 0
            self.f2_power = 35

    def moved(self, event):
        print('MOVE')
        t_end = time.time() + 3

        def find_y():
            if self.turn_point_1 <= self.x <= self.turn_point_2:
                self.y = 800 - sqrt(300 ** 2 - self.x ** 2)
            elif self.turn_point_2 <= self.x <= self.turn_point_3:
                self.y = 925 - sqrt(500 ** 2 - (self.x - 450) ** 2)
            elif self.turn_point_3 <= self.x <= self.turn_point_4:
                self.y = 800 - sqrt(400 ** 2 - (self.x - 1000) ** 2)

        def coordination():
            """Сравнивает нынешнее положение пушки с тем, в котором пушка хочет оказаться.
            В зависимость от этого пересчитывает dx"""
            if self.x >= event.x:
                self.dx = - self.dx
                canv.delete(self.oval)
                canv.delete(self.id)
                self.oval = canv.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill="pink",
                                             outline='purple')
                self.id = canv.create_line(self.x, self.y, self.x - 30, self.y - 20, width=5, fill="purple")

                self.max = self.x
                self.min = event.x
            else:
                self.dx = self.dx
                self.max = event.x
                self.min = self.x

        def run():

            if time.time() < t_end:
                if self.min <= self.x <= self.max:
                    self.x = self.x + self.dx
                    if self.turn_point_1 <= self.x <= self.turn_point_2:
                        self.f = 800 - sqrt(300 ** 2 - self.x ** 2)
                        self.dy = self.f - self.y
                        self.y = self.y + self.dy
                        canv.move(self.oval, self.dx, self.dy)
                        canv.move(self.id, self.dx, self.dy)
                    elif self.turn_point_2 <= self.x <= self.turn_point_3:
                        self.f = 925 - sqrt(500 ** 2 - (self.x - 450) ** 2)
                        self.dy = self.f - self.y
                        self.y = self.y + self.dy
                        canv.move(self.oval, self.dx, self.dy)
                        canv.move(self.id, self.dx, self.dy)
                    elif self.turn_point_3 <= self.x <= self.turn_point_4:
                        self.f = 800 - sqrt(400 ** 2 - (self.x - 1000) ** 2)
                        self.dy = self.f - self.y
                        self.y = self.y + self.dy
                        canv.move(self.oval, self.dx, self.dy)
                        canv.move(self.id, self.dx, self.dy)

                root.after(40, run)

        find_y()
        coordination()
        run()
        root.after(40, run())

    def aiming(self, event=0):
        if event:
            if abs(event.x - self.x) < 0.0001:
                event.x += 0.1
            self.an = atan((event.y - self.y) / (event.x - self.x))
            if event.x < self.x:
                self.an += pi

        canv.delete(self.oval)
        canv.delete(self.id)
        self.oval = canv.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill="pink",
                                     outline='purple')
        self.id = canv.create_line(self.x, self.y, self.x - 30, self.y - 20, width=5, fill="purple")

        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            pass

        canv.coords(self.id, self.x, self.y, self.x + 30 * cos(self.an), self.y + 30 * sin(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='purple')


class Game:
    create_background()

    def __init__(self):
        self.moving = []
        self.gamer1 = Gun()
        self.gamer1.x = 10
        self.gamer1.y = 500
        self.gamer2 = Gun()
        self.gamer2.x = 990
        self.gamer2.y = 400
        self.gamer1.Balls = self.moving
        self.gamer2.Balls = self.moving
        self.active_gamer = self.gamer1
        self.unactive_gamer = self.gamer2

        canv.bind('<Button-1>', self.fire_start)
        canv.bind('<Button-3>', self.moved)
        canv.bind('<ButtonRelease-1>', self.fire_end)
        canv.bind('<Motion>', self.aiming)
        self.CONTROL = 0

    def fire_start(self, event):
        self.active_gamer.fire_start(event)

    def fire_end(self, event):
        self.active_gamer.fire_end(event)
        self.active_gamer.stop()

    def aiming(self, event):
        self.active_gamer.aiming(event)

    def power_up(self, event):
        self.active_gamer.power_up(event)

    def moved(self, event):
        if self.CONTROL < 1:
            self.CONTROL += 1
            self.active_gamer.moved(event)

    def round(self):
        self.CONTROL = 0
        if self.active_gamer == self.gamer1:
            self.active_gamer = self.gamer2
            print('Gamer1')
        else:
            self.active_gamer = self.gamer1
            print('Gamer2')

        self.active_gamer.on = 1

        while self.active_gamer.on or self.moving:
            for m in self.moving:
                m.move()
            self.active_gamer.aiming()
            self.active_gamer.power_up()
            canv.update()
            time.sleep(0.01)
        
def show_wind(vx, vy):
    global v_wind_text
    if vx < -5:
        print ("ветер сильно сдувает на запад")
        vx_text = "ветер сильно сдувает на запад"
    elif vx >= -5 and vx < 0:
        print ("ветер слегка сдувает на запад")
        vx_text = "ветер слегка сдувает на запад"
    elif vx >= 0 and vx <= 5:
        print ("ветер слегка сдувает на запад")
        vx_text = "ветер слегка сдувает на восток"
    elif vx > 5:
        print ("ветер сильно сдувает на восток")
        vx_text = "ветер сильно сдувает на восток"
    if vy < -2:
        print (" и сильно прибивает к земле")
        vy_text = " и сильно прибивает к земле"
    elif vy >= -2 and vy < 0:
        print (" и слегка прибивает к земле")
        vy_text = " и слегка прибивает к земле"
    elif vy >= 0 and vy <= 2:
        print (" и слегка поднимает к небу")
        vy_text = " и слегка поднимает к небу"
    elif vy > 2:
        print (" и сильно поднимает к небу")
        vy_text = " и сильно поднимает к небу"
    print("vx_wind = ", vx, "vy_wind = ", vy)
    v_wind_text = vx_text+vy_text
    canv.create_text(450, 10,
                     text=v_wind_text,
                     font=("Times New Roman", 20),
                     fill="black")
        
def start_callback():
    global root, canv
    canv.destroy()

    canv = Canvas(root, bg='DeepSkyBlue')
    canv.pack(fill=BOTH, expand=1)

    create_background()

    game1 = Game()
    while 1:
        game1.round()


def help_callback():
    help_window = Toplevel(root)
    help_window.geometry("400x400")
    text = Text(help_window, width=100, height=100, font=Font(family='Helvetica', size=10))
    text.pack(expand='yes', fill='both')

    with open("game_rules.txt", mode="r", encoding="utf-8") as f:
        text.insert(END, f.read())

    Button(help_window, text='OK', command=help_window.destroy).pack(side=BOTTOM, pady=30)
    return


def start_screen():
    global root, canv

    canv.create_text(650, 100,
                     text="Добро пожаловать в игру",
                     font=("Times New Roman", 30),
                     fill="black")
    
    canv.create_text(680, 230,
                     text="ТАНКИ",
                     font=("Times New Roman", 40),
                     fill="black")

    help_button = Button(canv, text="Правила игры", bg="ForestGreen", command=help_callback).pack(padx=20, pady=20, side=BOTTOM, anchor=E)
    start_button = Button(canv, image=img_photo, bg="ForestGreen", activebackground="ForestGreen",
                          command=start_callback).pack(side=BOTTOM)


start_screen()

root.mainloop()