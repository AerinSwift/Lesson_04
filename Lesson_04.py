# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# """Закомментировал, т.к. без запуска из терминала скрипт кладет отладку"""
# from sys import argv
#
# lesson_04, work_hours, bucks_per_hour, bonus = argv
#
# """Конвертируем строку, полученную из терминала, в число"""
# work_hours_int = int(argv[1])
# bucks_per_hour_int = int(argv[2])
# bonus_int = int(argv[3])
#
# print("Имя скрипта: ", lesson_04)
# print("Параметр 1, выработка в часах: ", work_hours_int)
# print("Параметр 2, часовая ставка: ", bucks_per_hour_int)
# print("Параметр 3, премия: ", bonus_int)
# print("Заработная плата: ", work_hours_int * bucks_per_hour_int + bonus_int)

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print("Исходный список: ", original_list)
"""Не понял, как использовать индексы (и можно ли вообще) в генераторе, потому нашел костыль с enumerate"""
new_list = [num for i, num in enumerate(original_list) if i > 0 and original_list[i] > original_list[i - 1]]
print("Список элементов исходного списка, значение которых больше предыдущего элемента: ", new_list)

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

list_of_20_21 = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print("Числа, кратные 20 и 21, в пределах от 20 до 240: ", list_of_20_21)

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

# Как не пытался, не удалось полностью решить задачу.
orig_numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
used_numbers = []
unique_numbers = []
ind = 0
for el in orig_numbers:
    temp = orig_numbers.pop(ind)
    used_numbers.append(temp)
    ind = ind + 1
    if temp in orig_numbers:
        continue
    else:
        unique_numbers.append(temp)

print("Изначальный массив чисел: ", orig_numbers)
print("Не имеющий повторений числа массива:", unique_numbers)


# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce
even_numbers = [el for el in range(100, 1001) if el % 2 == 0]
result_multiply = reduce((lambda x, y: x * y), even_numbers)
print("Произведение всех четных чисел от 100 до 1000: ", result_multiply)

# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle
start_number = int(input("Введите стартовое число. Будут сгенерированы целые числа, от указанного числа до 10"))
iter_list = []
for el in count(start_number):
    if el > 10:
        break
    else:
        iter_list.append(el)
        print(el)
print("Эти числа были записаны в список. "
      "С помощью функции cycle() программа циклично выведет их определенное число раз.")
print("Список сгенерированных чисел: ", iter_list)
cycle_count = int(input("Сколько раз вывести элементы списка?"))
counter = 0

for el in cycle(iter_list):
    if counter == cycle_count:
        break
    print(el)
    counter += 1

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(fact_num):
    temporal = 1
    for i in range(1, fact_num + 1):
        temporal *= i
        yield temporal


fact_num = int(input("Укажите факториал какого числа Вы хотели бы узнать?\n"))
for el in fact(fact_num):
    print(el)

