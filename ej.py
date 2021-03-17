import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
pi = 3.14


def mushroom(x0, y0, length, width):

    ellipse(screen, (249, 255, 255),
            (x0 + 0.13 * length, y0 + 0.52 * width, 0.05 * length, 0.2 * width))
    ellipse(screen, 'black', (x0 + 0.13 * length, y0 + 0.52 * width, 0.05 * length, 0.2 * width), 1)
    ellipse(screen, (228, 13, 31),
            (x0 + 0.08 * length, y0 + 0.5 * width, 0.15 * length, 0.1 * width))
    ellipse(screen, 'black', (x0 + 0.08 * length, y0 + 0.5 * width, 0.15 * length, 0.1 * width), 1)
    circle(screen, (249, 255, 255), (x0 + 0.13 * length, y0 + 0.52 * width), 0.005 * length)
    circle(screen, (249, 255, 255), (x0 + 0.16 * length, y0 + 0.55 * width), 0.007 * length)
    circle(screen, (249, 255, 255), (x0 + 0.17 * length, y0 + 0.52 * width), 0.009 * length)

    circle(screen, (249, 255, 255), (x0 + 0.11 * length, y0 + 0.56 * width), 0.006 * length)
    circle(screen, (249, 255, 255), (x0 + 0.12 * length, y0 + 0.58 * width), 0.008 * length)


def ej(x0, y0, length, width):
    ellipse(screen, (253, 198, 105),
            (x0 + 0.88 * length, y0 + 0.25 * width, 0.07 * length, 0.04 * width))  # leg
    ellipse(screen, 'black', (x0 + 0.88 * length, y0 + 0.25 * width, 0.07 * length, 0.04 * width), 1)
    ellipse(screen, (253, 198, 105),
            (x0 + 0.52 * length, y0 + 0.13 * width, 0.4 * length, 0.2 * width))  # body
    ellipse(screen, 'black', (x0 + 0.52 * length, y0 + 0.13 * width, 0.4 * length, 0.2 * width), 1)
    ellipse(screen, (253, 198, 105),
            (x0 + 0.85 * length, y0 + 0.3 * width, 0.08 * length, 0.05 * width))  # leg
    ellipse(screen, 'black', (x0 + 0.85 * length, y0 + 0.3 * width, 0.08 * length, 0.05 * width), 1)

    ellipse(screen, (253, 198, 105),
            (x0 + 0.85 * length, y0 + 0.3 * width, 0.08 * length, 0.05 * width))  # head
    ellipse(screen, 'black', (x0 + 0.85 * length, y0 + 0.3 * width, 0.08 * length, 0.05 * width), 1)

def tree(x0, y0, width, length):

    rect(screen, (173, 76, 43), (x0, y0, width, length))
    rect(screen, (104, 52, 36), (x0 + 0.05*width, y0, 0.05*width, 1*length))
    rect(screen, (104, 52, 36), (x0 + 0.15 * width, y0, 0.03 * width, 1 * length))
    rect(screen, (104, 52, 36), (x0 + 0.2 * width, y0, 0.03 * width, 1 * length))
    rect(screen, (104, 52, 36), (x0 + 0.3 * width, y0, 0.07 * width, 1 * length))

    rect(screen, (104, 52, 36), (x0 + 0.4 * width, y0, 0.7 * width, 1 * length))
    rect(screen, (63, 26, 13), (x0 + 0.45 * width, y0, 0.05 * width, 1 * length))
    rect(screen, (63, 26, 13), (x0 + 0.6 * width, y0, 0.07 * width, 1 * length))
    rect(screen, (63, 26, 13), (x0 + 0.7 * width, y0, 0.02 * width, 1 * length))
    rect(screen, (63, 26, 13), (x0 + 0.8 * width, y0, 0.02 * width, 1 * length))
    rect(screen, (63, 26, 13), (x0 + 0.9 * width, y0, 0.15 * width, 1 * length))


# background
rect(screen, (66, 92, 35), (0, 0, 600, 500))
rect(screen, (150, 120, 68), (0, 500, 600, 300))

# everything else
mushroom(150, 420, 600, 400)
tree(80, 0, 120, 790)
tree(0, 0, 50, 520)
tree(500, 0, 40, 520)
tree(565, 0, 30, 540)
mushroom(250, 360, 350, 200)
mushroom(0, 430, 600, 500)
ej(100, 600, 400, 400)


pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()