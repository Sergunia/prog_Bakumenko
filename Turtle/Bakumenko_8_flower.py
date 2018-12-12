import turtle
t=turtle.Turtle()

t.shape('turtle')

def Regular_polygon (N, L):
    """Правильный многоугольник с N сторонами длины L"""
    for i in range (N):
        t.forward(L)
        t.left(360/N)
        
for i in range(4):
    Regular_polygon (360, 0.5)
    t.left(180)
    Regular_polygon (360, 0.5)
    t.left(60)
