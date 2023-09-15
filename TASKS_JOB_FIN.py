from pprint import pprint
"""Необходимо реализовать декоратор @strict Декоратор проверяет соответствие типов переданных в вызов
функции аргументов типам аргументов, объявленным в прототипе функции. (подсказка: аннотации типов аргументов можно
получить из атрибута объекта функции func.__annotations__ или с помощью модуля inspect) При несоответствии типов бросать
исключение TypeError Гарантируется, что параметры в декорируемых функциях будут следующих типов: bool, int, float, str
Гарантируется, что в декорируемых функциях не будет значений параметров, заданных по умолчанию"""

def strict(func):
    def check(arg1, arg2):
        if list(func.__annotations__.values())[0] == type(arg1) and list(func.__annotations__.values())[1] == type(arg2):
            return func(arg1, arg2)
        else:
            raise TypeError
    return check

@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError

"""Необходимо реализовать скрипт, который будет получать с русскоязычной википедии список всех животных 
(https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту) и записывать в файл в формате beasts.csv количество 
животных на каждую букву алфавита. Содержимое результирующего файла:"""

import requests
from bs4 import BeautifulSoup
from collections import Counter
import csv
from operator import itemgetter

url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.143 YaBrowser/22.5.0.1884 Yowser/2.5 Safari/537.36"
# }
names_dict = Counter()


def count_animals(url):
    run = True
    req = requests.get(url).text
    while run:
        soup = BeautifulSoup(req, 'html.parser')
        block = soup.find('div', class_='mw-category mw-category-columns')
        category_letter = block.find_all('div', class_='mw-category-group')
        animal_names = block.find_all('li')
        animals_names = []
        for animal in animal_names:
            animal_name = animal.text
            animals_names.append(animal_name)
        names = 0
        for el in category_letter:
            category = el.find('h3').text
            if category == 'A':
                run = False
            else:
                for name in animals_names:
                    if name.startswith(category):
                        names_dict[category] += 1
        links = soup.find('div', id='mw-pages').find_all('a')
        for a in links:
            if a.text == 'Следующая страница':
                url = 'https://ru.wikipedia.org/' + a.get('href')
                req = requests.get(url).text
    return names_dict



def data_file(func):
    sort = sorted(func.items(), key=itemgetter(0))
    with open('beasts.csv', 'wt', encoding='utf-8') as f:
        rec = csv.writer(f)
        rec.writerows(sort)
    return 'Файл создан'


# print(data_file(count_animals(url)))

"""Когда пользователь заходит на страницу урока, мы сохраняем время его захода. Когда пользователь выходит с урока 
(или закрывает вкладку, браузер – в общем как-то разрывает соединение с сервером), мы фиксируем время выхода с урока. 
Время присутствия каждого пользователя на уроке хранится у нас в виде интервалов. В функцию передается словарь, 
содержащий три списка с таймстемпами (время в секундах): lesson – начало и конец урока pupil – интервалы присутствия ученика 
tutor – интервалы присутствия учителя Интервалы устроены следующим образом – это всегда список из четного количества элементов. 
Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока. 
Нужно написать функцию appearance, которая получает на вход словарь с интервалами и возвращает время общего присутствия 
ученика и учителя на уроке (в секундах)."""


