from pygame import *
wins = 700
winh =500
FPS = 120

window = display.set_mode((wins,winh))
display.set_caption('PING_PONG')
background = transform.scale(image.load('66.jpg'), (700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x, player_y,size_x,size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

clock = time.Clock()

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_w] and self.rect.y < 395:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_o] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_l] and self.rect.y < 395:
            self.rect.y += self.speed

sp_x = 3
sp_y = 3       
ball = GameSprite('64.png', 325,45,50,50,0)
player = Player('65.PNG', 10,200,40,100,10)
player2 = Player2('65.PNG', 650,200,40,100,10)
font.init()
font1 = font.Font(None,56)
score1 = 0
score2 = 0
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type ==  KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    if finish != True:
        
        
        window.blit(background,(0, 0))
        player.update()
        player.reset()
        player2.update()
        player2.reset()
        ball.rect.x += sp_x
        ball.rect.y += sp_y
        ball.reset()
        if sprite.collide_rect(player,ball):
            sp_x *= -1
        if sprite.collide_rect(player2,ball):
            sp_x *= -1    
        if ball.rect.y  >= 450:
            sp_y *= -1
        if ball.rect.y  <= 0:
            sp_y *= -1
        if ball.rect.x > -10:
            score2 += 1
            ball.rect.x = 

        text = font1.render(str(score1),1,(45,140,200))
        window.blit(text,(10,15))
        text2 = font1.render(str(score2),1,(200,200,200))
        window.blit(text2,(670,15))
    display.update()
    clock.tick(FPS)