import pygame as pg
import sys
import random
import time

pg.init()
screen=pg.display.set_mode((1000,720))
land=pg.image.load("Land_BG.png")
water=pg.image.load("Water_BG.png")
wood=pg.image.load("Wood_BG.png")
cloud1=pg.image.load("Cloud1.png")
cloud2=pg.image.load("Cloud2.png")
duck=pg.image.load("duck.png")
crosshair=pg.image.load("crosshair.png")
yes=pg.image.load("yes.png")
no=pg.image.load("no.png")
#sound
pg.mixer.music.load("test.mp3")
duck_hit=pg.mixer.Sound("burst.wav")

high=0
kill=True
game1=True
yes_rect=yes.get_rect(center=(400,400))
no_rect=no.get_rect(center=(600,400))
gameover=pg.font.SysFont("comicsansms",40)
message=gameover.render("Game Over!!!",True,(0, 0, 245))
message_rect=message.get_rect(center=(850,50))
again=gameover.render("Do you want to play again???",True,(100, 27, 255))
again_rect=again.get_rect(center=(480,300))

water_position=600
water_velocity=1.5
c=[80,680,800,450]
ducks=[]
re=True

pg.mouse.set_visible(False)

for i in range(20):
    duckx=random.randint(0,950)
    ducky=random.randint(480,660)
    ducks.append(duck.get_rect(center=(duckx,ducky)))

biggame=True
start_time=pg.time.get_ticks()
game=True
def regame():
    global game
    game=False
pg.mixer.music.play(-1)
while biggame:
    while game:
        current_time=pg.time.get_ticks()
        duration=(current_time-start_time)/1000

        score=gameover.render("Score: "+str(20-len(ducks)),False,(0, 0, 255))
        score_rect=score.get_rect(center=(90,50))
        for a in pg.event.get():
            if a.type==pg.QUIT:
                pg.quit()
                sys.exit()
            if a.type==pg.MOUSEMOTION:
                crosshair_rect=crosshair.get_rect(center=a.pos)
            while kill==True:
                if a.type==pg.MOUSEBUTTONDOWN:
                    kak=0
                    for g in ducks:
                        if g.collidepoint(a.pos):
                            duck_hit.play()
                            ducks.pop(kak)
                            pg.display.update()
                            break
                        kak+=1
                kill=False
            kill=True
            if a.type==pg.MOUSEBUTTONDOWN:
                if(yes_rect.collidepoint(a.pos)):
                    regame()
            if a.type==pg.MOUSEBUTTONDOWN:
                if(no_rect.collidepoint(a.pos)):
                    game=False
                    re=False
        screen.blit(wood,(0,0))
        screen.blit(land,(0,550))
        screen.blit(water,(0,water_position))
        screen.blit(cloud1,(c[0],90))
        screen.blit(cloud2,(c[1],100))
        screen.blit(cloud1,(c[2],150))
        screen.blit(cloud2,(c[3],120))
        screen.blit(score,score_rect)
        for duck_rect in ducks:
            screen.blit(duck,duck_rect)
        screen.blit(crosshair,crosshair_rect)
        for k in range(4):
            if(c[k]<1002):
                c[k]=c[k]+k+0.5
            else:
                c[k]=-150
        water_position+=water_velocity
        if water_position>=680 or water_position<=600:
            water_velocity*=-1
        
        for grab in ducks:
            g=random.randint(2,7)
            grab[0]+=g
            if grab[0]>1002:
                grab[0]=-150

        if(len(ducks)<=0 or duration>=10):
            if(20-len(ducks)>high):
                high=20-len(ducks)
            hscore=gameover.render("high Score = "+str(high),True,(0, 0, 245))
            hscore_rect=hscore.get_rect(center=(850,105))
            screen.blit(message,message_rect)
            screen.blit(hscore,hscore_rect)
            game1=False
        
        if(game1==False):
            kill=False
            screen.blit(again,again_rect)
            screen.blit(yes,yes_rect)
            screen.blit(no,no_rect)
        pg.display.update()
    if(re==False):
        biggame=False
    else:
        game=True
        kill=True
        game1=True
        ducks.clear()
        for i in range(20):
            duckx=random.randint(0,950)
            ducky=random.randint(480,660)
            ducks.append(duck.get_rect(center=(duckx,ducky)))
        start_time=pg.time.get_ticks()