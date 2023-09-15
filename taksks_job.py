from pprint import pprint
"""Необходимо реализовать декоратор @strict Декоратор проверяет соответствие типов переданных в вызов
функции аргументов типам аргументов, объявленным в прототипе функции. (подсказка: аннотации типов аргументов можно
получить из атрибута объекта функции func.__annotations__ или с помощью модуля inspect) При несоответствии типов бросать
исключение TypeError Гарантируется, что параметры в декорируемых функциях будут следующих типов: bool, int, float, str
Гарантируется, что в декорируемых функциях не будет значений параметров, заданных по умолчанию"""



# def strict(func):
#     def check(arg1, arg2):
#         # print(func.__annotations__.items())
#         # print(type(arg1))
#         # print(list(func.__annotations__.values())[0])
#         if list(func.__annotations__.values())[0] == type(arg1) and list(func.__annotations__.values())[1] == type(arg2):
#             print('OK')
#             return func(arg1, arg2)
#         else:
#             raise TypeError
#     return check



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
import wikipedia

url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.143 YaBrowser/22.5.0.1884 Yowser/2.5 Safari/537.36"
}
resp = requests.get(url, headers=headers)
# print(resp.text)
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)
block = soup.find('div', class_='mw-category mw-category-columns') #сылки на всех животных со страницы
# print(block)
# print('---------------')
category_group = block.find('div', class_='mw-category-group')
# print(category_group)
"""Получаем категорию животных, букву с которой начинается: """
category = category_group.find_next('h3')
# print(category.text)
"""Получаем список всех животных с именами и ссылками """
animals_name = block.find_all('li')
# print(animals_name)
"""Получаем список всех имен животных на странице"""
animals = []
for animal in animals_name:
    animal_name = animal.text
    animals.append(animal_name)
# print(animals)

"""Присваиваем сколько животных на эту букву находится на странице"""
names = 0
for name in animals:
    if name.startswith(category.text):
        names += 1
names_dict = {}
names_dict.update({category.text: names})
# print(names_dict.keys(), ',', names_dict.values())
#
# for key, value in names_dict.items():
#     print(key,',', value)

links = soup.find('div', id='mw-pages').find_all('a') #список ссылок
pprint(links)
for a in links:
    if a.text == 'Следующая страница':
        url = 'https://ru.wikipedia.org/' + a.get('href')
        req = requests.get(url).text
        s = BeautifulSoup(req, 'html.parser')
        block2 = s.find('div', class_='mw-category mw-category-columns')
        # print(block2)






# order = {}
# for key in names_dict:
#     try:
#         order[key] += int(names_dict[key])
#     except:
#         order[key] = int(names_dict[key])

# for key, value in order.items():
#     print(key, value)


# print(animals)






# <li><a href="/wiki/%D0%90%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B5_%D1%89%D1%83%D1%87%D0%BA%D0%B8" title="Азиатские щучки">Азиатские щучки</a></li></ul></div></div>
# <li><a href="/wiki/%D0%90%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B5_%D1%89%D1%83%D1%87%D0%BA%D0%B8" title="Азиатские щучки">Азиатские щучки</a></li></ul></div>
# bs = BeautifulSoup(resp.text, 'html')
# data = bs.find('div','mw-category-group')
# # print(resp.status_code)
# print(data.text)

# resp = (wikipedia.search('Категория:Животные_по_алфавиту'))
# print(resp)

"""Когда пользователь заходит на страницу урока, мы сохраняем время его захода. Когда пользователь выходит с урока 
(или закрывает вкладку, браузер – в общем как-то разрывает соединение с сервером), мы фиксируем время выхода с урока. 
Время присутствия каждого пользователя на уроке хранится у нас в виде интервалов. В функцию передается словарь, 
содержащий три списка с таймстемпами (время в секундах): lesson – начало и конец урока pupil – интервалы присутствия ученика 
tutor – интервалы присутствия учителя Интервалы устроены следующим образом – это всегда список из четного количества элементов. 
Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока. 
Нужно написать функцию appearance, которая получает на вход словарь с интервалами и возвращает время общего присутствия 
ученика и учителя на уроке (в секундах)."""

# def appearance(intervals: dict[str, list[int]]) -> int:
#     events = []
#     for el in intervals:
#         ev = intervals[el]
#         for i in range(len(ev)):
#             events.append((ev[i], 1 - 2 * (i % 2)))
#     events.sort()
#     counter = 0
#     start = -1
#     total_time = 0
#     for event in events:
#         counter += event[1]
#         if counter == 3:
#             start = event[0]
#         if counter == 2 and start > 0:
#             total_time += event[0] - start
#             start = -1
#     return total_time

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]
# print(1594663290-1594663200)

# if __name__ == '__main__':
#    for i, test in enumerate(tests):
#        test_answer = appearance(test['intervals'])
#        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

# t = { 'lesson': [1594663200, 1594666800],'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],'tutor': [1594663290, 1594663430, 1594663443, 1594666473] }

from pprint import pprint
# t = {'lesson': [1594702800, 1594706400],
#              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
#              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]}
# events = []
# for k in t:
#     # print(k)
#     ev = t[k]
#     # print(ev)
#     for i in range(len(ev)):
#         # print(i)
#         events.append((ev[i], 1 - 2*(i%2))) # +-1 для чётного и нечетного индекса
# # print(events)
# # pprint(sorted(events))
# events.sort()
# cnt = 0
# start = -1
# elapsedtime = 0
# for e in events:
#     # print(e)
#     cnt += e[1]
#     print(cnt)
#     if cnt == 3:
#         start = e[0]
#         print(start)
#     if cnt > 3:
#         start = -1
#         print(start)
#     if cnt == 2 and start > 0:
#         # print(start)
#         elapsedtime += e[0] - start
#         start = -1
# print(elapsedtime)





# t = { 'lesson': [1594663200, 1594666800],'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],'tutor': [1594663290, 1594663430, 1594663443, 1594666473] }
# events = []
# for k in t:
#     ev = t[k]
#     for i in range(len(ev)):
#         events.append((ev[i], 1 - 2*(i%2))) # +-1 для чётного и нечетного индекса
# pprint(sorted(events))
# events.sort()
# cnt = 0
# start = -1
# elapsedtime = 0
# for e in events:
#     cnt += e[1]
#     print(cnt)
#     if cnt == 3:
#         start = e[0]
#         print(start)
#     if cnt == 2 and start > 0:
#         print(e[0])
#         elapsedtime += e[0] - start
#         start = -1
# print(elapsedtime)

# import itertools
# task = {
#     'lesson': [1594663200, 1594666800],
#     'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
#     'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
# }

# task = {'lesson': [1594702800, 1594706400],
#              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
#              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]}
#
#
# def all_events(task):
#     for v in task.values():
#         yield from zip(v, itertools.cycle((-1, 1)))
#
# # print(*all_events(task), sep='\n')
# # print('------')
# # print(*sorted(all_events(task)), sep='\n')
#
# def presence_events(task):
#     c_prev = 0
#     for time, border in sorted(all_events(task)):
#         c_next = c_prev + border
#         if c_prev == -2 and c_next == -3:
#             yield time, border
#         if c_prev == -3 and c_next == -2:
#             yield time, border
#         c_prev = c_next
#
# print(*presence_events(task), sep='\n')
#
# def presence(task):
#     return sum(t * b for t, b in presence_events(task))
#
# print(presence(task))