import pygame

pygame.init()

screen_width = 1280
screen_heiht = 720

window = pygame.display.set_mode((screen_width, screen_heiht))

pygame.display.set_caption("Geomrtry Dash platformer")

fps = 30
width = 61
height = 71
x = 50
y = 720 - height
speed = 10

isJump = False
jumpCount = 10
isDead = False

walkLeft = [pygame.image.load('learn_python3/pygame_left_1.png'), pygame.image.load('learn_python3/pygame_left_2.png'),
pygame.image.load('learn_python3/pygame_left_3.png'),pygame.image.load('learn_python3/pygame_left_4.png'), 
pygame.image.load('learn_python3/pygame_left_5.png'), pygame.image.load('learn_python3/pygame_left_6.png')]

walkRight = [pygame.image.load('learn_python3/pygame_right_1.png'), pygame.image.load('learn_python3/pygame_right_2.png'),
pygame.image.load('learn_python3/pygame_right_3.png'),pygame.image.load('learn_python3/pygame_right_4.png'), 
pygame.image.load('learn_python3/pygame_right_5.png'), pygame.image.load('learn_python3/pygame_right_6.png')]

playerStand = pygame.image.load('learn_python3/pygame_idle.png')

bg = pygame.image.load('learn_python3/bg.jpg')

clock = pygame.time.Clock()


left = False
right = False
animcount = 0

def drawWindow():

    global animcount
    window.blit(bg, (0, 0))

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

    
    pygame.draw.polygon(window, (255, 0, 0), ((800, screen_heiht), (850, 620), (900, screen_heiht)))  
    pygame.display.update()

run = True
while run:
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
    

pygame.quit()