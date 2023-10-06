import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, KEYUP, K_SPACE
from pygame.locals import Rect
import math

pygame.init()

SURFACE = pygame.display.set_mode((400,300))
pygame.display.set_caption('Game Window')
FPSCLOCK = pygame.time.Clock()

class Block:
    def __init__(self,color,rect):
        self.color = color
        self.rect = rect

    def draw(self):
        pygame.draw.rect(SURFACE,self.color,self.rect)

class Ball:

    def __init__(self,color,rect,dir,speed):
        self.color = color
        self.rect = rect
        self.dir = dir
        self.speed = speed
    
    def draw(self):
        pygame.draw.ellipse(SURFACE,self.color,self.rect)
        
    def move(self):
        self.rect.centerx += math.cos(math.radians(self.dir))*self.speed
        self.rect.centery -= math.sin(math.radians(self.dir))*self.speed

        if ball_rect.centerx <=0 or ball_rect.centerx >= 400:
            self.dir = 180 - self.dir
        if ball_rect.centery <= 0 or ball_rect.centery >= 300:
            self.dir = -self.dir

left=6
top=30
width=45
height=20
color=(200,50,200)
blocks = []
for i in range(4):
    for j in range(8):
        rect = Rect(left, top, width, height)
        blocks.append(Block(color, rect))
        left += 49
    left = 6
    top += 24
 
pw = 100
ph = 5
 
ball_rect = Rect(150,100,10,10)
ball_color = (255,255,0)
ball = Ball(ball_color, ball_rect, 60, 5)

paddle = Block((0, 0, 255),Rect(180, 295,pw, ph))

pygame.key.set_repeat(30, 30)

num = 0
while True:
    SURFACE.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT and paddle.rect.centerx-pw/2 > 0:
                paddle.rect.centerx -= 10
            elif event.key == K_RIGHT and paddle.rect.centerx+pw/2 < 400:
                paddle.rect.centerx += 10

    for block in blocks:
        if ball.rect.colliderect(block.rect)==True:
            ball.dir = -ball.dir
            blocks.remove(block)

    if ball.rect.colliderect(paddle.rect)==True:
            ball.dir = -ball.dir
            
    for block in blocks:
        block.draw()
    ball.draw()
    paddle.draw()

    pygame.display.update()

    if not blocks or ball_rect.centery > 300:
        continue
    ball.move()

    FPSCLOCK.tick(60)