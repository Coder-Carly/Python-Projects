import pgzrun
from random import randint
WIDTH = 300
HEIGHT = 300

def draw():
    r=Rect((0,0), (100, 150))
    r.center = 150, 150
    screen.draw.rect(r,(120,130,120))
    r2=Rect((0,0), (100, 150))
    r2.center = 200, 200
    screen.draw.filled_rect(r2,(255,0,0))
pgzrun.go()