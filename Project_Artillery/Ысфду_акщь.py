from tkinter import *
import random
from math import *


class Cannon:
    def __init__(self, x, y):
        canv.create_arc(x-75, y-100, x+75, y, start=0, extent=180, style=ARC)
        self.m_barrel = None
        self.m_x = x
        self.m_y = y
        self.m_l = 100
        self.m_alpha = pi / 2.
        self.draw()
        return

    def point(self, x, y):
        if x == self.m_x:
            self.m_alpha = pi/2
        else:
            if y > self.m_y:
                if x >= self.m_x:
                    self.m_alpha = 0
                else:
                    self.m_alpha = pi
            else:
                self.m_alpha = atan(-(y-self.m_y)/(x-self.m_x))

        self.draw()
        return

    def draw(self):
        canv.delete(self.m_barrel)
        xc = self.m_x
        yc = self.m_y - 100
        w = 20
        if self.m_alpha >= 0:
            x1 = xc - w / 2 * cos(pi / 2 - self.m_alpha)
            y1 = yc - w / 2 * sin(pi / 2 - self.m_alpha)
            x2 = x1 + self.m_l * cos(self.m_alpha)
            y2 = y1 - self.m_l * sin(self.m_alpha)
            x3 = x2 + w * cos(pi / 2 - self.m_alpha)
            y3 = y2 + w * sin(pi / 2 - self.m_alpha)
            x4 = xc + w / 2 * cos(pi / 2 - self.m_alpha)
            y4 = yc + w / 2 * sin(pi / 2 - self.m_alpha)
        else:
            x1 = xc + w / 2 * cos(pi / 2 - abs(self.m_alpha))
            y1 = yc - w / 2 * sin(pi / 2 - abs(self.m_alpha))
            x2 = x1 - self.m_l * cos(abs(self.m_alpha))
            y2 = y1 - self.m_l * sin(abs(self.m_alpha))
            x3 = x2 - w * cos(pi / 2 - abs(self.m_alpha))
            y3 = y2 + w * sin(pi / 2 - abs(self.m_alpha))
            x4 = xc - w / 2 * cos(pi / 2 - abs(self.m_alpha))
            y4 = yc + w / 2 * sin(pi / 2 - abs(self.m_alpha))

        self.m_barrel = canv.create_polygon([x1, y1, x2, y2, x3, y3, x4, y4])
        return

    def fire(self):
        global shell
        global powder

        x = self.m_x + self.m_l * cos(self.m_alpha)
        y = self.m_y - 100 - self.m_l * sin(self.m_alpha)

        velocity = powder.m_amount * 200
        shell = Shell(x, y, self.m_alpha, velocity)
        return


class Shell:
    def __init__(self, x, y, alpha, velocity):
        print(x, y, alpha, velocity)

        self.m_x0 = x
        self.m_y0 = y
        self.m_x = x
        self.m_y = y
        self.m_alpha = alpha
        self.m_velocity = velocity
        self.m_t = 0
        self.m_shell = canv.create_oval(self.m_x0-10, self.m_y0-10, self.m_x0+10, self.m_y0+10, fill='black')
        return

    def move(self, dt):
        global target, score

        self.m_t += dt
        x = self.m_x0 + self.m_velocity * self.m_t * cos(self.m_alpha)
        y = self.m_y0 - self.m_velocity * self.m_t * sin(self.m_alpha) + 1000 * self.m_t**2 / 2

        if x < 0 or y < 0 or x > 1000 or y > 480:
            self.delete()
            return

        canv.move(self.m_shell, x - self.m_x, y - self.m_y)
        self.m_x = x
        self.m_y = y

        if target.check_hit(x, y):
            score.inc_hits()
            self.delete()
            draw_target()

    def delete(self):
        global shell
        canv.delete(self.m_shell)
        shell = None


class Target:
    def __init__(self, x, y):
        self.m_x = x + 50
        self.m_y = y + 50
        self.m_target = canv.create_oval(x, y, x+100, y+100, fill='red')
        return

    def delete(self):
        canv.delete(self.m_target)

    def check_hit(self, x, y):
        r = sqrt((x - self.m_x)**2 + (y - self.m_y)**2)
        if r < 50:
            return True


class Score:
    def __init__(self):
        self.m_rect = canv.create_rectangle(800, 510, 950, 540)
        self.m_shots = 0
        self.m_hits = 0
        self.text = canv.create_text(870, 525, text="0/0", font='Arial 20')
        return

    def inc_shots(self):
        self.m_shots += 1
        self.show()
        return

    def inc_hits(self):
        self.m_hits += 1
        self.show()
        return

    def show(self):
        score_text = str(self.m_hits) + " / " + str(self.m_shots)
        canv.itemconfig(self.text, text=score_text)
        return


class PowderIndicator:
    def __init__(self, x, y):
        self.m_rect = canv.create_rectangle(x, y, x + 300, y + 30)
        self.m_amount = 0
        self.m_x = x
        self.m_y = y
        self.div_array = []
        return

    def inc(self):
        if self.m_amount < 10:
            self.m_amount += 1
            self.draw_scale()

    def draw_scale(self):
        x = self.m_x + (self.m_amount - 1)*30 + 2
        y = self.m_y + 2
        self.div_array.append(canv.create_rectangle(x, y, x + 26, y + 26, fill='green'))

    def clear(self):
        for div in self.div_array:
            canv.delete(div)

        self.div_array.clear()
        self.m_amount = 0
        return


def shell_timer():
    if shell:
        shell.move(0.1)
        window.after(100, shell_timer)
    return


def powder_timer():
    global mouse_down_status
    if mouse_down_status:
        powder.inc()
        window.after(500, powder_timer)
    return


def mouse_move(event):
    cannon.point(event.x, event.y)
    return


def mouse_down(event):
    if shell is None:
        global mouse_down_status
        mouse_down_status = True
        cannon.point(event.x, event.y)
        window.after(500, powder_timer)
        return


def mouse_up(event):
    if shell is None:
        global mouse_down_status
        mouse_down_status = False
        cannon.fire()
        window.after(100, shell_timer)
        powder.clear()
        score.inc_shots()
        return


def draw_target():
    global target
    if target:
        target.delete()
    target = Target(random.randint(500, 800), random.randint(100, 300))


window = Tk()
window.geometry('1000x600')
canv = Canvas(window,  bg='white')
canv.pack(fill=BOTH, expand=1)

canv.create_rectangle(10, 10, 990, 590)
canv.create_line(10, 480, 990, 480)

# Рисуем пушку
cannon = Cannon(125, 530)
shell = None

# Рисуем мишень
target = None
draw_target()

# Рисуем индикатор уровня пороха
powder = PowderIndicator(30, 510)

# Рисуем панель индикации
score = Score()

mouse_down_status = False

canv.bind('<Button-1>', mouse_down)
canv.bind('<ButtonRelease-1>', mouse_up)

canv.bind('<Motion>', mouse_move)
window.mainloop()