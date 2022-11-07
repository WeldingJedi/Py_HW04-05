import random

def range_generation(v, w, x, y):
    array = [random.randint(x, y) for _ in range(random.randint(v, w))]
    return array

def ascending_check(array):
    size = len(array)
    for i in range(size):
        result = []
        result.append(array[i])
        flag = i
        ind = flag + 1
        while ind < size:
            if array[flag] < array[ind] and array[ind] > result[-1]:
                result.append(array[ind])
            ind += 1
        if len(result) > 1: print(result)

def unique_elements(array):
    unique = []
    for number in array:
        if number not in unique:
            unique.append(number)
    return unique

def repeating_elements(array):
    counter = {}
    for elem in array:
        counter[elem] = counter.get(elem, 0) + 1
    repeats = {element: count for element, count in counter.items() if count > 1}
    return repeats


# Задача 1. Задайте список случайных чисел от 1 до 10, 
# выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

def task01():

    numbers = range_generation(3, 20, 1, 10)
    print(f'Genered range:\n{numbers}')
    result = lambda x: x > 5
    result = list(filter(result, numbers))
    print(f'Sorted range:\n{result}')

# task01()


# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

def task02():
    
    numbers = range_generation(5, 10, 1, 9)
    print(f'Genered range:\n{numbers}')
    print(f'Ascending range(s):')
    ascending_check(numbers)

task02()    


# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, 
# сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

def task03():

    numbers = range_generation(5, 12, 1, 10)
    print(f'Generated range:\n{numbers}')
    unique_list = unique_elements(numbers)
    repeats_dict = repeating_elements(numbers)
    print(f'Repeated num: repeat times:\n{repeats_dict}')
    print(f'Unique range:\n{unique_list}')

# task03()
