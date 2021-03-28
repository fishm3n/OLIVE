import pygame
import random
from pygame.constants import QUIT


win = pygame.display.set_mode((500,500))
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
        
class blocks():
    def __init__(self,x,y,width,height,color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 3
    def draw(self,win):
        self.move()
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
    def move(self):
        if self.y <= 500 :
            self.y += self.vel
        else:
            self.y = -5 

def draw_bg():
    pygame.display.update()
    win.fill((0,0,255))
    for block in blocks:
        block.draw(win)
rand_position = random.randint(10,490)
rand_width = random.randint(5,40)
rand_height = random.randint(5,30)
blocks = []
olive = player(250,460,30,30,(0,255,0))
clock = pygame.time.Clock()
while True:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == QUIT :
           pygame.quit()
    for block in blocks:
        #if len(blocks) < 3:
            blocks.append(blocks(10,-21,12,12,(0,255,255)))
        
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and olive.x + olive.width + olive.vel < 500 :
        olive.x += olive.vel

    if keys[pygame.K_LEFT] and olive.x - olive.vel > 0:
        olive.x -= olive.vel
    draw_bg()
    olive.draw(win)
    

