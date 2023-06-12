from pygame import *

class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)

        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # método que dibuja al personaje en la ventana
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    
    cooldown = 200
    last_fire = time.get_ticks()
    
    def update(self, keys):
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_ESCAPE]:
            event.post(event.Event(QUIT))
        if keys[K_SPACE]:
            self.fire()
            
    def fire(self):
        now = time.get_ticks()
        
        if now - self.last_fire >= self.cooldown:
            self.last_fire = now
            
            bullet = Bullet("bullet.png", self.rect.centerx - 7, self.rect.top, 14, 20, 15)
            bullets.add(bullet)
    
        

player = Player("rocket.png", 100, win_height - 100, 50, 50, (5) )
