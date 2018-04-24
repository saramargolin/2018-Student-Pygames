#GLA
#Crazy Car
#Gavin Pritipaul & Leland Zheng & Christopher Alarcon
#You have to drive down a road and aviod the obstcales in the path
#I am not able make the cones stop resizing at a certain size and disappear when it gets to a certain size
#Margolin suggestions:
#add driving sound and add a way to win.
from gamelib import*

#Game Object
game = Game(800, 600, "Crazy Car")

#Image Variables
bk = Animation("road3.png",12,game,768/3,960/4)
bk.resizeTo(game.width,game.height)
game.setBackground(bk)

car= Image("car.png",game)
car.moveTo(390,500)
car.resizeBy(-10)

fence= Image("fence.png",game)
fence.rotateBy(-40)
fence.resizeBy(-70)
fence.moveTo(155,400)

fence2= Image("fence2.png",game)
fence2.rotateBy(40)
fence2.resizeBy(-70)
fence2.moveTo(625,400)

f = Font(red,20,red,"Comic Sans MS")
f1= Font(blue,70,red,"Comic Sans MS")
f2= Font(blue,20,blue,"Comic Sans MS")

y = 100

cones = []

for index in range(50):
    cones.append( Animation( "cones.png",2,game,240/1,360/2))
for index in range(50):
    cones[index].resizeBy(-70)

    cones[index].setSpeed(11,180)
    x = randint(300,500)
    cones[index].moveTo(x,-y)
    y+=250

#sound files
carcrash= Sound("carcrash.wav",1)
drive = Sound("drive.wav",2)


#Title Screen
while not game.over:
    game.processInput()
    bk.draw()
    game.drawText("Crazy Car",240,50,f1)
    game.drawText("Use the left and right arrow keys to aviod the oncoming obstacles!",80,300,f)
    game.drawText("Press Space Bar to Start The Game",230,200,f)
    car.draw()
    fence.draw()
    fence2.draw()
    if keys.Pressed[K_SPACE]:
        game.over=True
    game.update(60)

    

#Level One Game Loop
game.over=False
obstaclesPassed = 0 
while not game.over:
    game.processInput()
    bk.draw()
    car.draw()
    fence.draw()
    fence2.draw()
    
    game.drawText("Level 1", 10,10,Font(blue,30,blue,"Comic Sans MS"))
    

    for index in range(50):
        cones[index].move()
        if cones[index].collidedWith(car):
            car.health -= 10
            cones[index].moveTo(390,6000)
            carcrash.play()
            
        if cones[index].isOffScreen("bottom")and cones[index].visible:
            obstaclesPassed += 1
            cones[index].visible = False
    if obstaclesPassed >= 50:
        game.over=True

    if car.health <1:
        game.drawText("YOU LOSE!",210
                      ,50,f1)
        game.drawText("Press Space Bar to End The Game",230,200,f)
        if keys.Pressed[K_SPACE]:
            game.quit()

    game.drawText("Health: " + str(car.health),600,10,f2)
    game.drawText("Obstacles Passed: " + str(obstaclesPassed),600,30,f2)

    if fence.collidedWith(car):
        car.health-=10
        car.x+=150
       
    if fence2.collidedWith(car):
        car.health-=10
        car.x-=150
       
          
    if keys.Pressed[K_ESCAPE]:
        game.quit()
    if keys.Pressed[K_RIGHT]:
        car.x += 6
        drive.play()#added sound
    if keys.Pressed[K_LEFT]:
        car.x -= 6
        drive.play()
    game.update(60)

game.over=False
obstaclesPassed=0

y = 100
garbage = []
w = 60
h = 100

for index in range(25):
    garbage.append( Image("garbage.png",game))   
for index in range(25):
    garbage[index].setSpeed(7,180)#Zero deg (up), 180 deg (down)
    garbage[index].resizeBy(-70)
    x = randint(300,500)
    garbage[index].moveTo(x, -y)
    y+=250
    w+=10
    h+=10

y = 100

cones = []

for index in range(35):
    cones.append( Animation( "cones.png",2,game,240/1,360/2))
for index in range(35):
    cones[index].resizeBy(-70)
    cones[index].setSpeed(11,180)
    x = randint(300,500)
    cones[index].moveTo(x,-y)
    y+=250
    w+=10
    h+=10

#Level Two Game Loop
game.over=False
obstaclesPassed=0
car.health=100
while not game.over:
    game.processInput()
    bk.draw()
    car.draw()
    fence.draw()
    fence2.draw()
    game.drawText("Level 2", 10,10,Font(blue,30,blue,"Comic Sans MS"))
    

    for index in range(25):
        garbage[index].move()
        if garbage[index].collidedWith(car):
            car.health -= 10
            garbage[index].moveTo(390,6000)
            carcrash.play()
        if garbage[index].isOffScreen("bottom") and garbage[index].visible:
            obstaclesPassed += 1
            garbage[index].visible = False

    for index in range(35):
        cones[index].move()
        if cones[index].collidedWith(car):
            car.health -= 10
            cones[index].moveTo(390,6000)
            carcrash.play()
        if cones[index].isOffScreen("bottom") and cones[index].visible:
            obstaclesPassed += 1
            cones[index].visible = False

    if obstaclesPassed >= 50:
        game.drawText("YOU WIN!",220,50,f1)
        game.drawText("Press Space Bar to End The Game",230,200,f)
        if keys.Pressed[K_SPACE]:
            game.quit()

    if car.health <1:
        game.over = True


    game.drawText("Health: " + str(car.health),600,10,f2)
    game.drawText("Obstacles Passed: " + str(obstaclesPassed),600,30,f2)


    if fence.collidedWith(car):
        car.health-=10
        car.moveTo(390,500)
       
    if fence2.collidedWith(car):
        car.health-=10
        car.moveTo(390,500)
      

    if keys.Pressed[K_ESCAPE]:
        game.quit()
    if keys.Pressed[K_RIGHT]:
        car.x += 8
        drive.play()
    if keys.Pressed[K_LEFT]:
        car.x -= 8
        drive.play()
    game.update(60)

#Ending Screen
game.over=False
while not game.over:
    game.processInput()
    bk.draw()
    game.drawText("Crazy Car",240,50,f1)
    game.drawText("Thanks For Playing!",300,250,f2)
    game.drawText("You Lose! ",350,200,f2)
    game.drawText("Press Space Bar to End The Game",250,300,f2)
    car.draw()
    fence.draw()
    fence2.draw()
    if keys.Pressed[K_SPACE]:
        game.over=True
    game.update(60)
game.quit()

