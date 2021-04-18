from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,image1,speed1,x,y):
        super().__init__()
        self.image = transform.scale(image.load(image1),(65, 65))
        self.speed = speed1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed
class Enemy(GameSprite):
    way = 'left'
    def update(self, x1, x2):
        if self.rect.x <= x1:
            self.way = 'right'
        if self.rect.x >= x2:
            self.way = 'left'
        if self.way == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed



class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,width,height,x,y):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

w1 = Wall(154, 20, 30, 10, 130, 280, 0)
w2 = Wall(114, 20, 30, 10, 300, 20, 120)
w3 = Wall(114, 20, 30, 270, 10, 20, 120)
w4 = Wall(114, 20, 30, 10, 10, 400, 110)
w5 = Wall(114, 20, 30, 10, 200, 400, 120)
w6 = Wall(114, 20, 30, 10, 400, 400, 120)
w7 = Wall(114, 20, 30, 250, 10, 20, 420)
w8 = Wall(114, 20, 30, 250, 10, 150, 320)
w9 = Wall(114, 20, 30, 150, 10, 550, 120)
w10 = Wall(114, 20, 30, 150, 10, 400, 220)
w11 = Wall(114, 20, 30, 10, 110, 150, 220)
w12 = Wall(114, 20, 50, 10, 130, 280, 100)
w13 = Wall(114, 20, 30, 180, 10, 520, 310)
w14 = Wall(114, 20, 30, 180, 10, 520, 400)


font.init()
font = font.SysFont('Arial', 100)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))
                

window = display.set_mode((700, 500))

display.set_caption("Лабиринт")

background = transform.scale(image.load("prypyat.png"), (700, 500))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

music_win = mixer.Sound('money.ogg')
music_lose = mixer.Sound('kick.ogg')


player = Player('stalker.png',10,0,440)
monster = Enemy('Bandit.png',4,500,330)
gold = GameSprite('clondaik.png',0,600,430)
killer = Enemy('mutant.png',3,280,10)

clock = time.Clock()
FPS = 30
game = True
finish = False
while game:


    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        gold.reset()
        player.reset()
        monster.update(420, 640)
        monster.reset()
        killer.update(285, 640)
        killer.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        if sprite.collide_rect(player,gold):
            finish= True
            window.blit(win, (150, 150))
            music_win.play()

        if  sprite.collide_rect(player,monster) or sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2) or sprite.collide_rect(player,w3) or sprite.collide_rect(player,w4) or sprite.collide_rect(player,w5) or sprite.collide_rect(player,w6) or sprite.collide_rect(player,w7) or sprite.collide_rect(player,w8) or sprite.collide_rect(player,w9) or sprite.collide_rect(player,killer) or sprite.collide_rect(player,w10) or sprite.collide_rect(player,w11) or sprite.collide_rect(player,w12) or sprite.collide_rect(player,w13) or sprite.collide_rect(player,w14):
            finish = True
            window.blit(lose, (150, 150))
            music_lose.play()

    display.update()
    clock.tick(FPS)