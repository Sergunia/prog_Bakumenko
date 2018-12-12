import turtle
t = turtle.Turtle()

t.shape('turtle')


def draw_star(num, l):
    for i in range(n):
        t.forward(l)
        t.right(180-(180/num))


length = 150
n = 5
draw_star(n, length)

t.penup()
t.forward(200)
t.pendown()
n = 11
draw_star(n, length)
