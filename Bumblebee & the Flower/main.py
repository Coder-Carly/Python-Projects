import pygame
import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600

score = 0
game_over = False

bee = Actor("bumblebee")
bee.pos = 100,100

flower = Actor("flower")
flower.pos = 200,200

def draw():
    screen.clear()
    background_image=pygame.image.load("images/background.png")
    scaled_image=pygame.transform.scale(background_image,(WIDTH, HEIGHT))
    screen.blit(scaled_image,(0,0))

    flower.draw()
    bee.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))

    if game_over:
        screen.fill((255, 192, 203, 128))
        screen.draw.text(
            "Time's Up! Your Final Score: " + str(score),
            midtop = (WIDTH/2, 10),
            fontsize=40,
            color="red"
        )

def place_flower():
    flower.x = randint(70, WIDTH - 70)
    flower.y = randint(70, HEIGHT - 70)
place_flower()

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.left:
        bee.x = max(0, bee.x - 2)
    if keyboard.right:
        bee.x = min(WIDTH, bee.x + 2)
    if keyboard.up:
        bee.y = max(0, bee.y - 2)
    if keyboard.down:
        bee.y = min(HEIGHT, bee.y + 2)
    
    flower_collected = bee.colliderect(flower)

    if flower_collected:
        score = score + 10
        place_flower()

clock.schedule(time_up, 60.0)
pgzrun.go()