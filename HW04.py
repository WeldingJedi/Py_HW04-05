import random
import math
from math import pi

def check_factor(x):
    pointer = True
    for i in range(2, math.ceil(math.sqrt(x))):
        pointer = bool(x % i)
        if not pointer:
            break
    return pointer

def find_factors(x):
    factors = []
    for i in range(2, x // 2 + 1):
        while check_factor(i) and x % i == 0:
            if x % i == 0:
                factors.append(i)
                x /= i
    print(factors)

# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

def task01():

    n = random.randint(1, 1000)
    print(f'Genered number:\n{n}')
    print(f'Prime factors:')
    find_factors(n)

# task01()


# Задача 2. В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, 
# какое мороженное есть на складе. Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

def task02():

    data = open('icecream.txt', encoding = 'utf-8')
    icecream = data.readlines()
    data.close()

    product_range = set(icecream[0].replace('\n', '').split(', '))
    stock = set(icecream[1].replace('\n', '').split(', '))

    print(f'Over: {product_range - stock}')     # или использовать difference

# task02()


# Задача 3. Выведите число π с заданной точностью. Точность вводится пользователем в виде натурального числа.
# 3 -> 3.142
# 5 -> 3.14159

def task03():

    accur = random.randint(1, 15)   # почему-то pi не выдает более 15 знаков после зпт
    print(f'Accuracy: {accur}\n{round(pi, accur)}')

# task03()
