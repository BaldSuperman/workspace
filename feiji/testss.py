import pygame
from feiji.plane_Sprite import *
screen = pygame.display.set_mode(SCREEN_RECT.size)
while True:
    for even in pygame.event.get():
        print(even.type)

