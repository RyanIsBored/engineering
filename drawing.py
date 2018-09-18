from ggame import *


red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)


noOutline = LineStyle(0,black)

rectangle = RectangleAsset(200,200,noOutline,blue)
circle = CircleAsset(100,noOutline,green)
triangle = PolygonAsset([(100,200), (350,100), (500,200)],noOutline,red)











Sprite(rectangle,(200,200))
Sprite(circle,(100,300))
Sprite(triangle,(300,100))
App().run()