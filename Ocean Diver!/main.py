import pygame
import pgzrun
import random
from random import randint

WIDTH = 600
HEIGHT = 600

score = 0
game_over = False

diver = Actor("diver3")
diver.pos = 100, 100

pearls = ["pearl1", "pearl2", "pearl3"]
pearl = Actor(random.choice(pearls))
pearl.pos = 200, 200

background_image = pygame.image.load("images/ocean.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

def draw():
    screen.clear()
    screen.blit(background_image, (0, 0))
    diver.draw()
    pearl.draw()
    screen.draw.text("Pearls: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill((65, 105, 225, 128))
        screen.draw.text(
            "Sorry, but you ran out of oxygen! \n Total Number Of Pearls: " + str(score),
            midtop=(WIDTH / 2, 10),
            fontsize=40,
            color="cyan"
        )

def place_pearl():
    global pearl
    other_pearls = [p for p in pearls if p != pearl.image]  # exclude current pearl
    pearl = Actor(random.choice(other_pearls))
    pearl.x = randint(70, WIDTH - 70)
    pearl.y = randint(70, HEIGHT - 70)

place_pearl()

def time_up():
    global game_over
    game_over = True

def update():
    global score, pearl, game_over
    if game_over:
        return

    if keyboard.left:
        diver.x = max(0, diver.x - 2)
    if keyboard.right:
        diver.x = min(WIDTH, diver.x + 2)
    if keyboard.up:
        diver.y = max(0, diver.y - 2)
    if keyboard.down:
        diver.y = min(HEIGHT, diver.y + 2)

    if diver.colliderect(pearl):
        score += 1
        place_pearl()

clock.schedule(time_up, 60.0)
pgzrun.go()