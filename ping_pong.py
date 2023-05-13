from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
bg = transform.scale(image.load('bg.jpg'), (700, 500))
class GameSprite(sprite.Sprite): #создаем класс наследник 
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):#конструктор ининт
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))#изображение
        self.speed = player_speed#скорость
        self.rect = self.image.get_rect()#приямоугольник в который вписан спрайт
        self.rect.x = player_x#положение по х
        self.rect.y = player_y#положение по у
        self.width = player_width#ширина
        self.height = player_height#высота
    def reset(self):#метод отрисовка
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):#создаем класс наследник
    def update_r(self):# метод передвижение
        keys_pressed = key.get_pressed()#получаем все события клавиатуры
        if keys_pressed[K_UP] and self.rect.y > 5:#если нажата кнопка влево и координаты больше 0 
            self.rect.y -= self.speed#тогда персонаж передвигается в лево
        if keys_pressed[K_DOWN] and self.rect.y < 400: #если нажата кнопка в право и координаты меньше 600
            self.rect.y += self.speed#тогда персонаж передвигаается в прав
    def update_l(self):# метод передвижение
        keys_pressed = key.get_pressed()#получаем все события клавиатуры
        if keys_pressed[K_w] and self.rect.y > 5:#если нажата кнопка влево и координаты больше 0 
            self.rect.y -= self.speed#тогда персонаж передвигается в лево
        if keys_pressed[K_s] and self.rect.y < 400 : #если нажата кнопка в право и координаты меньше 600
            self.rect.y += self.speed#тогда персонаж передвигаается в прав
racket1 = Player('racket.png', 10, 10, 5, 10, 100)
racket2 = Player('racket.png', 680, 400, 5, 10, 100)
game = True
while game:
    window.blit(bg,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    racket1.update_l()
    racket1.reset()
    racket2.update_r()
    racket2.reset()
    display.update()
