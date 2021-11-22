# Задание 1
# name = input("Введите ваше имя")
# age = int(input("Введите ваш возраст"))

# print(f"Здравствуйте, {name}. Вам {age}")

# Задание 2
# time = int(input("Укажите время в секундах"))
# hours = time // 3600
# minutes = (time - hours * 3600) // 60
# seconds = time - (hours * 3600 + minutes * 60)
# print(f"Время сейчас {hours} {minutes} {seconds}")

# Задание 3
# number = int(input("Введите число"))
# numb = str(number)
# pos1 = numb + numb
# pos2 = numb + numb + numb
# result = number + int(pos1) + int(pos2)
# print(f"Ваш результат равен {result}")

# Задание 4
#number = int(input("Введите целое положительное число"))
#num = number % 10
#number = number // 10
#while number > 0:
#    if number % 10 > num:
#        num = number % 10
#        number = number // 10
#    if number > 9:
#        continue
#    else:
#        print(f"Самая большая цифра в Вашем числе {num}")
#        break

# Задание 5
#income = float(input("Введите выручку фирмы"))
#costs = float(input("Введите издержки фирмы"))
#if income > costs:
#    print(f"Фиорма работает с прибылью. Рентабельность выручки составляет {income / costs}")
#    worker = int(input("Введите количество сотрудников"))
#    print(f"Прибыль в расчкете на одного сотрудника составляет {income / worker}")
#else:
#    print("Фирма работает в убыток")

# Задание 6
a = int(input("Введите результат пробежки в км"))
b = int(input("Введите желаемый результат"))
day = 1
while a < day:
    day += 1
    a += a * .10
else:
    print(f"Вы достигнете желаемого показателя на {day} день")