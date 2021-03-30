import pygame
import random
from pygame.constants import QUIT

pygame.init()

class player():
    hit_count = 0
    def __init__(self,x,y,width,height,color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 5
        #if we use charecter we must use hitbox 
        #self.hitbox = [self.x,self.y,self.width,self.height]
    def draw(self,win) ->None:
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
    def hit(self):
        self.hit_count += 1
        print("hit",self.hit_count)
        hit_sound.play()

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
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
    def move(self):
        if self.y <= 500 :
            self.y += self.vel
        else:
            self.y = -5 

#define object from classes and initial variables
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('OLIVE')
olive = player(250,460,30,30,(0,255,0))
block = blocks(random.randint(150,460),-60,random.randint(20,40),random.randint(20,40),(255,252,20))
clock = pygame.time.Clock()
#block_1 = blocks(random.randint(20,150),-60,random.randint(20,40),random.randint(20,40),(255,252,120))
#block_2 = blocks(random.randint(150,300),-60,random.randint(20,40),random.randint(20,40),(155,122,120))
#block_3 = blocks(random.randint(300,460),-60,random.randint(20,40),random.randint(20,40),(255,252,20))
#blocks = [block_1,block_2,block_3]

#define music and sound of game
hit_sound = pygame.mixer.Sound("D:\Internet Explorer\pygame\OLIVE\olive\sounds\hit_sound.wav")
bg_music = pygame.mixer.Sound("D:/Internet Explorer/pygame/OLIVE/olive/musics/bg_music.mp3")
#or use pygame.mixer.music.load then wright pygame.music.play(-1)
bg_music.play(-1)

#draw blocks , background and other stuf 
def draw_bg():
    pygame.display.update()
    win.fill((0,0,255))
    if block.y == 500:
        block.y = 0
        block.x = random.randint(40,460)
    block.draw(win)
    if block.y - block.height == olive.y - olive.height or block.y + block.height == olive.y :
       if block.x + block.width > olive.x - olive.width and block.x - block.width < olive.x:
           olive.hit()
#if we want use extra blocks we must do with this way
#    for block in blocks:
#        olive.hitbox[0] = olive.x
#        olive.hitbox[1] = olive.y
#        olive.hitbox[2] = olive.width
#        olive.hitbox[3] = olive.height
#        if block.y - block.height < olive.hitbox[1] + olive.hitbox[3] and block.y + block.height > olive.hitbox[1]:
#            if block.x + block.width > olive.hitbox[0] and block.x - block.width < olive.hitbox[0] + olive.hitbox[2]:
#                olive.hit() 
#        if block.y < 500:
#            block.draw(win)
#        else:
#            block.y = -10
#            block.width = random.randint(20,40)
#            block.height = random.randint(20,40)
#            if block == block_1:
#                block.x = random.randint(20,150)
#            elif block == block_2:
#                block.x = random.randint(150,300)
#            elif block == block_3:
#                block.x = random.randint(300,460)

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
    

