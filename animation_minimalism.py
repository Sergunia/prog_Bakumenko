import graphics as gr
import time

# The program draws Arjan Janssen's picture
window = gr.GraphWin("Minimalism", 1200, 700)


def main():
    draw_janssen_picture()
    draw_visitor()
    move_visitor()
    window.getMouse()
    window.close()


def draw_janssen_picture():
    """
        Рисует все кроме посетителя:
            draw_floor_plinth_wall() рисует пол, плинтус и стену.
            draw_pictures() рисует картины.
    """
    draw_floor_plinth_wall()
    draw_pictures()


def draw_floor_plinth_wall():
    # FLOOR
    draw_rectangle(0, 560, 1200, 140, 81, 81, 79)
    # PLINTH
    draw_rectangle(0, 540, 1200, 20, 219, 219, 219)
    # WALL
    draw_rectangle(0, 0, 1200, 540, 240, 240, 240)


def draw_pictures():
    # let's define colours of three pictures
    pictures = [((153, 154, 158), (180, 182, 181), (172, 176, 177), (214, 214, 214)),
                ((65, 67, 66), (6, 8, 7), (157, 158, 160), (25, 29, 30)),
                ((202, 204, 203), (213, 213, 213), (223, 223, 223), (23, 27, 26))]

    # Set point (xo,yo): left corner of Picture1
    xo = 350
    yo = 180
    draw_some_pictures(pictures, xo, yo)


def draw_some_pictures(pic, x, y):
    """
        Рисует все элементы из pictures с отступом 200 от предыдущего
    """
    for step in range(len(pic)):
        draw_picture(x, y, pic[step])
        x += 200


def draw_picture(xo, yo, pic):
    """
        Рисует одну картину:
        xо,yо - координаты правой нижней точки левого верхней чсти картины;
        pic - список, хранящий наборы цветов четырёх прямоугольников картины
    """
    draw_rectangle(xo, yo, 50, 80, *pic[0])
    draw_rectangle(xo + 50, yo, 50, 80, *pic[1])
    draw_rectangle(xo, yo + 80, 50, 80, *pic[2])
    draw_rectangle(xo + 50, yo + 80, 50, 80, *pic[3])


def draw_rectangle(x, y, length, height, r, g, b):
    """
        Рисует прямоугольник:
        x,y - координаты правой нижней точки прямоугольника;
        length - длина прямоугольника ;
        height - высота;
        r,g,b - параметры его цвета
    """
    rectangle = gr.Rectangle(gr.Point(x, y), gr.Point(x + length, y + height))
    rectangle.setFill(gr.color_rgb(r, g, b))
    rectangle.setOutline(gr.color_rgb(r, g, b))
    rectangle.draw(window)


def draw_visitor():
    """
        Рисует посетителя на мотоцикле.
            Посетитель:
                head(),
                hand(),
                body().
            Мотоцикл:
                wheel_back(),
                wheel_forward(),
                main_part(),
                rudder(),
                wheel_forward_center(),
                rudder_wheel_stick(),
                rudder_wheel_circle().
            Список Elements содержит в себе все элементы изображения посетителя.
    """
    global wheel_back, wheel_forward, main_part, rudder, wheel_forward_center, rudder_wheel_stick,\
        rudder_wheel_circle, body, head, hand, elements

    wheel_back = gr.Circle(gr.Point(50, 620), 50)
    wheel_back.setFill('grey')
    wheel_back.setOutline('black')

    wheel_forward = gr.Circle(gr.Point(300, 620), 50)
    wheel_forward.setFill('grey')
    wheel_forward.setOutline('black')

    main_part = gr.Rectangle(gr.Point(0, 550), gr.Point(200, 640))
    main_part.setFill('orange')
    main_part.setOutline('orange')

    rudder = gr.Rectangle(gr.Point(150, 510), gr.Point(200, 550))
    rudder.setFill('orange')
    rudder.setOutline('orange')

    wheel_forward_center = gr.Circle(gr.Point(300, 620), 3)
    wheel_forward_center.setFill('gold')
    wheel_forward_center.setOutline('black')

    rudder_wheel_stick = gr.Line(gr.Point(300, 620), gr.Point(150, 460))
    rudder_wheel_stick.setWidth(6)
    rudder_wheel_stick.setOutline('gold')

    rudder_wheel_circle = gr.Circle(gr.Point(150, 460), 5)
    rudder_wheel_circle.setFill('red')
    rudder_wheel_circle.setOutline('black')

    body = gr.Rectangle(gr.Point(60, 450), gr.Point(110, 550))
    body.setFill('red')
    body.setOutline('red')

    hand = gr.Line(gr.Point(110, 460), gr.Point(150, 460))
    hand.setWidth(10)
    hand.setOutline('red')

    head = gr.Circle(gr.Point(85, 420), 30)
    head.setFill('yellow')
    head.setOutline('yellow')

    elements = (wheel_back, wheel_forward, main_part, rudder_wheel_stick, rudder, wheel_forward_center,
                rudder_wheel_circle, body, hand, head)

    for k in range(len(elements)):
        elements[k].draw(window)


def move_visitor():
    for i in range(400):
        for k in range(len(elements)):
            elements[k].move(3, 0)
    time.sleep(0.1)


if __name__ == "__main__":
    main()
