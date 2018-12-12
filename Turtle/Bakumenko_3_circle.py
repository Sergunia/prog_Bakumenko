import turtle
t = turtle.Turtle()

t.shape('turtle')


def regular_polygon(l, n):
    """Правильный многоугольник с n сторонами длины l"""
    for i in range(n):
        t.forward(l)
        t.left(360/n)


# рисует окружность
regular_polygon(0.5, 360)
