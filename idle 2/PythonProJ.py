from pygame.locals import *
import pygame
from random import randint

pygame.init()

size = [600, 750]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Drowning Shark')

done = False
clock = pygame.time.Clock()

background_image = pygame.image.load("gamebg.jpg")
avatar_image = pygame.image.load("avatar.png")
normal_bar_image = pygame.image.load("bar.png")
danger_bar_image = pygame.image.load("Danger_bar.png")
screen.blit(background_image, [-700, -100])

X = size[0] / 2.5
Y = 0

NORMAL_BAR = 0
DANGER_BAR = 1


def move(x, y):
    global X, Y
    X = x
    Y = y
    screen.blit(avatar_image, (x, y))


def moveDown():
    global X, Y
    move(X, Y + 7)

def moveUp():
    global X, Y
    move(X, Y - 10)


def start_menu():
    intro = True


def is_alive():
    global X, Y, size
    if X + 110 > size[0] or X < 0:
        return False
    if Y + 110 > size[1] or Y < 0:
        return False
    return True


bars = []

move(size[0] / 2.5, 0)

while not done:

    screen.blit(background_image, [-700, -100])
    if randint(0, 9) <= 1:
        xbars = randint(0, size[0])
        lengthbar = randint(80, 120)
        types = randint(0, 1)
        bars.append({
            "x": xbars,
            "y": size[1],
            "length": lengthbar,
            "type": types
        })

    for bar in bars:
        bar["y"] -= 10
        if bar["type"] == NORMAL_BAR:
            bar2 = pygame.transform.scale(normal_bar_image,(bar["length"],20))
            screen.blit(bar2, [bar["x"],bar["y"]])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                X -= 10
            if event.key == K_RIGHT:
                X += 10

    onbar = False
    for bar in bars:
        if X >= bar["x"] and X <= bar["x"]+bar["length"]:
            if bar["y"] - Y < 80:
                onbar = True

    if onbar :
        moveUp()
    else:
        moveDown()

    if not is_alive():
        done = True

    pygame.display.flip()
    pygame.display.update()

    clock.tick(60)

start_menu()
