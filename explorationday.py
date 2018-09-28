from ggame import *




ROWS = 20
COLS = 40
CELL_SIZE = 20


def moveRight(event):
    if yes2.x < (COLS-1)*CELL_SIZE:
        yes2.x += CELL_SIZE
def moveLeft(event):
    if yes2.x > 0:
        yes2.x -= CELL_SIZE
def moveUp(event):
    if yes2.y > 0:
        yes2.y -= CELL_SIZE
def moveDown(event):
    if yes2.y < (ROWS-1)*CELL_SIZE:
        yes2.y += CELL_SIZE

if __name__ == '__main__':
    red = Color(0xFF0000,1)
    noOutline = LineStyle(0,black)
    yes = RectangleAsset(CELL_SIZE,CELL_SIZE,noOutline,red)
    yes2=Sprite(yes)

    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown)
    App().run()