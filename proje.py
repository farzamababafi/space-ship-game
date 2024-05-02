import pygame
import random
import math
from pygame import mixer
pygame.init()
mixer.init()
score=0
class window:
    def __init__(self): 
         self.win=pygame.display.set_mode((800,800))
         pygame.display.set_caption('first game')
         self.backg=pygame.image.load('407715-PD3A61-464.jpg')
    def show(self):
        self.win.blit(self.backg,(0,0))
win1=window()
class txt(window):
    def __init__(self,x,y):
        self.font=pygame.font.Font('freesansbold.ttf',32)
        self.textx=x
        self.texty=y
    def show(self):
        self.label=self.font.render('score :' +str(score) ,True,(255,255,255))
        win1.win.blit(self.label,(self.textx,self.texty))
    def game_over(self):
        self.game=self.font.render('game over' ,True,(255,255,255))
        win1.win.blit(self.game,(350,400))
t1=txt(10,10)
class player:
    def __init__(self,x,y,vel):
        self.player_p=pygame.image.load('spaceship.png')
        self.shx=x
        self.shy=y
        self.sh_vel=vel
    def show(self):
            win1.win.blit(self.player_p,(self.shx,self.shy))
    def move(self,key):
        if key[pygame.K_LEFT] and self.shx>0:
            self.shx-=self.sh_vel
        if key[pygame.K_RIGHT] and self.shx<730:
            self.shx+=self.sh_vel
        if key[pygame.K_DOWN] and self.shy<720:
            self.shy+=self.sh_vel
        if key[pygame.K_UP] and self.shy>0 and self.shy>430:
            self.shy-=self.sh_vel
p1=player(380,720,1)
class bullet(player):
    def __init__(self,vel):
        self.bs=mixer.Sound('a.mp3')
        self.bullet_p=pygame.image.load('u.png')
        self.bx=0
        self.by=0
        self.b_vel=vel
        self.r=0
    def shot(self,key):
        if key[pygame.K_SPACE]:
            win1.win.blit(self.bullet_p,(p1.shx+25,p1.shy-5))
            self.bs.play()
            self.bx=p1.shx+25
            self.by=p1.shy-5
            self.r=1
        if self.r==1:
            self.by-=self.b_vel
            win1.win.blit(self.bullet_p,(self.bx,self.by))
b1=bullet(1)
class enemy:
    def __init__(self,vel1,vel2,num):
        self.es=mixer.Sound('b.mp3')
        self.enemy_p=[]
        self.enx=[]
        self.eny=[]
        self.enx_vel=[]
        self.eny_vel=[]
        self.num=num
        for i in range(num):
            self.enemy_p.append(pygame.image.load('ufo.png'))
            self.enx.append(random.randint(0, 740))
            self.eny.append(random.randint(0, 350))
            self.enx_vel.append(vel1)
            self.eny_vel.append(vel2)
    def show(self):
        for i in range(self.num): 
            win1.win.blit(self.enemy_p[i],(self.enx[i],self.eny[i]))
    def move(self):
        for i in range(self.num): 
           self.enx[i]+= self.enx_vel[i]
           if self.enx[i]>740:
               self.enx_vel[i]-=0.5
               self.eny[i]+=self.eny_vel[i]
           elif self.enx[i]<0:
               self.enx_vel[i]+=0.5
               self.eny[i]+=self.eny_vel[i]
           if  self.eny[i]>700:
                for j in range(self.num): 
                    self.eny[j]=2000
                b1.r=2
                break
                    
e1=enemy(0.5,40,6)
def dis(x1:enemy,y1:enemy,x2:bullet,y2:bullet):
    c=[]
    for i in range(e1.num):
        c.append(math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2)))
        if c[i]<20:
            return True
        else:
            return False
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    keys=pygame.key.get_pressed()
    p1.move(keys)
    e1.move()
    win1.show()
    b1.shot(keys)
    p1.show()
    e1.show()
    for i in range(e1.num):
         if dis(e1.enx[i],e1.eny[i],b1.bx,b1.by):
            e1.es.play()
            b1.bx=b1.by=0
            e1.enx[i]=random.randint(0, 740)
            e1.eny[i]=random.randint(0, 350)
            b1.r=0
            score+=1
    t1.show()
    if b1.r==2:
        t1.game_over()
    
    pygame.display.update()
pygame.quit()

