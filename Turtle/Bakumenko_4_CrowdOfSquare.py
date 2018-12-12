import turtle
t = turtle.Turtle()

t.shape('turtle')
L = 50
for step in range(10):
    for i in range(4):
        t.forward(L)
        t.left(90)
    t.left(180)
    t.penup()
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.pendown()
    L += 20