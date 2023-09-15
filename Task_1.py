"""Сейчас активно развивается новая история, основателем которой является Профессор А.С. Багиров. Он выяснил,
что на протяжении многих лет на земле вместе с людьми существовали ящеры. Строительство пирамид, захват Байкала и еще
много разных событий произошли благодаря ящерам.
Учёные ещё не выяснили, сколько времени ящеры существовали на земле. Они находят разные данные в виде даты начала и
даты окончания, и чтобы проверить их на корректность, необходимо посчитать, сколько дней ящеры существовали для двух
конкретных дат. Календарь ящеров очень похож на григорианский, лишь с тем исключением, что там нет високосных годов.
Вам даны дата начала и дата окончания существования ящеров, нужно найти количество полных дней и секунд в неполном дне,
 чтобы учёные смогли оценить, насколько даты корректны."""
import math
from datetime import datetime


# def lizard_life():
#     year1, month1, day1, hour1, min1, sec1 = input('Введите дату начала  ').split()
#     year2, month2, day2, hour2, min2, sec2 = input('Введите дату конца '). split()
#     if month1 ==
#
#     date1 = datetime(int(year1),int(month1), int(day1), int(hour1), int(min1), int(sec1))
#     date2 = datetime(int(year2),int(month2), int(day2), int(hour2), int(min2), int(sec2))
#     dt = date2-date1
#     return dt.years, dt.seconds
#
#
# print(lizard_life())



# month_d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# year1, month1, day1, hour1, min1, sec1 = input().split()
# year2, month2, day2, hour2, min2, sec2 = input(). split()
#
# if int(month1) > 1:
#     sec1 = int(year1) * 31536000 + sum(month_d[:int(month1)-1])*86400 + int(day1)*86400 + int(hour1)*3600 + int(min1)*60 + int(sec1)
#     days_1 = sec1//86400
#     secs_1 = sec1 % 86400
#
#
# if int(month2) > 1:
#     sec2 = int(year2) * 31536000 + sum(month_d[:int(month2)-1])*86400 + int(day2)*86400 + int(hour2)*3600 + int(min2)*60 + int(sec2)
#     days_2 = sec2 // 86400
#     secs_2 = sec2 % 86400
#
# secs = sec2 - sec1
# days = secs//86400
# seconds = secs % 86400
# print(days, seconds)

month_d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year1, month1, day1, hour1, min1, sec1 = input().split()
year2, month2, day2, hour2, min2, sec2 = input(). split()
date1 = datetime(int(year1),int(month1), int(day1), int(hour1), int(min1), int(sec1))
date2 = datetime(int(year2), int(month2), int(day2), int(hour2), int(min2), int(sec2))

if int(date1.month) > 1:
    sec1 = int(date1.year) * 31536000 + sum(month_d[:int(date1.month)-1])*86400 + int(date1.day)*86400 + int(date1.hour)*3600 + int(date1.minute)*60 + int(date1.second)
else:
    sec1 = int(date1.year) * 31536000 + int(date1.day)*86400 + int(date1.hour)*3600 + int(date1.minute)*60 + int(date1.second)


if int(date2.month) > 1:
    sec2 = int(date2.year) * 31536000 + sum(month_d[:int(date2.month)-1])*86400 + int(date2.day)*86400 + int(date2.hour)*3600 + int(date2.minute)*60 + int(date2.second)
else:
    sec2 = int(date2.year) * 31536000 + int(date2.day) * 86400 + int(date2.hour) * 3600 + int(date2.minute) * 60 + int(date2.second)

secs = sec2 - sec1
days = secs//86400
seconds = secs % 86400
print(days, seconds)