import pygame,random
pygame.init()
man = pygame.display.set_mode((500,750))
background_image = pygame.image.load('pup.jpg')   # surfaces/blocks
bird_image  =pygame.image.load('john.png')
logo=pygame.image.load('log.png')
mon=pygame.image.load("mon.jpg")
optparse_x=random.randint(0,400)
optparse_y=random.randint(150,450)
bird_y=300 
score = 0
score_font=pygame.font.Font("freesansbold.ttf",32)
def scoring(score):
    display =score_font.render("Monadscore:"+str(score) ,True,(255,255,255))
    man.blit(display,(10,10))
    # if score>optparse_x:

def display_bird(y):
    man.blit(bird_image, (200,y))
    man.blit(logo,(1,75))
    #man.blit(mon,(635,750))
def display_obstacle():
    pygame.draw.rect(man, (100, 255, 100), (optparse_x, 0, 70, optparse_y)) # left,top,width,height
    obstacle_gap=150
    pygame.draw.rect(man,(100,255,100), (optparse_x,optparse_y+obstacle_gap,70,635-(obstacle_gap+optparse_y)))
def display_bird(y):
    man.blit(logo, (100, 100))
    man.blit(bird_image, (100,y))
    man.blit(logo,(100,100))
    # man.blit(mon,(100,100))

def collising(optparse_x,optparse_y,bird_y):
    if optparse_x>=100 and optparse_x<=100+75:
        if bird_y<=optparse_y or bird_y>=(635-(485-optparse_y)):#485
           pygame.quit()
while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
             pygame.quit()
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_SPACE:
                bird_y=bird_y-40
            if score>=5:
                bird_y=bird_y-50
        if events.type ==pygame.KEYUP:
            if events.key == pygame.K_SPACE:
                bird_y=bird_y+15
        if collising(optparse_x, optparse_y, bird_y):
            print("Game Over! Final Score:", score)
    man.fill((255, 255, 255))
    man.blit(background_image, (0, 0))  # image
    man.blit(mon, (0,635 ))
    bird_y=bird_y+1
    optparse_x=optparse_x-1
    if score>=5:
        optparse_x=optparse_x-2
    #optparse_y =optparse_y+ 1

    if optparse_x<=10:
        optparse_x=400
        optparse_y = random.randint(150, 450)
        score += 1

    if bird_y<=0:
        bird_y=0
    if bird_y>=570:
        bird_y=57

    display_obstacle()
    display_bird(bird_y)
    display_obstacle()
    scoring(score)
    collising(optparse_x,optparse_y,bird_y)
    pygame.display.update()
#pygame.quit()