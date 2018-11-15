import math
from tkinter import *
import time

time_counter = 0
g = 9.8  # Ускорение свободного падения для снаряда.


class Cannon:
    max_velocity = 100


    def __init__(self, canvas):
        self.canvas = canvas
        self.x = x = -30
        self.y = y = 550
        self.shell_num = None  # TODO: оставшееся на данный момент количество снарядов
        self.direction = math.pi/4
        self.power = 0
        self.power_speed = 0
        self.cannon_diametr = 80
        self.line_length = 80
        self.line = canv.create_line(x + 30, y + 30,
                                     x + 110,
                                     y + 110,
                                     width=20, fill="red")
        self.oval = canv.create_oval(x, y,
                                     x + self.cannon_diametr,
                                     y + self.cannon_diametr,
                                     outline="black", fill="black")


    def aim(self, x, y):
        """
        Меняет направление direction так, чтобы он из точки
         (self.x, self.y) указывал в точку (x, y).
        :param x: координата x, в которую целимся
        :param y: координата y, в которую целимся
        :return: None
        """

        self.direction = math.atan((self.y - y)/(self.x - x))

        self.draw(self.x + 40, self.y + 40)


    def fire(self):
        """
        Создаёт объект снаряда (если ещё не потрачены все снаряды)
        летящий в направлении угла direction
        со скоростью, зависящей от длительности клика мышки
        :param dt:  длительность клика мышки, мс
        :return: экземпляр снаряда типа Shell
        """
        print(self.stop_time)
        print(self.start_time)
        self.time_length = self.stop_time - self.start_time
        self.power_speed = (self.power * self.time_length)/3
        shell = Shell(self.x + 40 + self.line_length*math.cos(self.direction),
                      self.y + 40 + self.line_length*math.sin(self.direction),
                      self.power_speed, self.power_speed, self.canvas, self.direction)

        shells.append(shell)
        print(self.time_length)

    def draw(self, x_gun, y_gun):
        """
        Рисует дуло пушки, которое движется в зависимости от перемещений мышки
        :return:
        """
        global y_end
        self.canvas.delete(self.line)
        x_start = x_gun + math.cos(self.direction)*self.cannon_diametr/8
        y_start = y_gun + math.sin(self.direction) * self.cannon_diametr / 8
        x_end = x_gun + self.line_length*math.cos(self.direction)
        y_end = y_gun + self.line_length*math.sin(self.direction)
        self.line = self.canvas.create_line(
            x_start,
            y_start,
            x_end,
            y_end, width=20, fill="red"
        )
        if y_end > 500:
            y_end = 500





class Shell:
    global standard_radius
    standard_radius = 30

    def __init__(self, x, y, Vx, Vy, canvas, direction):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.direction = direction
        self.r = standard_radius
        x1 = x - standard_radius
        y1 = y - standard_radius
        x2 = x + standard_radius
        y2 = y + standard_radius
        self.delta_x = 0
        self.delta_y = 0


        self.canvas = canvas

        self.oval = self.canvas.create_oval(x1, y1, x2, y2, fill='red', outline="pink")


    def go(self, dt):
        """
        Сдвигает снаряд исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt: время элементарного перемещения
        :return: Движущийся снаряд
        """

        ax, ay = 0, g
        self.delta_x = self.Vx * dt * math.cos(self.direction) + ax * (dt ** 2) / 2
        self.delta_y = self.Vy * dt * math.sin(self.direction) + ay * (dt ** 2) / 2
        self.x += self.delta_x
        self.y += self.delta_y
        self.Vx += ax * dt
        self.Vy += -ay * dt

        self.draw()

        if self.y > 600:
            self.canvas.delete(self.oval)
        if self.x > 800:
            self.Vx = -self.Vx


    def draw(self):
        """
        Рисует движущийся снаряд
        :return:
        """
        self.canvas.move(self.oval, self.delta_x, self.delta_y)


    def detect_collision(self, other):
        """
        Проверяет факт соприкосновения снаряда и объекта other
        :param other: объект, который должен иметь поля x, y, r
        :return: логическое значение типа bool
        """

        length = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return length <= self.r + other.r



class Target:
    standard_radius = 5

    def __init__(self, x, y, Vx, Vy):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.r = standard_raduis

    def go(self, dt):
        """
        Сдвигает шарик-мишень исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt:
        :return:
        """

        ax, ay = 0, g
        self.x += self.Vx * dt
        self.y += self.Vy * dt
        self.Vx += ax * dt
        self.Vy += - ay * dt

        # TODO: Шарики-мишени должны отражаться от стенок

    def collide(self, other):
        """
        Расчёт абсолютно упругого соударения
        :param other:
        :return:
        """

        pass  # TODO


def mouse_move_handler(event):
    """
    Направляет дуло пушки в сторону курсора
    :param event: перемещение курсора по экрану
    :return: Координаты курсорв мыши
    """
    cannon.aim(event.x, event.y)


def tick():
    """
    Считает время нажатия клавиши мыши
    :return:
    """
    global time_counter
    time_counter += 1
    for shell in shells:
        shell.go(0.1)

    root.after(10, tick)


def time_start(event):
    """
    Включает счетчик в момент нажания левой клавиши мыши
    :param event: Момент нажатия левой клавиши
    :return: Начальное значение времени
    """
    global time_counter
    cannon.start_time = time_counter


def time_stop(event):
    """
    Выключает счетчик после отпускания левой клавиши
    Обнуляет счетчик
    Запускает снаряд в момент момент отпускания левой клавиши
    :param event: Момент отпускания левой клавиши
    :return: Конечное значение времени
    """
    global time_counter
    cannon.stop_time = time_counter
    cannon.fire()
    time_counter = 0

def power_maker(event): 
    cannon.power = power_scale.get() 


power_scale = Scale(orient=HORIZONTAL, length=300, 
from_=0, to=10, tickinterval=1, resolution=1) 
power_scale.pack() 
power_scale.set(1) 


root = Tk() 
fr = Frame(root) 
root.geometry('800x600') 
canv = Canvas(root, bg='white') 
canv.pack(fill=BOTH, expand=1) 

canv.bind('<Motion>', mouse_move_handler) 
canv.bind("<ButtonPress-1>", time_start) 
canv.bind("<ButtonRelease-1>", time_stop) 
power_scale.bind("<Motion>", power_maker)
shells = []

cannon = Cannon(canv)

tick()
root.mainloop()
