import turtle
t = turtle.Turtle()

t.shape('turtle')


def regular_polygon(n, l):
    """Правильный многоугольник с n сторонами длины l"""
    for step in range(n):
        t.forward(l)
        t.left(360/n)


t.right(90)
L = 0.5
for i in range(20):
    regular_polygon(360, 1)
    t.left(180)
    regular_polygon(360, 1)
    L += 0.1
