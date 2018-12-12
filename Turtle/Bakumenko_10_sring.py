import turtle
t = turtle.Turtle()

t.shape('turtle')


def regular_polygon(n, l):
    """Правильный многоугольник с n сторонами длины l"""
    for step in range(n):
        t.forward(l)
        t.left(360/n)


t.left(90)
for i in range(10):
    regular_polygon(180, 0.5)
    regular_polygon(180, 0.1)
