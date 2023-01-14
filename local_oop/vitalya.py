import itertools
import os
import time


from localiz import Local

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
        self._ = Local(Local.get_default_lang())
        self._serial_number = 'АА001221-56'
        self._name = '-'
        self._place = '-'
        self._functionality = '-'

    def __str__(self):
        def formating(phrases : str):
            if phrases == '-':
                return '-'

            phrases = phrases.split('\n')
            text = []
            for phrase in phrases:
                text.append(self._.traslate(phrase))
            text = ',\n'.join(text)
            if '"' not in text:
                return text.capitalize()
            return text

        return f'{formating("serial number")}: {self._serial_number}.\n' + \
                f'{formating("name")}: {formating(self._name)}.\n' + \
                f'{formating("location")}: {formating(self._place)}.\n' + \
                f'{formating("functionality")}: {formating(self._functionality)}.\n'

class RobotV(Robot):
    def __init__(self, lang : Local = None):
        super().__init__()
        if lang != None:
            self._ = lang
        self._name = 'v'
        self._place = 'factory'

class RobotDecorator(Robot):
    def __init__(self, robot, lang : Local = None):
        super().__init__()
        if lang != None:
            self._ = lang
        self._robot = robot

class RobotVita(RobotDecorator):
    def __init__(self, robot, lang : Local = None):
        super().__init__(robot, lang)
        self._name = 'vita'
        self._place = '"OOO Koshmarik"'
        self._functionality = 'building houses\nshed building'

class RobotVitaliy(RobotDecorator):
    def __init__(self, robot, lang : Local = None):
        super().__init__(robot, lang)
        self._name = 'vitaliy'
        self._place = '"OOO Koshmarik"'
        self._functionality = robot._functionality + '\nadding floors to a building\ndemolition of the upper floor of the building'

def input_lang():
    _ = Local(Local.get_default_lang())

    input_text = _.traslate('choose language').capitalize()
    error_text = _.traslate('the language you selected does not exist in the database').capitalize() + \
                            '! ' + _.traslate('try again').capitalize() + '...'
    langs = _.get_langs_list()

    print(input_text + ':')
    for i in range(len(langs)):
        print(str(i + 1) + ' - ' + langs[i])

    while True:
        num = int(input('- '))

        if num < 1 or num > len(langs):
            print('\033[31m{}\033[0m'.format(error_text))
            continue
        
        return Local(langs[num - 1])

if __name__ == '__main__':
    _ = input_lang()
    
    def formating(*phrases):
        text = []
        for phrase in phrases:
            text.append(_.traslate(phrase))
        return ' '.join(text).capitalize()

    createRobotMsg = formating('create of robot') + '...'
    robotTrainMsg = formating('robot training') + ':'
    robotOperationMsg = formating('robot operation') + ':'
    chsRobotCreateMsg = formating('characteristics of the robot', 
                                    'after creation') + ':'
    chsRobotPrimEdMsg = formating('characteristics of the robot',
                                    'after primary education') + ':'
    chsRobotOperationMsg = formating('characteristics of the robot',
                                    'after operation') + ':'
    doneMsg = formating('completed')

    print(createRobotMsg)
    time.sleep(3)
    robotV = RobotV(lang=_)
    print(chsRobotCreateMsg, '\n',  robotV)
    time.sleep(1)
    
    print(createRobotMsg)
    time.sleep(3)
    robotVita = RobotVita(robotV, lang=_)
    print(chsRobotPrimEdMsg,'\n', robotVita)
    time.sleep(1)
    
    print(createRobotMsg)    
    time.sleep(3)
    robotVitaliy = RobotVitaliy(robotVita, lang=_)
    print(chsRobotOperationMsg, '\n',robotVitaliy)
    time.sleep(1)

