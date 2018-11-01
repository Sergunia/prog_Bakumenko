import graphics as gr

# The program draws Arjan Janssen's picture
window = gr.GraphWin("Minimalism", 1200, 700)
    

def draw_janssen_picture():
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
    pictures = [((153, 154, 158), (180, 182, 181), (172, 176, 177), (214, 214, 214)), ((65, 67, 66), (6, 8, 7), (157, 158, 160), (25, 29, 30)), ((202, 204, 203), (213, 213, 213), (223, 223, 223), (23, 27, 26))]
    
    # Set point (xo,yo): left corner of Picture1
    xo = 350
    yo = 180
    draw_some_pictures(pictures, xo, yo)


def draw_some_pictures(pic,x,y):
    """
        Рисует все элементы из pictures с отступом 200 от предыдущего
    """ 
    for step in range (len(pic)):
        draw_picture(x, y, pic[step])
        x += 200


def draw_picture(xo, yo, pic):
    """
        Рисует одну картину:
        xо,yо - координаты правой нижней точки левого верхней чсти картины;
        pic - список, хранящий наборы цветов четырёх прямоугольников картины
    """
    draw_rectangle(xo, yo, 50, 80, *pic[0])
    draw_rectangle(xo+50, yo, 50, 80, *pic[1])
    draw_rectangle(xo, yo+80, 50, 80, *pic[2])
    draw_rectangle(xo+50, yo+80, 50, 80, *pic[3])


def draw_rectangle(x, y, length, height, r, g, b):
    """
        Рисует прямоугольник:
        x,y - координаты правой нижней точки прямоугольника;
        length - длина прямоугольника ;
        height - высота;
        r,g,b - параметры его цвета
    """
    rectangle = gr.Rectangle(gr.Point(x, y), gr.Point(x+length, y+height))
    rectangle.setFill(gr.color_rgb(r, g, b))
    rectangle.setOutline(gr.color_rgb(r, g, b))
    rectangle.draw(window)


draw_janssen_picture()

window.getMouse()
window.close()

