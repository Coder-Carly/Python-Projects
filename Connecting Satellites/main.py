import pgzrun
import pygame
from random import randint
from time import time

HEIGHT=800
WIDTH=800
satellites=[]
lines=[]
next_satellite=0
start_time=0
total_time=0
end_time=0
number_of_satellites=8

def create_satellite():
    global satellites,start_time
    for count in range(0, number_of_satellites):
        satellite=Actor("satellite")
        satellite.pos=randint(50,WIDTH-50),randint(50,HEIGHT-50)
        satellites.append(satellite)
    start_time=time()

def draw():
    global total_time
    background_image=pygame.image.load("images/space_background.png")
    scaled_image=pygame.transform.scale(background_image,(WIDTH,HEIGHT))
    screen.blit(scaled_image,(10,10))
    number=1
    for satellite in satellites:
        satellite.draw()
        screen.draw.text(str(number),satellite.pos,fontsize=30,color="white")
        number+=1
    for line in lines:
        screen.draw.line(line[0],line[1],"white")
    if next_satellite < number_of_satellites:
        total_time=time()-start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)

def update():
    pass
def on_mouse_down(pos):
    global next_satellite,lines
    if next_satellite < number_of_satellites:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
            next_satellite+=1
        else:
            lines=[]
            next_satellite=0

create_satellite()
pgzrun.go()
