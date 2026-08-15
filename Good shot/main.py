import pgzrun
from random import randint

TITLE="Shoot the Alien!"
WIDTH=500
HEIGHT=500

message=""
score=0
message2=""

al=Actor("alien")
al.pos=50,50



def draw():
    screen.clear()
    screen.fill(color=(128,0,0))
    al.draw()
    screen.draw.text(message,center=(400,10), fontsize=30)
    screen.draw.text(message2,center=(100,10), fontsize=30)

def place_alien():
    al.x=randint(50, WIDTH-50)
    al.y=randint(50, HEIGHT-50)

def on_mouse_down(pos):
    global message
    global message2
    global score
    if al.collidepoint(pos):
        message="Good Shot!"
        score +=1
        message2="Score: {}".format(score)
        place_alien()
    else:
        message="You missed"
        score-=1
        message2="Score: {}".format(score)
place_alien()
pgzrun.go()