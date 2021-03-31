import pygame
import random
from random import randint
from pygame import *

pygame.init()

screen_width = 1280
screen_heiht = 720

window = pygame.display.set_mode((screen_width, screen_heiht))

pygame.display.set_caption("balls")

finish = False
fps = 30
width = 61
height = 71
x = 50
y = 720 - height - 3
speed = 10
k = 180
length_b = 35
b_spd = 5
balls = []
meteors = []
scores = 0

isJump = False
jumpCount = 10
isDead = False

class GameSprite(sprite.Sprite):

    def __init__(self, spd, img_name, x, y):
        sprite.Sprite.__init__(self)
        self.spd = spd
        self.image = transform.scale(img_name, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
        

walkLeft = [image.load('learn_python3/pygame_left_1.png'),  image.load('learn_python3/pygame_left_2.png'),
image.load('learn_python3/pygame_left_3.png'), image.load('learn_python3/pygame_left_4.png'), 
image.load('learn_python3/pygame_left_5.png'), image.load('learn_python3/pygame_left_6.png')]

walkRight = [image.load('learn_python3/pygame_right_1.png'),  image.load('learn_python3/pygame_right_2.png'),
image.load('learn_python3/pygame_right_3.png'), image.load('learn_python3/pygame_right_4.png'), 
image.load('learn_python3/pygame_right_5.png'), image.load('learn_python3/pygame_right_6.png')]

playerStand = image.load('learn_python3/pygame_idle.png')

all_heroes = [image.load('learn_python3/pygame_left_1.png'),  image.load('learn_python3/pygame_left_2.png'),
image.load('learn_python3/pygame_left_3.png'), image.load('learn_python3/pygame_left_4.png'), 
image.load('learn_python3/pygame_left_5.png'), image.load('learn_python3/pygame_left_6.png'),
image.load('learn_python3/pygame_right_1.png'),  image.load('learn_python3/pygame_right_2.png'),
image.load('learn_python3/pygame_right_3.png'), image.load('learn_python3/pygame_right_4.png'), 
image.load('learn_python3/pygame_right_5.png'), image.load('learn_python3/pygame_right_6.png'),
image.load('learn_python3/pygame_idle.png')]



bg = pygame.transform.scale(image.load('learn_python3/bg.png'), (screen_width, screen_heiht))
football = 'learn_python3/football.png'
basketball = 'learn_python3/basketball.png'
meteor_img = 'learn_python3/meteor.png'
clock = pygame.time.Clock()
game_over = 'learn_python3/Game_over.jpg'

left = False
right = False
animcount = 0


class Ball(sprite.Sprite):

    def __init__(self, spd, img, width, height, x, y, indx):
        sprite.Sprite.__init__(self)

        self.spd = spd
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.indx = indx
    
    def update(self):
        self.rect.y += self.spd

    def kill(self):
        balls.pop(self.indx)
    
def spawningBalls():
    global k
    global meteor_img

    k += 1
    if k >= 25:                               
        k = 0
        random_ball = randint(1, 4)
        if random_ball == 1:
            some_ball = Ball(randint(4,8), football, length_b, length_b, randint(0, screen_width - length_b), 0, len(balls))
            balls.append(some_ball)
        if random_ball == 2:
            some_ball = Ball(randint(3,8), basketball, length_b, length_b, randint(0, screen_width - length_b), 0, len(balls))
            balls.append(some_ball)
        else:
            meteor = Ball(randint(2,9), meteor_img, randint(65, 85), randint(100, 120), randint(0, screen_width - length_b), 0, len(meteors))
            meteors.append(meteor)
    
    for ball in balls:
        window.blit(ball.image, ball.rect)
        ball.update()
        for i in all_heroes:
            i = GameSprite(speed, i, x, y)
            if sprite.collide_rect(i, ball):
                ball.kill()

    for meteor in meteors:
        window.blit(meteor.image, meteor.rect)
        meteor.update()
        for b in all_heroes:
            b = GameSprite(speed, b, x, y)
            if sprite.collide_rect(b, meteor):
                finish = True

def drawWindow():

    global animcount
    window.blit(bg, (0, 0))

    spawningBalls()

    if animcount + 1 >= fps:
        animcount = 0 

    if left:
        window.blit(walkLeft[animcount // 5], (x, y))
        animcount += 1
    elif right:
        window.blit(walkRight[animcount // 5], (x, y))
        animcount += 1
    else:
        window.blit(playerStand, (x, y))

    
    pygame.display.update()

run = True
while run:
    if not finish:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= speed
            left = True
            right = False
            if x < 0:
                x = 0

        elif keys[pygame.K_RIGHT]:
            x += speed
            left = False
            right = True
            if x > screen_width - width:
                x = screen_width - width
        
        else:
            left = False
            right = False
            animcount = 0

        if not isJump:
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            if jumpCount >= -10:
                if jumpCount < 0:
                    y += (jumpCount ** 2) / 2
                    jumpCount -= 1
                else:
                    y -= (jumpCount ** 2) / 2
                    jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10

        drawWindow()
    else:
        window.blit(game_over, (0, 0))  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  
    
pygame.quit()