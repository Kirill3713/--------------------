# Импортируем нужные модули и создаем переменные цветов
import colorama
red = colorama.Fore.LIGHTRED_EX
reset = colorama.Fore.RESET
cyan = colorama.Fore.CYAN
blue = colorama.Fore.BLUE
white = colorama.Fore.WHITE
light_white = colorama.Fore.LIGHTWHITE_EX
# Определяем функцию
def find_root(n:int) -> int:
    """
    Функция для нахождения арифметического квадратного корня целого числа.
    """
    # Объявляем переменную x
    x = 1
    # Получаем информацию о квадрате, который необходимо найти
    try:
        n = int(n)
    # Добавляем исключение, на случай неправильного ввода
    except ValueError:
        return red + "Введено некорректное значение!" + reset
    while x < 10001:
        # Проверяем: это тот квадрат, который нам нужен, или нет
        if x ** 2 == n:
            return light_white + "Число  найдено." + reset
        # Прибавляем к x единицу
        x += 1
    # Если n - не квадрат числа
    else:
        return white + "Число не найдено. Такого квадрата в пределах миллиона нет." + reset

# Объявляем переменную x
x = 1
# Получаем информацию о квадрате, который необходимо найти
try:
    n = int(input(cyan + "Введите число, которое хотите найти: " + blue))
# Добавляем исключение, на случай неправильного ввода
except ValueError:
    print(red + "Введено некорректное значение!" + reset)
    quit()
while x < 10001:
    # Тренировка (просто чтоб знать, что так тоже можно))
    if x ** 2 % 100 == 0:
        print(cyan + "Пропуск(", f"{x}² = {x ** 2} "")" + reset)
        # Проверяем: это тот квадрат, который нам нужен, или нет
        if x ** 2 == n:
            print(light_white + "Число  найдено." + reset)
            break
        x += 1
        continue
    # Выводим число и его квадрат
    print(blue + f"{x}² = {x ** 2}" + reset)
    # Проверяем: это тот квадрат, который нам нужен, или нет
    if x ** 2 == n:
        print(light_white + "Число  найдено." + reset)
        break
    # Прибавляем к x единицу
    x += 1
# Если n - не квадрат числа
else:
    print(white + "Число не найдено. Такого квадрата в пределах миллиона нет." + reset)