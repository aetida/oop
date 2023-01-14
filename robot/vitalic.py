import time

class MoreThanOneRobotException(Exception):
    def __str__(self):
        return '\033[31m{}\033[0m'.format('It is impossible to create another one robot!')

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instances[cls]
        print('Ошибка: нельзя создать ещё одного робота!')  
        return None

class Robot(metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self._serial_number = 'АА001221-56'
        self._name = '-'
        self._place = '-'
        self._functionality = '-'

    def __str__(self):
        return f'Серийный номер: {self._serial_number}\n' + \
                f'Наименование: {self._name}\n' + \
                f'Место нахождения: {self._place}\n' + \
                f'Функциональность: {self._functionality}\n'

class RobotV(Robot):
    def __init__(self):
        super().__init__()
        self._name = 'B'
        self._place = 'Завод'

class RobotDecorator(Robot):
    def __init__(self, robot):
        super().__init__()
        self._robot = robot

class RobotVita(RobotDecorator):
    def __init__(self, robot):
        super().__init__(robot)
        self._name = 'Вита'
        self._place = '"ООО Кошмарик"'
        self._functionality = '"постройка домов"\n"постройка сараев"'

class RobotVitaliy(RobotDecorator):
    def __init__(self, robot):
        super().__init__(robot)
        self._name = 'Виталий'
        self._place = '"ООО Кошмарик"'
        self._functionality = robot._functionality + '\n"добавление этажей к постройке"\n"снос верхнего этажа у постройки"'

if __name__ == '__main__':

    print('Создание робота...')
    time.sleep(3)
    robotV = RobotV()
    print('\nХарактеристики робота после создания:', robotV)
    
    print('Обучение робота...\n')
    time.sleep(3)
    robotVita = RobotVita(robotV)
    print('\nХарактеристики робота после первичного обучения:', robotVita)
    
    print('Эксплуатация робота...\n')
    time.sleep(3)
    robotVitaliy = RobotVitaliy(robotVita)
    print('\nХарактеристики робота после эксплуатации:', robotVitaliy)