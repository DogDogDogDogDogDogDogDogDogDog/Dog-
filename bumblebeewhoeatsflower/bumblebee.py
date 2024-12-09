import pgzrun
from random import randint
WIDTH=500
HEIGHT=500
TITLE="Bummbly Bee and the quest to eat all the flowers!"
B=Actor("bee")
B.pos=250,250
F=Actor("flower")
F.pos=100,150
S=0
GameOver=False
def draw():
    screen.clear()
    screen.blit("background",(0,0))
    B.draw()
    F.draw()
    screen.draw.text("Score:"+str(S),center=(250,45),fontsize=30,color="red")
    if GameOver:
        screen.fill("red")
        screen.draw.text("Times up!!!",fontsize=50,color="green",center=(250,200))
        screen.draw.text("Your final score is:"+str(S),fontsize=50,color="green",center=(250,250))
def randomflowerpos():
    F.x=randint(1,450)
    F.y=randint(1,450)

def timer():
    global GameOver
    GameOver=True

def update():
    global S
    if keyboard.left and B.x>0:
        B.x=B.x-5
    if keyboard.right and B.x<500:
        B.x=B.x+5
    if keyboard.up and B.y>0:
        B.y=B.y-5
    if keyboard.down and B.y<500:
        B.y=B.y+5
    
    if B.colliderect(F):
        randomflowerpos()
        S=S+1

clock.schedule(timer,10.0)

randomflowerpos()

pgzrun.go()