import turtle
t = turtle.Turtle()

t.shape('turtle')
L = 0.5
for i in range(360):
    t.forward(L)
    t.left(20)
    L += 0.1
