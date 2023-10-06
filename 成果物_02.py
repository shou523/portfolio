import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, Rect
import math
pygame.init()
FPSCLOCK = pygame.time.Clock()
SURFACE = pygame.display.set_mode((400,300))
pygame.display.set_caption("Game Window")
pygame.key.set_repeat(30, 30)
class Block:
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect
    def draw(self):
        pygame.draw.rect(SURFACE, self.color, self.rect)
class Ball:
    def __init__(self, color, rect, dir, speed):
        self.color = color #ブロックの色(R,G,B)
        self.rect = rect #初期位置と大きさ(Rect を利用)
        self.dir = dir #初期角度
        self.speed = speed #初期スピード
    def draw(self):
        pygame.draw.ellipse(SURFACE, self.color, self.rect)
    def move(self):
        if self.rect.centerx < 0 or self.rect.centerx > 400:
            self.dir = 180-self.dir
        if self.rect.centery < 0 or self.rect.centery > 300:
            self.dir = -self.dir
        self.rect.centerx += math.cos(math.radians(self.dir))*self.speed
        self.rect.centery -= math.sin(math.radians(self.dir))*self.speed
#Rect オブジェクトの生成
left=6
top=30

width=45
height=20
color=(200,50,200)
blocks = []
for j in range(4):
    for i in range(8):
        rect = Rect(left, top, width, height)
        blocks.append(Block(color,rect))
        left += 49
    left = 6
    top += 24
#Ball オブジェクトの生成
ball_rect = Rect(150,100,10,10)
ball_color = (255,255,0)
ball = Ball(ball_color, ball_rect, 320, 2)

while True:
    SURFACE.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #ボールとブロックの衝突判定
    for block in blocks:
        if ball.rect.colliderect(block.rect)==True:
            blocks.remove(block) #衝突したらそのオブジェクトをリストから削除する
            ball.dir = -ball.dir
    ball.move()
    for block in blocks:
        block.draw()
ball.draw()
pygame.display.update()
FPSCLOCK.tick(60)