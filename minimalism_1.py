import graphics as gr

#The program draws Arjan Janssen's picture
window = gr.GraphWin("Minimalism", 1200, 700)


def DrawJanssenPicture():
    DrawFloorPlinthWall()
    DrawPictures()


def DrawFloorPlinthWall():
    # FLOOR
    DrawRectangle(0, 560, 1200, 140, 81, 81, 79)
    # PLINTH
    DrawRectangle(0, 540, 1200, 20, 219, 219, 219)
    # WALL
    DrawRectangle(0, 0, 1200, 540, 240, 240, 240)


def DrawPictures():
    # let's define coloures of three pictures
    Picture1 = [(153,154,158), (180,182,181), (172,176,177), (214,214,214)]
    Picture2 = [(65,67,66), (6,8,7), (157,158,160), (25,29,30)]
    Picture3 = [(202,204,203), (213,213,213), (223,223,223), (23,27,26)]
    Pictures = [Picture1, Picture2, Picture3]
    
    # Set point (xo,yo): left corner of Picture1
    xo = 350
    yo = 180
    DrawSomePictures(Pictures,xo,yo)


def DrawSomePictures(pic,x,y):
    """
        Рисует все элементы из Pictures с отступом 200 от предыдущего
    """ 
    for step in range (len(pic)):
        DrawPicture(x, y, pic[step])
        x += 200


def DrawPicture(xo, yo, pic):
    """
        Рисует одну картину:
        xо,yо - координаты правой нижней точки левого верхней чсти картины;
        pic - список, хранящий наборы цветов четырёх прямоугольников картины
    """
    DrawRectangle(xo, yo, 50, 80, *pic[0])
    DrawRectangle(xo+50, yo, 50, 80, *pic[1])
    DrawRectangle(xo, yo+80, 50, 80, *pic[2])
    DrawRectangle(xo+50, yo+80, 50, 80, *pic[3])


def DrawRectangle(x, y, length, height, r, g, b):
    """
        Рисует прямоугольник:
        x,y - координаты правой нижней точки прямоугольника;
        length - длина прямоугольника ;
        height - высота;
        r,g,b - параметры его цвета
    """
    rectangle = gr.Rectangle(gr.Point(x, y), gr.Point(x+length, y+height))
    rectangle.setFill(gr.color_rgb(r,g,b))
    rectangle.setOutline(gr.color_rgb(r,g,b))
    rectangle.draw(window)


DrawJanssenPicture()

window.getMouse()
window.close()
