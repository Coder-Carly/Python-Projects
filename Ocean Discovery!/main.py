import pgzrun
import random

# screen dimensions
WIDTH = 1200
HEIGHT = 600

# defining colours
WHITE = (255,255,255)
BLUE = (0,0,255)

# create the submarine and octopus
submarine = Actor('submarine')
squid = Actor('squid')

# submarine starts on the left side
submarine.pos = (100, HEIGHT/2)

# octopus starts on the right side
squid.pos = (WIDTH - 100, HEIGHT/2)

speed = 5
squid_speed = 2

# define a list for bullets
bullets = []

# octopus health
squid_health = 100
max_health = 100

# game states
game_over = False
game_won = False


# display the health
def display_health():
    screen.draw.text(
        "Squid Health: {}/{}".format(squid_health, max_health),
        (50, 50),
        color=WHITE
    )


# display game over
def gameover():
    screen.draw.text(
        "GAME OVER",
        center=(WIDTH/2, HEIGHT/2),
        color=WHITE,
        fontsize=60
    )


# display win message
def you_win():
    screen.draw.text(
        "YOU WIN!",
        center=(WIDTH/2, HEIGHT/2),
        color=WHITE,
        fontsize=60
    )


# shooting
def on_key_down(key):
    if key == keys.SPACE and game_over == False and game_won == False:

        bullets.append(Actor('bubble'))

        # put the bubble in front of the submarine
        bullets[-1].x = submarine.x + 40
        bullets[-1].y = submarine.y


def update():

    global squid_health
    global game_over
    global game_won

    # Don't allow the game to continue after winning or losing
    if game_over == True or game_won == True:
        return

    # -------------------------
    # MOVE THE SUBMARINE
    # -------------------------

    if keyboard.up:
        submarine.y -= speed

        if submarine.y <= 0:
            submarine.y = 0

    elif keyboard.down:
        submarine.y += speed

        if submarine.y >= HEIGHT:
            submarine.y = HEIGHT


    # -------------------------
    # MOVE THE BULLETS
    # -------------------------

    for bullet in bullets[:]:

        # bubbles move to the right
        bullet.x += 10

        # remove bubble if it leaves the screen
        if bullet.x > WIDTH:
            bullets.remove(bullet)


    # -------------------------
    # MOVE THE OCTOPUS
    # -------------------------

    squid.x -= squid_speed


    # -------------------------
    # CHECK IF OCTOPUS REACHES
    # THE SUBMARINE
    # -------------------------

    if squid.colliderect(submarine):
        game_over = True


    # -------------------------
    # CHECK BULLET COLLISIONS
    # -------------------------

    for bullet in bullets[:]:

        if squid.colliderect(bullet):

            # remove the bubble
            bullets.remove(bullet)

            # reduce octopus health
            squid_health -= 5

            # check if octopus has no health left
            if squid_health <= 0:
                game_won = True

            break


# -------------------------
# DRAW EVERYTHING
# -------------------------

def draw():

    screen.clear()

    # underwater background
    screen.fill(BLUE)

    # draw the submarine
    submarine.draw()

    # draw the octopus
    if game_won == False:
        squid.draw()

    # draw the bubbles
    for bullet in bullets:
        bullet.draw()

    # display octopus health
    if game_over == False and game_won == False:
        display_health()

    # display the correct ending
    if game_over:
        gameover()

    if game_won:
        you_win()


pgzrun.go()