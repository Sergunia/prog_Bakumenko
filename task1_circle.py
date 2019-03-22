from tkinter import *

root = Tk()
root.geometry('800x600')        # размер окна 800x600
canv = Canvas(root, bg='white') # создать в окне root, фон - белый
canv.pack(fill=BOTH, expand=1)  # размер - максимально возможный в обе стороны

x = y = 400 # координаты центра круга
r = 150 # радиус
color = 'green'


canv.create_oval(x-r, y-r, x+r, y+r, fill = color)


mainloop()
