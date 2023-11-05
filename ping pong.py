from pygame import *
wins = 700
winh =500
FPS = 60
window = display.set_mode((wins,winh))
display.set_caption('PING_PONG')
background = transform.scale(image.load('66.jpg'), (700,500))
window.blit(background,(0, 0))


clock = time.Clock()



game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type ==  KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    display.update()
    clock.tick(FPS)