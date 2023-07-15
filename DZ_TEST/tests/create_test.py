from main import search_terms, geo_id, maximum_volume
from yandex import Yandex
from dotenv import load_dotenv, find_dotenv
import os
import pytest

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

#проверка тестами первое задание
class Testmain_py:
    def test_search_terms(self):
        terms = queries
        extected = ['Поисквых запросов из 2 слов 42.86%', 'Поисквых запросов из 3 слов 57.14%']
        result = search_terms(terms)
        assert result == extected

    def test_geo_id(self):
        geo_ids = ids
        extected = [15, 35, 54, 98, 119, 213]
        result = geo_id(geo_ids)
        assert result == extected

    def test_max_values(self):
        dict_ = stats
        extected = 'yandex'
        result = maximum_volume(dict_)
        assert result == extected

#проверка тестами второе задание яндекса
class TestYandex:

    def test_yandex_code(self):
        path = 'яндекс папка'
        load_dotenv(find_dotenv())
        ya = Yandex(os.getenv('Token_yandex'))
        resoult = ya.create_folder(path)
        if resoult == 401:
            print('Переданы неверные параметры')
        if resoult == 409:
            print('Такая папка уже существует')
        if resoult == 201 or resoult == 200:
            print('результат создания папки — папка появилась в списке файлов.')