class Horse:

    def __init__(self, x_distance: int = 0, sound = 'Frrr'):
        self.sound = sound
        self.x_distance = x_distance

    def run(self, dx):
        self.x_distance += dx  # Увеличиваем пройденный путь
#        print(f'{self.x_distance}')

class Eagle:

#    y_distance = 0
#    sound = 'I train, eat, sleep, and repeat'
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
    def fly(self, dy):  #dy - изменение дистанции, увеличивает y_distance на dy.
        self.y_distance += dy  # Увеличиваем
#        print(f'{self.y_distance}')

class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)  # Инициализация родительского класса Horse
        Eagle.__init__(self)  # Инициализация родительского класса Eagle

    def move(self, dx, dy):
        self.run(dx)  # Запускаем метод run из класса Horse
        self.fly(dy)  # Запускаем метод fly из класса Eagle

    def get_pos(self):
        return (self.x_distance, self.y_distance)  # Возвращаем текущее положение

    def voice(self):
        print(f'{self.sound}')


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
