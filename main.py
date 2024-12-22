import pygame
from pygame.examples.sprite_texture import running
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/photo_2024-12-22_23-46-57.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/photo_2024-12-22_23-53-30.jpg")
target_widht = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_widht)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(o, 255)), (random.randint(o, 255)), (random.randint(o, 255))

running = True
while running:
    pass













pygame.quit()