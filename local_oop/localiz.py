import ctypes
import locale

from typing import Dict, List

class Local():
    __lang_en = 'en'
    __lang_ru = 'ru'
    __langs = [__lang_en, __lang_ru]

    __data: Dict = {
        'create of robot': {
            __lang_ru: 'создание робота',
            __lang_en: 'create of robot',
        },
        'robot training': {
            __lang_ru: 'обучение робота',
            __lang_en: 'robot training',
        },
        'robot operation': {
            __lang_ru: 'эксплуатация робота',
            __lang_en: 'robot operation',
        },
        'characteristics of the robot': {
            __lang_ru: 'характеристики робота',
            __lang_en: 'characteristics of the robot',
        },
        'after creation': {
            __lang_ru: 'после создания',
            __lang_en: 'after creation',
        },
        'after primary education': {
            __lang_ru: 'после первичного обучения',
            __lang_en: 'after primary education',
        },
        'after operation': {
            __lang_ru: 'после эксплуатации',
            __lang_en: 'after operation',
        },
        'it is impossible to create another one robot': {
            __lang_ru: 'невозможно создать еще одного робота',
            __lang_en: 'it is impossible to create another one robot'
        },
        'v': {
            __lang_ru: 'в',
            __lang_en: 'v',
        },
        'vita': {
            __lang_ru: 'вита',
            __lang_en: 'vita',
        },
        'vitaliy': {
            __lang_ru: 'виталий',
            __lang_en: 'vitaliy', 
        },
        'serial number': {
            __lang_ru: 'серийный номер',
            __lang_en: 'serial number',
        }, 
        'name': {
            __lang_ru: 'наименование',
            __lang_en: 'name',
        },
        'location': {
            __lang_ru: 'местонахождение',
            __lang_en: 'location'
        },
        'functionality': {
            __lang_ru: 'функциональность',
            __lang_en: 'functionality',
        },
        'factory': {
            __lang_ru: 'завод',
            __lang_en: 'factory',
        },
        '"OOO Koshmarik"': {
            __lang_ru: '"ООО Кошмарик"',
            __lang_en: '"OOO Koshmarik"',
        },
        'building houses': {
            __lang_ru: 'постройка домов',
            __lang_en: 'building houses',
        },
        'shed building': {
            __lang_ru: 'постройка сараев', 
            __lang_en: 'shed building',
        },
        'adding floors to a building': {
            __lang_ru: 'добавление этажей к постройке', 
            __lang_en: 'adding floors to a building',
        },
        'demolition of the upper floor of the building': {
            __lang_ru: 'снос верхнего этажа у постройки', 
            __lang_en: 'demolition of the upper floor of the building',
        },
        'this phrase does not exist in the database': {
            __lang_ru: 'в базе данной фразы не существует', 
            __lang_en: 'this phrase does not exist in the database',
        },
        'the language you selected does not exist in the database': {
            __lang_ru: 'выбранного языка не существует в базе',
            __lang_en: 'the language you selected does not exist in the database',
        },
        'try again': {
            __lang_ru: 'попробуйте ещё раз',
            __lang_en: 'try again',
        },
        'choose language': {
            __lang_ru: 'выберите язык',
            __lang_en: 'choose language',
        },
        'completed': {
            __lang_ru: 'выполнено',
            __lang_en: 'completed',
        }
    }

    @staticmethod
    def get_langs_list() -> List:
        return Local.__langs

    @staticmethod
    def get_default_lang():
        windll = ctypes.windll.kernel32
        windll.GetUserDefaultUILanguage()
        lang = locale.windows_locale[windll.GetUserDefaultUILanguage()]

        if lang[:2] not in Local.get_langs_list():
            return 'en'
        return lang[:2]

    def __init__(self, lang=__lang_ru):
        lang = lang.lower()
        if lang not in self.get_langs_list():
            raise Exception('The language you selected does not exist in the database')
        
        self.__lang = lang

    def traslate(self, text : str) -> str:
        text = text.lower() if '"' not in text else text
        if text not in self.__data.keys():
            error_text = 'this phrase does not exist in the database'
            raise Exception(self.__data[error_text][self.__lang].capitalize())
        
        return self.__data[text][self.__lang]
        