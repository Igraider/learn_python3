from typing_extensions import runtime
import pygame
import random
from pygame import *
from pygame import display

pygame.init()

infoObject = pygame.display.Info()
window = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

pygame.display.set_caption("Хлоп.")

blue = (0, 0, 225)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
purple = (255, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
colors = [blue, red, green, yellow, purple, white, black]

font_name = pygame.font.match_font('arial')

def is_hlop():
    if random.randint(1, 10) <= 2:
        return True
    else:
        return False

def choose_random_color():

    if is_hlop():
        text = 'Хлоп'
        color = random.choice(colors)


    color = random.choice(colors)
    

def draw_text(surf, color, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    window.blit(text_surface, text_rect)

run = True

while run:

    time.delay(50)
    
    window.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = key.get_pressed()

    if keys[K_ESCAPE]:
        run = False

    display.update()

quit()