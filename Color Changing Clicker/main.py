import pgzrun
from random import randint, choice

TITLE = "Shape Clicker"
WIDTH = 500
HEIGHT = 500

current_shape = None  # (shape, pos, color, extra)

def draw():
    screen.clear()
    screen.fill((0, 0, 0))

    if current_shape is None:
        return

    shape, pos, col, extra = current_shape
    x, y = pos

    if shape == "circle":
        screen.draw.filled_circle(pos, extra, col)

    elif shape == "square":
        size = extra
        rect = Rect(x - size // 2, y - size // 2, size, size)
        screen.draw.filled_rect(rect, col)

    elif shape == "rectangle":
        w, h = extra
        rect = Rect(x - w // 2, y - h // 2, w, h)
        screen.draw.filled_rect(rect, col)

def new_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def on_mouse_down(pos, button):
    global current_shape
    shape = choice(["circle", "square", "rectangle", "triangle"])
    col = new_color()

    if shape == "circle":
        extra = randint(20, 60)
    elif shape == "square":
        extra = randint(40, 100)
    elif shape == "rectangle":
        extra = (randint(60, 130), randint(30, 80))
    else:  # triangle
        extra = randint(30, 70)

    current_shape = (shape, pos, col, extra)


pgzrun.go()