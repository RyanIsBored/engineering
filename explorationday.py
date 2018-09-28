from ggame import *




ROWS = 20
COLS = 40
CELL_SIZE = 20


def moveRight(event):
    if yes2.x < (COLS-1)*CELL_SIZE:
        yes2.x += CELL_SIZE




if __name__ == '__main__':
    red = Color(0xFF0000,1)
    noOutline = LineStyle(0,black)
    yes = RectangleAsset(CELL_SIZE,CELL_SIZE,noOutline,red)
    yes2=Sprite(yes)

    App().listenKeyEvent('keydown','right arrow',moveRight)

    App().run()