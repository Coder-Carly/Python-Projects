import pgzrun
import pygame
import random

FONT_option=(255,255,255)
WIDTH=800
HEIGHT=600
CENTRE_X=WIDTH/2
CENTRE_Y=HEIGHT/2
FINAL_LEVEL=6
START_SPEED=10
ITEMS=["paper_bag","potato_chips", "plastic_bottle"]

game_over=False
game_complete=False
current_lvl=1
items=[]
animations=[]

def draw():
    global items, current_lvl, game_complete, game_over
    screen.clear()
    background_image=pygame.image.load("images/background.png")
    scaled_image=pygame.transform.scale(background_image,(WIDTH,HEIGHT))
    screen.blit(scaled_image,(0,0))
    if game_over:
        display_message("GAME OVER", "Try Again")
    elif game_complete:
        display_message("YOU WON", "Well done!")
    else:
        for i in items:
            i.draw()

def update():
    global items
    if len(items)==0:
        items=make_items(current_lvl)

def make_items(extra_items):
    itc=gotc(extra_items) #itc = items to create  gotc =  get option to create
    new_items=create_items(itc)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def gotc(extra_items):
    itc=["paper_bag"]
    for i in range(0, extra_items):
        random_option=random.choice(ITEMS)
        itc.append(random_option)
    return itc

def create_items(itc):
    new_items=[]
    for x in itc:
        item=Actor(x)
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    gaps=len(items_to_layout)+1
    gap_size=WIDTH/gaps
    random.shuffle(items_to_layout)
    for i,item in enumerate(items_to_layout):
        new_x_pos=(i+1) *gap_size
        item.x=new_x_pos

def animate_items(items_to_animate):
    global animations
    for i in items_to_animate:
        duration=START_SPEED-current_lvl
        i.anchor=("center","bottom")
        animation=animate(i,duration=duration,on_finished=handle_game_over,y=HEIGHT+100)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over=True

def on_mouse_down(pos):
    global items,current_lvl
    for i in items:
        if i.collidepoint(pos):
            if "paper_bag" in i.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global current_lvl, items, animations, game_complete
    stop_animations(animations)
    if current_lvl == FINAL_LEVEL:
        game_complete = True
    else:
        current_lvl+=1
        items=[]
        animations=[]

def stop_animations(animations_to_stop):
    for a in animations_to_stop:
        if a.running:
            a.stop()

def display_message(title,subtitle):
    screen.draw.text(title,fontsize=60,center=(CENTRE_X,CENTRE_Y),color="white")
    screen.draw.text(subtitle,fontsize=30,center=(CENTRE_X,CENTRE_Y+30),color="white")

pgzrun.go()

    