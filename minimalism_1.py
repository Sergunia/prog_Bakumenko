import graphics as gr

window = gr.GraphWin("Minimalism", 1200, 700)

def DrawRectangle(x,y,l,h,r,g,b):
    #x,y - координаты правой нижней точки прямоугольника; l - длина прямоугольника ; h - высота; r,g,b - параметры его цвета
    rectangle = gr.Rectangle(gr.Point(x, y), gr.Point(x+l, y+h))
    rectangle.setFill(gr.color_rgb(r,g,b))
    rectangle.setOutline(gr.color_rgb(r,g,b))
    rectangle.draw(window)
    
def DrawPicture(xo, yo, pic):
    DrawRectangle(xo,yo,50,80,*pic[0])
    DrawRectangle(xo+50,yo,50,80,*pic[1])
    DrawRectangle(xo,yo+80,50,80,*pic[2])
    DrawRectangle(xo+50,yo+80,50,80,*pic[3])
        
def DrawMorePictures(pic,x,y):
    for step in range (len(pic)):
        DrawPicture(x,y,pic[step])
        x += 200

#FLOOR
DrawRectangle(0,560,1200,140,81,81,79)
#PLINTH
DrawRectangle(0,540,1200,20,219,219,219)
#WALL
DrawRectangle(0,0,1200,540,240,240,240)

#PICTURES
Picture1 = [(153,154,158),(180,182,181),(172,176,177),(214,214,214)]
Picture2 = [(65,67,66),(6,8,7),(157,158,160),(25,29,30)]
Picture3 = [(202,204,203),(213,213,213),(223,223,223),(23,27,26)]
Pictures = [Picture1, Picture2, Picture3]

xo = 350
yo = 180
DrawMorePictures(Pictures,xo,yo)
        
window.getMouse()
window.close()
