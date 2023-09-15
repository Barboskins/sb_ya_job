"""Даны два числа A и B. Вам нужно вычислить их сумму A + B. В этой задаче для работы с входными и
выходными данными вы можете использовать и файлы и потоки на ваше усмотрение."""

# A,B = input().split()
# C = int(A) + int(B)
# print(C)

"""Даны два числа A и B. Вам нужно вычислить их сумму A+B. В этой задаче вам нужно читать из файла и выводить ответ в файл"""

# data = []
# with open('input.txt', 'rt') as f:
#     m = f.read()
#     r = [int(x) for x in m.split()]
#     # print(type(sum(r)))
#     with open('output.txt', 'wt') as f:
#         f.write(str(sum(r)))

    # for l in f:
    #     print(l.strip())
    # for line in f:
    #     data.append(int(x) for x in line.split())
    #     for i in data:
    #         sum(i)
    #         print(i)
    # data = f.readline()
    # print(data)
    # summ = int(data[0]) + int(data[2])
    # with open('output.txt', 'wt') as f:
    #     f.write(str(summ))

"""Даны две строки строчных латинских символов: строка J и строка S. Символы, входящие в строку J, — «драгоценности», 
входящие в строку S — «камни». Нужно определить, какое количество символов из S одновременно являются «драгоценностями». 
Проще говоря, нужно проверить, какое количество символов из S входит в J.
Это разминочная задача, к которой мы размещаем готовые решения. Она очень простая и нужна для того, чтобы вы могли 
познакомиться с нашей автоматической системой проверки решений. Ввод и вывод осуществляется через файлы, либо через 
стандартные потоки ввода-вывода, как вам удобнее"""

# J = input()
# S = input()
#
# n = 0
# for el in S:
#     if el in J:
#         n +=1
# print(n)


# def f(a, b):
#     print(a)
# x = {'a': 'Hello', 'b': 'World'}
# f(**x)
import requests
from bs4 import BeautifulSoup
from collections import Counter
from operator import itemgetter
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.143 YaBrowser/22.5.0.1884 Yowser/2.5 Safari/537.36"
}
url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

# names_dict = {}
names_dict = Counter()
order = {}
req = requests.get(url, headers=headers).text
run = True
while run:
    soup = BeautifulSoup(req, 'html.parser')

    block = soup.find('div', class_='mw-category mw-category-columns')
    category_letter = block.find_all('div', class_='mw-category-group')
    # print(category_letter)
    # for el in category_letter:
    #     category = el.find('h3').text
        # print(category)

    # category = category_letter.find('h3')
    # print(category)
    animal_names = block.find_all('li')

    animals_names = []
    for animal in animal_names:
        animal_name = animal.text
        animals_names.append(animal_name)
    # print(animals_names)
    names = 0
    for el in category_letter:
        category = el.find('h3').text
        if category == 'A':
            run = False
        else:
            for name in animals_names:
                if name.startswith(category):
                    names_dict[category] += 1
                    # print(names_dict)

            # names += 1
            # names_dict[category] = names
    # names_dict = {}
    # names_dict.update({category: names})
    # print(names_dict)
            # names_dict[category] +=1

            # names_dict[category] = names
            # names_dict = {}
            # names_dict.update({category: names})
    # print(names_dict)
    # for key in names_dict:
    #     names_dict[key] += int(names_dict[key])
    # print(names_dict)

    # names_dict.update({category: names})



    # for key in names_dict:
    #     try:
    #         order[key] += int(names_dict[key])
    #     except:
    #         order[key] = int(names_dict[key])
    # print(order)
    # for key, value in order.items():
    #     print(key, value)

    links = soup.find('div', id='mw-pages').find_all('a')
    for a in links:
        if a.text == 'Следующая страница':
            url = 'https://ru.wikipedia.org/' + a.get('href')
            req = requests.get(url).text

    # if category == 'Я':
    #     break
c = sorted(names_dict.items(), key=itemgetter(0))
# print(c)
# print(order)

import csv

with open('beasts.csv', 'wt', encoding='utf-8') as f:
    rec = csv.writer(f)
    rec.writerows(c)

