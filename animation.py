import graphics as gr
import time


window = gr.GraphWin("/", 400, 400)
window.setBackground("skyblue")


def main():
    window.getMouse()
    window.close()


def draw_nature():
    sea = gr.Line(gr.Point(0, 250), gr.Point(400, 250))
    sea.setWidth(200)
    sea.setOutline('deepskyblue')

    island = gr.Circle(gr.Point(200, 1175), 900)
    island.setFill('gold')
    island.setOutline('gold')

    stone = gr.Oval(gr.Point(30, 355), gr.Point(120, 320))
    stone.setFill('lightgray')
    stone.setOutline("lightgray")

    sun = gr.Circle(gr.Point(400, 0), 40)
    sun.setFill('yellow')
    sun.setOutline('yellow')

    def draw_cloud(k, m):
        circle_centers = [(k, m), (k + 20, m), (k - 15, m + 20),
                          (k + 10, m + 20), (k + 35, m + 20)]
        for k, m in circle_centers:
            circle = gr.Circle(gr.Point(k, m), 20)
            circle.setFill('white')
            circle.setOutline('white')
            circle.draw(window)

    for q, w in [(40, 30), (120, 80), (230, 30)]:
        draw_cloud(q, w)

    sea.draw(window)
    sun.draw(window)
    island.draw(window)
    stone.draw(window)


def draw_house():
    house = gr.Rectangle(gr.Point(220, 210), gr.Point(380, 350))
    house.setOutline('gray')
    house.setFill("gray")

    roof = gr.Polygon(gr.Point(220, 210), gr.Point(300, 160), gr.Point(380, 210))
    roof.setFill('black')
    roof.setOutline('black')

    windows = gr.Rectangle(gr.Point(265, 250), gr.Point(335, 310))
    windows.setFill('lightblue')
    windows.setOutline('black')

    house.draw(window)
    roof.draw(window)
    windows.draw(window)

    for q, w, e, r in [(300, 250, 300, 310), (265, 280, 335, 280)]:
        line = gr.Line(gr.Point(q, w), gr.Point(e, r))
        line.setWidth(1)
        line.setOutline('black')
        line.draw(window)


def draw_boat():
    global boat, x
    x = 106
    boat = gr.Polygon(gr.Point(x-72, x+123), gr.Point(x+48, x+123), gr.Point(x+18, x+158), gr.Point(x-42, x+158))
    boat.setFill('Chocolate')
    boat.setOutline('Chocolate')
    boat.draw(window)


def draw_mast():
    global mast
    mast = gr.Line(gr.Point(x-2, x+48), gr.Point(x-2, x+123))
    mast.setWidth(2)
    mast.setOutline('black')
    mast.draw(window)


def draw_sails():
    global sail1, sail2
    sail1 = gr.Polygon(gr.Point(x, x+43), gr.Point(x, x+118), gr.Point(x+48, x+118))
    sail1.setFill('white')
    sail1.setOutline('white')

    sail2 = gr.Polygon(gr.Point(x-42, x+113), gr.Point(x-4, x+58), gr.Point(x-4, x+113))
    sail2.setFill('white')
    sail2.setOutline('white')

    sail1.draw(window)
    sail2.draw(window)


def draw_all_boat():
    draw_boat()
    draw_mast()
    draw_sails()


def draw_picture():
    draw_nature()
    draw_all_boat()
    draw_house()


draw_picture()


for i in range(390):
    sail1.move(1, 0)
    sail2.move(1, 0)
    mast.move(1, 0)
    boat.move(1, 0)
    time.sleep(0.1)


main()
