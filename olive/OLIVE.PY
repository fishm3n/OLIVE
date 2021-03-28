import pygame
import random
from pygame.constants import QUIT


class player():
    def __init__(self,x,y,width,height,color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 5
    def draw(self,win) ->None:
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))

win = pygame.display.set_mode((500,500))
olive = player(250,460,30,30,(0,255,0))
clock = pygame.time.Clock()
      
class blocks():
    def __init__(self,x,y,width,height,color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 4
    def draw(self,win):
        self.move()
        self.hit()
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
    def move(self):
        if self.y <= 500 :
            self.y += self.vel
        else:
            self.y = -5 
    def hit(self):
        if self.y == olive.y:
            if self.x > olive.x - olive.width and self.x < olive.x + olive.width:
                print('hit')

block_1 = blocks(random.randint(20,150),-60,random.randint(20,40),random.randint(20,40),(255,252,120))
block_2 = blocks(random.randint(150,300),-60,random.randint(20,40),random.randint(20,40),(155,122,120))
block_3 = blocks(random.randint(300,460),-60,random.randint(20,40),random.randint(20,40),(255,252,20))
blocks = [block_1,block_2,block_3]

#draw blocks , background and other stuf 
def draw_bg():
    pygame.display.update()
    win.fill((0,0,255))
    for block in blocks:
        if block.y < 500:
            block.draw(win)
        else:
            block.y = -10
            block.width = random.randint(20,40)
            block.height = random.randint(20,40)
            if block == block_1:
                block.x = random.randint(20,150)
            elif block == block_2:
                block.x = random.randint(150,300)
            elif block == block_3:
                block.x = random.randint(300,460)

#main loop
while True:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == QUIT :
           pygame.quit()       

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and olive.x + olive.width + olive.vel < 500 :
        olive.x += olive.vel
    if keys[pygame.K_LEFT] and olive.x - olive.vel > 0:
        olive.x -= olive.vel
        
    draw_bg()
    olive.draw(win)
    

