 #Clinic Inc

#Surgery Simulator
#Emmanuel, Asif, Andy, Kelly
#Become a Master Surgeon after operating on all patients.

# Imports
from gamelib import*

# Objects
game = Game(800,600,"Surgery Simulator",20)
bk = Image("Images//body.jpg",game)
bk.resizeTo(game.width,game.height)
inside = Image("Images//d.jpg",game,use_alpha=False)
tray = Image("Images//tray.jpg",game,use_alpha=False)
tray.rotateTo(90)
tray.moveTo(tray.x+275,tray.y+25)
tray.resizeBy(85)
tray2 = Image("Images//tray.jpg",game,use_alpha=False)
tray2.rotateTo(90)
tray2.moveTo(tray.x-550,tray.y-25)
tray2.resizeBy(85)
d = Image("Images//d.jpg",game)
d4 = Image("Images//d4.jpg",game,use_alpha=False)
d4.resizeBy(-87)
d4.moveTo(tray.x+25,tray.y-100)
ebk = Image("Images//lose.jpg",game)
ebk.resizeTo(game.width,game.height)
r = Image("Images//r.jpg",game,use_alpha=False)
r.resizeBy(-45)
r.moveTo(tray.x,tray.y+75)
h = Image("Images//h.png",game,use_alpha=False)
h.resizeBy(-40)
h.setSpeed(4,90)
sbk = Image("Images//sbk.jpg",game)
sbk.resizeTo(game.width,game.height)
g = Image("Images//g.jpg",game,use_alpha=False)
g.resizeBy(-20)
g.moveTo(g.x,g.y+130)
f =  Font(red,100,black,"Comic Sans Ns")
p = Image("Images//p.png",game)
p.resizeBy(-30)
p.moveTo(g.x,g.x-220)
r2 = Image("Images//r.jpg",game,use_alpha=False)
r2.resizeBy(-45)
r2.resizeBy(100)
r2.moveTo(bk.x,bk.y-25)
d42 = Image("Images//d4.jpg",game,use_alpha=False)
d42.resizeBy(-87)
d42.moveTo(bk.x+15,bk.y-75)
pig = Image("Images//pig.jpg",game,use_alpha=False)
pig.resizeBy(-50)
pig.moveTo(bk.x,bk.y+73)
pig2 = Image("Images//pig.jpg",game,use_alpha=False)
pig2.resizeBy(-50)
pig2.moveTo(bk.x-275,bk.y+73)
lungs2 = Image("Images//lungs.jpg",game,use_alpha=False)
lungs2.resizeBy(-70)
lungs2.moveTo(bk.x,bk.y-95)
lungs = Image("Images//lungs.jpg",game,use_alpha=False)
lungs.resizeBy(-70)
lungs.moveTo(bk.x-260,bk.y)
dead = Image("Images//dead.png",game,use_alpha=False)
dead.resizeBy(150)
stomach = Image("Images//d.jpg",game,use_alpha=False)
stomach.resizeBy(-60)
stomach.moveTo(stomach.x+250,stomach.y)
stomach2 = Image("Images//d.jpg",game,use_alpha=False)
stomach2.resizeBy(-60)
stomach2.moveTo(stomach.x-250,stomach.y-30)
hb = Image("Images//hb.jpg",game)
w = Image("Images//w.jpg",game,use_alpha=False)
# Start Screen
while not game.over:
    game.processInput()
    sbk.draw()
    g.draw()
    p.draw()

    game.drawText("Surgery Simulator",40,40,f)

    if p.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(60)

game.over = False

# GameLoop
while not game.over:
    game.processInput()
    bk.draw()
    tray.move()
    tray2.draw()
    d4.draw()

    if h.collidedWith(d4):
        d4.moveTo(h.x,h.y)
        if mouse.LeftClick and d4.collidedWith(d42):
            d4.resizeBy(100)
    if d4.width >300:
        d4.visible = False
        d42.move()
        stomach.draw()

        if h.collidedWith(stomach):
            stomach.moveTo(h.x,h.y)
            if mouse.LeftClick and stomach.collidedWith(stomach2):
                stomach.resizeBy(100)
        if stomach.width >460:
            stomach.visible = False
            stomach2.move()
            lungs.move()


            if lungs.collidedWith(h):
                lungs.moveTo(h.x,h.y)
                if mouse.LeftClick and lungs2.collidedWith(lungs):
                    lungs.resizeBy(100)
            if lungs.width >362:

                lungs.visible = False
                lungs2.move()
                pig2.draw()
            
                if pig2.collidedWith(h):
                    pig2.moveTo(h.x,h.y)
                    if mouse.LeftClick and pig.collidedWith(pig2):
                        pig2.resizeBy(100)
                if pig2.width >362:
                    pig2.visible = False
                    pig.move()
                    r.move()

                    if h.collidedWith(r):
                        r.moveTo(h.x,h.y)
                        if mouse.LeftClick and r.collidedWith(r2):
                            r.resizeBy(100)
                    if r.width > 584:
                        r.visible = False
                        r2.visible = True
                        r2.move()


    h.moveTo(mouse.x,mouse.y)
    
    game.displayTime(100,5)

# End Screen        
    if game.time < 1:
        ebk.draw()
        dead.draw()
    if r.width >584:
        hb.draw()
        w.draw()
# Update
    game.update(60)
game.quit()
# I plan to make the tray larger and it will include body parts you have to put into your patient in the right order. 

