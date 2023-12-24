# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток. Программа должна
# подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

attempts = 0
while attempts < MAX_ATTEMPTS:
    guess = int(input("Угадайте число от 0 до 1000: "))
    attempts += 1

    if guess == num:
        print("Поздравляю, вы угадали число!")
        break
    elif guess < num:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")
else:
    print(f"К сожалению, вы исчерпали все попытки. Загаданное число было {num}")