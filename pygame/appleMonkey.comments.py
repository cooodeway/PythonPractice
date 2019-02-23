import pygame
from pygame.locals import *  #引入Flag 等系列常量
from sys import exit

SCREEN_SIZE=(640,480)

class Monkey(pygame.sprite.Sprite):
    def __init__(self, initial_position, speed=1)
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,40])
        self.image.fill("res/monkey.png")
        self.rect=self.image.get_rect()
        self.rect.bottomright=initial_position
        self.speed=speed
        self.jumpspeed = 4*speed
        self.injump=False
        

    def moveleft(self):
        self.rect.left=self.rect.left - self.speed
        if self.rect.left<0：
            self.rect.left=0
    
    def moveright(self):
        self.rect.right = self.rect.right + self.speed
        if self.rect.right>SCREEN_SIZE[0]:
            self.rect.right = SCREEN_SIZE[0]

    def jumpup(self):
        self.injump=True
    
    def jumpmove(self):
        if self.injump:
            self.rect.bottom = self.rect.bottom + self.jumpspeed
            self.jumpspeed -= speed
            if self.rect.bottom > SCREEN_SIZE[1]:
                self.rect.bottom = SCREEN_SIZE[1]
                self.injump=False
                self.jumpspeed = 4* speed


class Apple(pygame.sprite.Sprite):
    def __init__(self, initial_position, acc=1, speed=0)
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([20,20])
        self.image.fill("res/apple.png")
        self.rect=self.image.get_rect()
        self.rect.bottomright=initial_position
        self.acc=acc
        self.speed=speed

    def move(self):
        self.rect.bottom = self.rect.bottom - speed
        self.speed += self.acc
    

def main():
    pygame.init() #初始化，为使用硬件做准备
    screen=pygame.display.set_mode(SCREEN_SIZE,DOUBLEBUF|HWSURFACE|RESIZABLE,32) #窗口大小，窗口标志，色彩位数
    pygame.display.set_caption("猴子接苹果") #窗口标题

    screen.fill((255,255,255))

    score =0
    #字体
    font=pygame.font.SysFont('arial',16)
    font_height=font.get_linesize()
    scoredisplay=font.render("得分：%s"%score, True, (0,0,0), (255,255,255)) #文本，是否开启抗锯齿，字体颜色，背景色

    monkey=Monkey([SCREEN_SIZE[0]/2, SCREEN_SIZE[1]], 1)
    rd = SCREEN_SIZE[0]/2
    apple = Apple([rd, 0], 1, 0)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    monkey.moveleft()
                if event.key==pygame.K_RIGHT:
                    monkey.moveright()
                if event.key==pygame.K_UP:
                    if not monkey.injump:
                        monkey.jumpup()

        if monkey.injump:
            monkey.jumpmove
        screen.blit(monkey.image,monkey.rect)
            
        apple.move()
        if pygame.Rect.collidelistall([monkey.rect,apple.rect]):
            score+=1
            scoredisplay=font.render("得分：%s"%score, True, (0,0,0), (255,255,255))
            apple = Apple([rd, 0], 1, 0)
        scrren.blit(apple.image, apple.rect)

        pygame.display.update()
        pygame.time.delay(20)
            
        

        #刷新画面
        
        # if event.type==VIDEORESIZE:
        #     # if event.size != None:           
        #     SCREEN_SIZE=event.size
        #     background = pygame.transform.smoothscale(background, SCREEN_SIZE)
        #     screen=pygame.display.set_mode(SCREEN_SIZE,RESIZABLE,32)
        #     screen.blit(background,(0,0))

#加载图片并转换
# background_path="res/sushiplate.jpg"
# cursor_icon_path="res/fugu.png"
# background=pygame.image.load(background_path).convert()
# cursor=pygame.image.load(cursor_icon_path).convert_alpha()
# #图片剪裁
# rect=pygame.Rect(16,16,32,32) #LEFT,TOP,WIDTH,HEIGHT
# cursor=cursor.subsurface(rect)
# print(cursor)
#-----------------------------------------------------
#convert:将图像数据转化为Surface对象,必须有
#convert_alpha:同Convert且保留Alpha通道信息
#-----------------------------------------------------
#图片保存
#pygame.image.save({surface},{path})

            # for y in range(0,SCREEN_SIZE[1],background.get_height()):
            #     for x in range(0,SCREEN_SIZE[0],background.get_width()):
            #         screen.blit(background,(x,y)) #重新填满背景
            #或者使用pygame.transform.smoothscale({surface},({size}))
#-----------------------------------------------------
#事件类型：
# 窗口：QUIT,ATiVEEVENT,VIDEORESIZE,VIDEOEXPOSE; 
# 用户：USEREVENT;
# 键盘：KEYDOWN,KEYUP;
# 鼠标：MOUSEMOTION,MOUSEBUTTONDOWN,MOUSEBUTTONUP;
# 手柄：JOYAXISMOTION,JOYBALLMOTION,JOYHATMOTION,JOYBUTTONDOWN,JOYBUTTONUP
#获取事件的方法：
#pygame.event.get;pygame.event.wait;pygame.event.epoll();
#事件的参数：
#KEY(key,mod,unicode) key=K_{键名，如：a,space,enter,return等}， mod“组合键信息”={用位运算获取mod&KMOD_CTRL,mod&KMOD_SHIFT,mod&KMOD_ALT}, unicode键值
#VIDEORESIZE(size,w,h)
#事件的模拟：
#myevent = pygame.event.Event(KEYDOWN,key=K_SPACE,mod=0,unicode=u' ') or pygame.event.Event(KEYDOWN,{key:K_SPACE,mod:0,unicode:u' '})
#pygame.event.post(myevent)
#事件的过滤：
#pygame.event.set_blocked({eventname})
#ex. pygame.event.set_blocked([KEYDOWN,KEYUP])
#事件允许
#pygame.event.set_allowed({eventname})
#-----------------------------------------------------
    #贴背景图
    screen.blit(background,(0,0))
    # #贴鼠标
    # x,y=pygame.mouse.get_pos()
    # x-=cursor.get_width()/2
    # y-=cursor.get_width()/2
    # screen.blit(cursor,(x,y))


#---------------------------------------------------------
#blit:参数分别为Surface对象，左上角位置
#---------------------------------------------------------



