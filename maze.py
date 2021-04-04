import pygame
from pygame import *

pygame.init()
window_width= 1280
window_height= 720
screen = pygame.display.set_mode( (window_width,window_height))
pygame.display.set_caption('Maze')
run = True
class Pacman(sprite.Sprite):
    
    
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    
