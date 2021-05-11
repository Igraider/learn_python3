import pygame
import random
from random import randint
from pygame import *

pygame.init()

speed = 3

infoObject = pygame.display.Info()
window = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

k = 0
letter = ''
hand = ''
shrift = 250
interval = shrift // 5
letter_x = randint(100, infoObject.current_w)
letter_y = randint(-50, infoObject.current_h - 2 * shrift - 50)
hand_x = letter_x
hand_y =  letter_y + 100


pygame.display.set_caption("Буквы.")

font_name = pygame.font.match_font('arial')
bg = transform.scale(image.load('learn_python3/white_phone.jpg'), (infoObject.current_w, infoObject.current_h))
def get_random_hand():
    global hand
    global hand_x
    global hand_y
    hands = ['П', 'Л', 'О']
    hand = random.choice(hands)
    hand_x = letter_x
    hand_y =  letter_y + shrift + interval

def get_random_letter():
    global letter
    global letter_x
    global letter_y
    all_letters = ('А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я').split()
    number = random.randint(0,32)
    letter = all_letters[number]
    letter_x = randint(100, infoObject.current_w - interval - 50)
    letter_y = randint(-50, infoObject.current_h - 2 * shrift - 100)
    

def draw_letter(surf, arg, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(arg + text, True, (0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    window.blit(text_surface, text_rect)

run = True
while run:
    
    time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(bg, (0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_RIGHT] and speed < 5:
        speed += 1
    if keys[pygame.K_LEFT] and speed > 1:
        speed -= 1
    k += 1
    if speed == 3:

        if k >= 60:
            get_random_letter()
            get_random_hand()
            k = 0

    elif speed == 1:

        if k >= 100:
            get_random_letter()
            get_random_hand()
            k = 0
    elif speed == 2:

        if k >= 80:
            get_random_letter()
            get_random_hand()
            k = 0
    
    elif speed == 4:

        if k >= 40:
            get_random_letter()
            get_random_hand()
            k = 0

    else:

        if k >= 30:
            get_random_letter()
            get_random_hand()
            k = 0

    draw_letter(window, '', hand, shrift, hand_x, hand_y)
    draw_letter(window, '', letter, shrift, letter_x, letter_y)
    draw_letter(window, '', 'Esc - Чтобы выйти.', 15, 100, 0)
    draw_letter(window, '', 'Скорость = ' + str(speed), 15, infoObject.current_w - 100, 0)
    display.update()

quit()