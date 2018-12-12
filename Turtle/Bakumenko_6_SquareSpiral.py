import turtle
t = turtle.Turtle()
t.shape('turtle')

L = 10
for i in range(40):
    """Квадратная спираль из 40 сторон, длины которых: 10+5n"""
    t.forward(L)
    t.left(90)
    L += 5
