#
# ************************************************* Домашнее задание ************************************************* #
# # ********************************* ( "Цели и задачи. Поток выполнения программы" )********************************* #
# Цель: применить навыки создания условных конструкций и знания операторов if, else, elif / and, or, not.
#
#
# Задача №1: "Все ли равны?":
# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else),
# которая выводит кол-во одинаковых чисел среди 3-х введённых.

# Пункты задачи:
#
#     Если все числа равны между собой, то вывести 3
#     Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
#     Если равных чисел среди 3-х вообще нет, то вывести 0
#
#     Помните, что условная конструкция начинается с if.
#     Операторы elif и else не могут существовать самостоятельно, они являются продолжением условной конструкции.
#     Старайтесь избегать вложенности условий и описывать их, используя операторы or, and и not.
#     Самое хорошее решение не только самое быстрое, но ещё и хорошо читаемое!

# -------------------------------------------------------------------------------------------------------------------- #
# Ответ №1
# входные данные
from time import sleep
first = int(input("Введите первое число. - "))
sleep(1)
second = int(input("Введите второе число.. - "))
sleep(1)
third = int(input("Введите третье число... - "))
if first == second and first == third:   # Для создания условия используем оператора if, после которого само условие
    sleep(2)
    print("Все три числа равны, хорошая работа!!! *** ")
elif first == second or first == third or second == third:  # elif # чтобы при выполнении одного из условий
    # компьютер не проверял остальные.
    sleep(2)
    print("Всего числа равны между собой. Еще разок ? **")
else:
    sleep(2)
    print("Нет равных между собой чисел. Попробуем еще ? *")
# -------------------------------------------------------------------------------------------------------------------- #
# D:\Программы\ProjectPyton\BasiesStructures\Scripts\python.exe "D:\Программы\ProjectPyton\
# Module 2 Basic Operators\Conditional construction. Operators (Homework).py"
# Введите первое число. - 1
# Введите второе число.. - 2
# Введите третье число... - 3
# Нет равных между собой чисел. Попробуем еще ? *
#
# Process finished with exit code 0
# -------------------------------------------------------------------------------------------------------------------- #
# D:\Программы\ProjectPyton\BasiesStructures\Scripts\python.exe "D:\Программы\ProjectPyton\
# Module 2 Basic Operators\Conditional construction. Operators (Homework).py"
# Введите первое число. - 1
# Введите второе число.. - 1
# Введите третье число... - 2
# Всего числа равны между собой. Еще разок ? **
#
# Process finished with exit code 0
# -------------------------------------------------------------------------------------------------------------------- #
# D:\Программы\ProjectPyton\BasiesStructures\Scripts\python.exe "D:\Программы\ProjectPyton\
# Module 2 Basic Operators\Conditional construction. Operators (Homework).py"
# Введите первое число. - 1
# Введите второе число.. - 1
# Введите третье число... - 1
# Все три числа равны, хорошая работа!!! ***
#
# Process finished with exit code 0
# -------------------------------------------------------------------------------------------------------------------- #
