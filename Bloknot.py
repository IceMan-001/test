# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")

'''Пример написания меню'''

MENU_figure = "Сделайте выбор:\
    \n  1 Верхний и правый треугольники;\
    \n  2 Левый и нижний треугольники;\
    \n  3 Верхний треугольник;\
    \n  4 Нижний треугольник;\
    \n  5 Верхний и нижний треугольники;\
    \n  6 Левый и правый треугольники;\
    \n  8 Правый треугольник;\
    \n  9 Верхний и левый треугольники;\
    \n  10 Правый и нижний треугольники;"
print(MENU_figure)        



'''Вариант проверок'''
# import logging

# logging.basicConfig(filename="error.log", filemode="a", level=logging.INFO)
# logging.info("Created")

# user_input = input("Число: ")

# try:
#     value = int(user_input)
# except ValueError as error:
#     value = int(user_input.strip("\t ,"))
#     logging.error(error)
#     print("Incorrect value")
# except ZeroDivisionError:
#     print("Divizion by zero")
# except (TypeError, AttributeError):
#     print()
# except Exception:
#     pass

# result = 1 / value
# print(result)

# except BaseException:
#     print("Smth went wrong")
#     raise

# print("jjhgjhg")

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops! That was no valid number. Try again...")


'''Основные методы строк тип "str" '''
'''объект.метод(аргументы)'''
# s = 'Pyhton'
# s.upper()  # делает все символы заглавными
# print(s.upper())  # PYHTON
# s.lower()  # делает все элементы строчными
# print(s.lower())  # pyhton
# msg = 'abracadabra'
# msg.count('ra')  # количество вхождения элемента (подстроки)
# print(msg.count('ra')) # 2
# msg.count('ra', 4, 10) # элемент, индексы начала и конца поска вхождения 10 не включительно
# # ищет слева на право
# msg.find('br', 1, 10) # первое вхождение подстроки в элемент. Если не находит, то возвращает - 1
# # ищет справо на лево
# msg.rfind('br', 2)
# msg.index('br') # Индекс вхождения подстроки
# msg.replace('a', 'o') # Заменить все а на о
# msg.replace('ab', 'AB') # Заменить все ab на AB
# msg.replace('ab', '', 2) # Удалить все ab и заменить пустой строкой, 2 - максимальное количество замен
# msg.isalpha()  # Проверяет если все буквы => True, иначе => False
# msg.isdigit()  # Прверяет если все цифра => True, иначе => False
# d = 'abc'
# d.rjust(5)  # '  abc' вернулась строка и два заполнителя до 5
# d = 12
# d.rjust(4, '0')  # '0012'  12 и два нуля в заполнение
# d.ljust(10, '*')  # '12********'
# 'Иванов Иван Иванивич'.split('')  # разделитель ['Иванов', 'Иван', 'Иванович']
# digs = '1,  2,   3,4,5,6'
# digs.replace(' ', '').split(',')  # ['1', '2', '3', '4', '5', '6']
# d = ['1', '2', '3', '4', '5', '6']
# ', '.join(d)  # '1, 2, 3, 4, 5, 6'  через запятую и пробел строка


# import re
# user_number = '25+15'
# n = re.split(r'[/*+-]', user_number)
# n1 = int(n[0])
# n2 = int(n[1])
# print(n, n1, n2)

def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)
                # 0001               , 2 

arr = [0, 1, 0, 1]
print(binary_array_to_number(arr))

# (0 * 2**3) + (0 * 2**2) + (0 * 2**1) + (1 * 2**0) = 0 + 0 + 0 + 1 = 1

_n = map(str, arr)  # <map object at 0x0000014D683A5B70>
print(_n)
_n = list(map(str, arr))  # ['0', '0', '0', '1']
print(_n)
print(type(_n))  # <class 'list'>
_n = "".join(map(str, arr))  # 0001
print(_n)
print(type(_n))  # <class 'str'>
_n = int(_n)  # 1
print(_n)

z = int('101', 2)
print(z)

print(int("0xf", base = 16))
# => 15
print(int("0o11", base = 8))
# => 9
print(int("0b101", base = 2))
# => 5


