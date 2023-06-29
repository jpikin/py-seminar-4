# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

from random import randint

def set_create(x):
    new_set = {randint(1,10) for _ in range(x)}
    print(f'Множество {new_set}')
    return new_set

n, m = int(input("Введите размер первого множества ")), int(input("Введите размер второго множества "))

sorted_lst = sorted(set_create(n) & set_create(m))
if len(sorted_lst) > 0:
    print("Общие элементы множеств:", end=' ')
    print(*sorted_lst)
else: print("Общих элементов не найдено")







# Вариант 2:

# def set_create(x):
#     return {int(input()) for _ in range(x)}

# n, m = int(input()), int(input())
# print(*sorted(set_create(n) & set_create(m)))

