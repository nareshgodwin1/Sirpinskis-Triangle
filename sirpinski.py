import random
import sys
import pygame as pg

n = random.randint(1,3)

pg.init()

clock = pg.time.Clock()
FPS = 60

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

gameDisplay = pg.display.set_mode((601,600))
gameDisplay.fill(black)

pg.draw.circle(gameDisplay, yellow,(300, 2), 2)
pg.draw.circle(gameDisplay, white,(2, 598), 2)
pg.draw.circle(gameDisplay, white,(599, 598), 2)

x = random.randint(2,599)

Ax = 300
Bx = 2
Cx = 599
Ay = 2
By = 598
Cy = 598


corners = [
    (2,    600), 
    (300,   2), 
    (600,   600)
    ]


x, y = 200, 500
while True:
    clock.tick(FPS)
    pg.draw.polygon(gameDisplay, yellow, [(300,1),(295, 6),(285,5),(294, 12),(290, 20),(300,14),(310,20), (304, 12), (315,5),(305,6)])
    for _ in range(25000):
        (a,b) = random.choice(corners)
        (g,h) = (((a+x)/2),((b+y)/2))
    if g <= 300 and h >= 301:
        pg.draw.circle(gameDisplay, red, (g,h), 1)  
    elif g >= 300 and h >= 301:
        pg.draw.circle(gameDisplay, white, (g,h), 1)
    elif h <= 300:
        pg.draw.circle(gameDisplay, green, (g,h), 1)
    
    x = g
    y = h

    
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            sys.exit()
    pg.display.update()




