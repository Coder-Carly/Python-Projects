import pgzrun
from random import randint

TITLE="Good Shot"
WIDTH=500
HEIGHT=500

message=""

al=Actor("Alien")
al.pos=50,50



def draw():
    screen.clear()
    screen.fill(color=(128,0,0))
    al.draw()
    screen.draw.tect(message,center=(400,10), fontsize=30)

def place_alien():
    al.x=randint(50, WIDTH-50)
    al.y=randint(50, HEIGHT-50)

def on_mouse_down(pos):
    global message
    if al.collidepoint(pos):
        message="Good Shot"
        place_alien()
    else:
        message("You Missed")

place_alien()
pgzrun.go()