from pygame import*
backgrounde = transform.scale(image.load("Background.jpg"), (700, 500))
clock = time.Clock()
FPS = 60
display.set_caption('Idk')
font.init()
font2 = font.Font(None, 36)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), [size_x, size_y])
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = "left"
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
class Player2(GameSprite):    
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
window = display.set_mode((700, 500))
playing = True
finish = False
player1 = Player1("platform.png", 0, 410, 5, 50, 100)
player2 = Player2("platform.png", 650, 410, 5, 50, 100)
ball = GameSprite("ball.png", 250, 100, 5, 50 , 50)
speed_x = 5
speed_y = 5
while playing:
    for e in event.get():
        if e.type == QUIT:
            playing = False
    if finish != True:
        ball.rect.y += speed_y
        ball.rect.x += speed_x
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
        if ball.rect.y > 450 or ball.rect.y < 5:
            speed_y *= -1
        if ball.rect.x > 0:
            text_lose = font2.render("Пропущено:", 1, (255,255,255))
            window.blit(text_lose, (250,250))
        window.blit(backgrounde,(0, 0))
        ball.reset()
        ball.update()
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        display.update()
        clock.tick(40)