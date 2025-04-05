import pygame
import random
import math
screenwidth=800
screenhight=500
pstartx=370
pstarty=380
estartymin=50
estartymax=150
espeedx=4
espeedy=40
bspeedy=10
cdistance=27
pygame.init()
screen=pygame.display.set_mode((screenwidth,screenhight))
background=pygame.image.load('bg.webp')
pygame.display.set_caption('space invaders')
icon=pygame.image.load('ufo.webp')
pygame.display.set_icon(icon)
playimg=pygame.image.load('')#img
playerx=playerx
playery=pstarty
pxchange=0
enemyimg=[]
enemyx=[]
enemyy=[]
enemyxchange=[]
enemyychange=[]
numofe= 6
for _i in range9(numofe):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0,screenwidth-64))
    enemyy.append(random.randint(estartymin,estartymax))
    enemyxchange.append(espeedx)
    enemyychange.append(espeedy)
bulletimg=pygame.image.load('')#bullet.png
bulletx= 0
bullety=pstarty
bulletxchange=0
bulletychange=bspeedy
bulletstate="ready"
scorevalue =0
font=pygame.font.Font('freestansbold.ttf',32)
textx=10
texty=10
overfont=pygame.font.Font('freestansbold.ttf',64)
def showscore(x,y):
    score=font.render("Score:"+str(scorevalue),True,(255,255,255))
    screen.blit(score,(x,y))
def gameovertext():
    overtext=overfont.render("Game OVER!",True,(255,255,255))
    screen.blit(overtext,(200,250))
def player(x,y):
    screen.blit(playimg,(x,y))
def enemey(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fireb(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletimg,(x+16,y+20))
def isCollition(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((enemyx-bullety)**2+(enemyy-bullety)**2)
    return distance < collutiondistance

