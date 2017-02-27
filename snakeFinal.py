import pygame, random, sys
from pygame.locals import *
def collide(x1, x2, y1, y2, w1, w2, h1, h2):
    if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
        return True
    else:
        return False
def die(screen, score):
    f=pygame.font.SysFont('Arial', 30)
    t=f.render('Your score is: '+str(score), True, (255, 255, 255))
    screen.blit(t, (10, 270))
    pygame.display.update()
    pygame.time.wait(5000)
    f.close()
    pygame.display.quit()

orig_stdout = sys.stdout
xs = [290]
ys = [290]
dirs = 0
if dirs == 0:
	pygame.time.wait(3000)
	dirs = 1
score = 0
foodpos = ((random.randint(0,600)/10)*10, (random.randint(0, 600)/10)*10)
pygame.init()
s=pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake Build - v1. 3. 4')
appleimage = pygame.Surface((10, 10))
appleimage.fill((255, 255, 0))
img = pygame.Surface((10, 10))
img.fill((255, 0, 0))
f = pygame.font.SysFont('Arial', 20)
clock = pygame.time.Clock()
while True:
    print "X :" + str(xs)
    print "Y :" + str(ys)
    xd = xs[0] - foodpos[0]
    yd = ys[0] - foodpos[1]
    dist = (xd**2 + yd**2)**(0.5)
    print "dist from food: " + str(dist)
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit(0)
        elif e.type == KEYDOWN:
            if e.key == K_UP and dirs != 0:
                dirs = 2
            elif e.key == K_DOWN and dirs != 2:
                dirs = 0
            elif e.key == K_LEFT and dirs != 1:
                dirs = 3
            elif e.key == K_RIGHT and dirs != 3:
                dirs = 1
            elif e.key == K_ESCAPE:
                die(s,score)
    i = len(xs)-1
    while i >= 2:
        if collide(xs[0], xs[i], ys[0], ys[i], 10, 10, 10, 10):
            die(s, score)
        i-=1
    if collide(xs[0], foodpos[0], ys[0], foodpos[1], 10, 10, 10, 10):
        score+=1
        xs.append(600)
        ys.append(600)
        foodpos = ((random.randint(0,600)/10)*10, (random.randint(0, 600)/10)*10)
    if xs[0] < 0 or xs[0] > 600 or ys[0] < 0 or ys[0] > 600:
    	if xs[0]<0:
    		xs[0]=600
    	elif xs[0]>600:
    		xs[0]=0
    	elif ys[0]<0:
    		ys[0]=600
    	elif ys[0]>600:
    		ys[0]=0
        #die(s, score)
    i = len(xs)-1
    
    while i >= 1:
        xs[i] = xs[i-1]
        ys[i] = ys[i-1]
        i -= 1
    if dirs==0:
        ys[0] += 10
    elif dirs==1:
        xs[0] += 10
    elif dirs==2:
        ys[0] -= 10
    elif dirs==3:
        xs[0] -= 10
    s.fill((0,0,0))
    for i in range(0, len(xs)):
        s.blit(img, (xs[i], ys[i]))
    s.blit(appleimage, foodpos)
    t=f.render(str(score), True, (255, 255, 255))
    s.blit(t, (10, 10))
    sys.stdout = orig_stdout
    pygame.display.update()
