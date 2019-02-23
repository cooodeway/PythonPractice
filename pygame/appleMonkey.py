import pygame
from pygame.locals import *  
from sys import exit
from random import *

SCREEN_SIZE=(640,480)

class Monkey(pygame.sprite.Sprite):
    def __init__(self, initial_position, speed=5):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("res/monkey.png").convert_alpha()
        self.image = pygame.transform.smoothscale(image,(40,40))
        self.rect=self.image.get_rect()
        self.rect.bottomright=initial_position
        self.speed=speed
        self.jumpspeed = 10*speed
        self.injump=False
        

    def moveleft(self):
        self.rect.left=self.rect.left - self.speed
        if self.rect.left<0:
            self.rect.left=0
    
    def moveright(self):
        self.rect.right = self.rect.right + self.speed
        if self.rect.right>SCREEN_SIZE[0]:
            self.rect.right = SCREEN_SIZE[0]

    def jumpup(self):
        self.injump=True
    
    def jumpmove(self):
        if self.injump:
            self.rect.bottom = self.rect.bottom - self.jumpspeed
            self.jumpspeed -= self.speed
            if self.rect.bottom > SCREEN_SIZE[1]:
                self.rect.bottom = SCREEN_SIZE[1]
                self.injump=False
                self.jumpspeed = 10* self.speed


class Apple(pygame.sprite.Sprite):
    def __init__(self, initial_position, acc=0.1, speed=0):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("res/apple.png").convert_alpha()
        self.image = pygame.transform.smoothscale(image,(20,20))
        self.rect=self.image.get_rect()
        self.rect.bottomright=initial_position
        self.acc=acc
        self.speed=speed

    def move(self):
        self.rect.bottom = self.rect.bottom + self.speed
        self.speed += self.acc
    

def main():
    pygame.init() 
    screen=pygame.display.set_mode(SCREEN_SIZE,0,32) 
    pygame.display.set_caption("猴子接苹果") 

    screen.fill((255,255,255))
    background_path="res/background.jpg"
    background=pygame.image.load(background_path).convert()
    screen.blit(background,(0,0))
    score =0

    font=pygame.font.SysFont('arial',16)
    text=font.render("Score: %s"%score, True, (0,0,0), (255,255,255)) 
    textrect = text.get_rect(centerx = 50, centery=10)
    screen.blit(text, textrect)

    clock=pygame.time.Clock()

    monkey=Monkey([SCREEN_SIZE[0]/2, SCREEN_SIZE[1]])
    apple = Apple([randint(0, SCREEN_SIZE[0]), 0])

    while True:
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()
            if event.type==pygame.KEYDOWN:
            #     if event.key==pygame.K_LEFT:
            #         monkey.moveleft()
            #     if event.key==pygame.K_RIGHT:
            #         monkey.moveright()
                if event.key==pygame.K_UP:
                    if not monkey.injump:
                        monkey.jumpup()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            monkey.moveleft()
        if key_pressed[pygame.K_RIGHT]:
            monkey.moveright()

        if monkey.injump:
            monkey.jumpmove()
        screen.blit(monkey.image,monkey.rect)
        
        oldrect = apple.rect
        apple.move()
        newrect = apple.rect
        if pygame.Rect.colliderect(monkey.rect, pygame.Rect(oldrect.left,oldrect.top, newrect.width,newrect.top+newrect.height-oldrect.top)):
            score+=1
            text=font.render("Score: %s"%score, True, (0,0,0), (255,255,255))  
            apple = Apple([randint(0, SCREEN_SIZE[0]), 0])
        if apple.rect.bottom > SCREEN_SIZE[1]:
            text = font.render("Game Over! Total Score:%s"% score, True, (0,0,0), (255,255,255))
            screen.blit(text, text.get_rect(centerx = 320, centery=240))
            pygame.display.update()
            pygame.time.delay(5000)
            exit()

        # print(apple.rect.bottom)
        screen.blit(apple.image, apple.rect)

        screen.blit(text, textrect)

        pygame.display.update()
        clock.tick(60)
            
if __name__=="__main__":
    main()


