# import turtle
#
# height = input('Введите ваш рост')
# print(height)
#
# color = input('Введите ваш любый цвет')
# print(color)
#
# a = 1
# b = 2
# c = 3
# b = 2 + a
# a = b * 4
# b = a / 3.14
# a = 8 - b
# print(a, ',' , b)
#
# total = 10 + 14
# print(total)
#
# down_payment = 3
# total = 4
# due = total + down_payment
# print(due)
#
# subtotal = 2
# total =  subtotal * 0.15
# print(total)
#
# sales = 3.145124123
# print(f"{sales:.2f}")
#
# number = 1234567.456
# print(f'{number:,.1f}')
#
# print('Джордж', 'Джон', 'Пол', 'Ринго', sep='@')
#
# "Нарисовать квадрат с синей заливкой, ширина стороны = 100"
# turtle.begin_fill()
# turtle.fillcolor('blue')
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.hideturtle()
# turtle.end_fill()
#
# "Нарисовать круг с красной заливкой, радиус = 75"
# turtle.begin_fill()
# turtle.circle(75)
# turtle.hideturtle()
# turtle.fillcolor('red')
# turtle.end_fill()
#
# age=int(input("Сколько тебе лет:"))
# if age > 18:
#     print("Ты взрослый")
# else:
#     if age == 18:
#         print("Тебе 18")
#     else:
#         if age<18:
#             print("Ты еще мал")
#
# # Если условие выполнено, то вывести наибольшую переменную
# context_a = int(input("Введите первое число: "))
# context_b = int(input("Введите второе число: "))
# if context_a > 10 and context_b < 100:
#     if context_a >context_b:
#         print("Наобольшее число: ", context_a)
#     else:
#         print("Наобольшее число: ", context_b)
# else:
#     print("Ваше число вне диапазона")
#
# # Исполнение цикла с словием повторения и вывод информации
# speed = int(input("Enter the speed: "))
# while speed > 0:
#     if speed >= 26 and speed <= 56:
#         print("Скорость нормальная")
#     elif speed < 26:
#         print("Скорость минимальна")
#     else:
#         print("Скорость аварийная")
#     speed = int(input("Введите скорость : "))
#
# # Исполнение цикла с условием повторения и вывод информации
# for speed in range (25, 58, 10):
#     if speed >= 26 and speed <= 56:
#         print("Скорость нормальная")
#     elif speed < 26:
#         print("Скорость минимальна")
#     else:
#         print("Скорость аварийная")
#
# # Определение допустимого интервала
# points = int(input('Введите значение: '))
# while points > 0:
#     if not (points >= 9 and points <=51):
#         print('Недопустимые точки')
#     else:
#         print('Допустимые точки')
#     points= int(input())
# # Вывод дня недели по числу
# Monday = "Понедельник"
# Tuesday = "Вторник"
# Wednesday = "Среда"
# Thursday = "Четверг"
# Friday= "Пятница"
# Saturday = "Суббота"
# Sunday = "Воскресенье"
# days = int(input("Введите число от 1 до 7: "))
# if days == 1:
#     print(Monday)
# elif days == 2:
#     print(Tuesday)
# elif days == 3:
#     print(Wednesday)
# elif days == 4:
#     print(Thursday)
# elif days == 5:
#     print(Friday)
# elif days == 6:
#     print(Saturday)
# elif days == 7:
#     print(Sunday)
# else:
#     print("Ошибка, число вне диапазона")
#
# # Определение площади прямоугольников и вывод сравнения
# length_a= int(input("Enter the length of A: "))
# width_a= int(input("Enter the width of A: "))
# width_b= int(input("Enter the width of B: "))
# length_b= int(input("Enter the length of B: "))
# s_a = length_a*width_a
# s_b = length_b*width_b
# if s_a > s_b:
#     print("Наибольшая площадь у прямоугольника 'A', составляет = ", s_a)
# elif s_a == s_b:
#     print("Площадь прямоугольников одинакова")
# else:
#     print("Наибольшая площадь у прямоугольника 'B', составляет = ", s_b)
#
# # Цикл с предусловием
# product = int(input("Enter product number: "))
# while product < 100000:
#     product = product * 10
#     print("Результат = ", product)
#
#  # Цикл с условием ввода
# solution = "Да"
# while solution == "Да":
#     num_one = int(input("Enter the number of one: "))
#     num_two = int(input("Enter the number of two: "))
#     print("The result is: ", num_one + num_two)
#     solution = input("Желаете попробовать еще раз?\nВведите 'Да' если хотите продолжить: ")
#
#  # Цикл с счетчиком
# for number in range(1001):
#     print(number)
#
#  # Цикл с нарастающим итогом
# total = 0.0
# for counter in range (10):
#     number = int(input("Введите число: "))
#     total += number
# print(total)
#
# # Цикл числового ряда
# total = 0.0
# for numerator in range (1, 31):
#     denominator = 31- numerator
#     total += numerator / denominator
# print("Сумма ряда:", total)
#
# # Цикл строк с символами
# for str in range(10):
#     for simbol in range(15):
#         print("#", end="")
#     print()
#
# # Цикл проверки валидации
# retry = "Da"
# while retry == "Da":
#     val = int(input("Введите положительное ненулевое число: "))
#     while val <=0:
#         print("Ошибка валидации.")
#         val=int(input("Попробуем еще раз: "))
#     print("Число подходит")
#     retry = input("Повторим?\nВведите 'Da' если готовы: ")
# script = 15
# def first_funcshion (name):
#     sssr= script+10
#     print(sssr)
# first_funcshion(script)
#
#
# # Рассчитать отпускную цену товара
#
# SUM_SALES = 0.30  # Объявить глобальную переменную с суммой скидки
# sums = 'Да'  # Предусловие цикла
# while sums == 'Да' or 'ДА':
#     def main():
#         user_sum = start_sum()  # Получить сумму от юзера
#         sales_sum = user_sum - sum_sales(user_sum)  # Рассчитать сумму скидки
#         print(f"Ваша отпускная цена составляет: ${sales_sum:.2f}")  # Показать результат
#
#
#     def start_sum():
#         return float(input("Enter sum of sales: "))
#
#
#     def sum_sales(sales):
#         return sales * SUM_SALES
#
#
#     main()
#     sums = input("Необходимо провести расчеты еще раз?\nВведите 'Да' если хотите продолжить: ")
#
# list1 = [1, 12, 2, 20, 3, 15, 4]
# list2 = [n for n in list1 if n>10]
#
# print(list2)
#
# list1 = [1, 12, 2, 20, 3, 15, 4]
# list2= [n*2 for n in list1]
#
# print(list2)
#
# name = 'Test'
# all = 0
# for x in name:
#     print(f'Символ {x} имеет индекс {all}')
#     all+=1
#
# x = 'lorenipsumhowmuch'
# print(len(x))
# print(x[2])

for i in range(5):
    print(i)