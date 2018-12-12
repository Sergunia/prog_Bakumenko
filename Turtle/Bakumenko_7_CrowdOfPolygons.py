import turtle
t = turtle.Turtle()

t.shape('turtle')


def regular_polygon(n, l):
    """Правильный многоугольник с n сторонами длины l"""
    for step in range(n):
        t.forward(l)
        t.left(360/n)


length = 20
n = 3
for i in range(20):
    t.left(90 + (180/n))
    regular_polygon(n, length)
    t.right(90 + (180/n))
    t.penup()
    t.forward(length/3)
    t.pendown()
    length += 10
    n += 1
