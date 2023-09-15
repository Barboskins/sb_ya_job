# Напишите программу для симуляции торговли на финансовых рынках, включая методы для выполнения транзакций покупки и
# продажи активов и получения текущей стоимости портфеля.


from decimal import Decimal
from enum import Enum

briefcase = {}


class AssetPrice(Enum):
    # Котировальный список активов.
    LKOH = Decimal(5896)
    SBER = Decimal(250)
# print(format(AssetPrice.LKOH.name))

# for el in AssetPrice:
#     print(el.name)

def show_asset():
    print('Котировальный список активов:')
    for asset in AssetPrice:
        print('{:10} = {}'.format(asset.name, asset.value))
    return 'Конец списка'


def purchase():
    name_asset = input('Введите название актива: ')
    for el in AssetPrice:
        if name_asset == el.name:
            print(el.value)
            briefcase[el.name] = int(el.value)
        else:
            'Такого актива нет'

    return f'Ваш портфель пополнился активом {list(briefcase.keys())}'



# print(show_asset())
#
# print(purchase())

# number = Decimal(0.1)
# # number = number + 2
# print(number)
