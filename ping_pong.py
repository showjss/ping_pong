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
    def update(self):# метод передвижение
        keys_pressed = key.get_pressed()#получаем все события клавиатуры
        if keys_pressed[K_LEFT] and self.rect.x > 0:#если нажата кнопка влево и координаты больше 0 
            self.rect.x -= self.speed#тогда персонаж передвигается в лево
        if keys_pressed[K_RIGHT] and self.rect.x < 600: #если нажата кнопка в право и координаты меньше 600
            self.rect.x += self.speed#тогда персонаж передвигаается в право
    
