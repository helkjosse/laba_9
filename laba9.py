import random
import logging

# Настройка логгинга
logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)

# Создать файл лога с utf-8 кодировкой
file_handler = logging.FileHandler("log.log", encoding='utf-8')

# Создать форматтер, отображающий дату, время, имя регистратора, уровень и сообщение
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавить обработчик к логгеру
logger.addHandler(file_handler)

def main():
    # Попросите пользователя ввести максимальное число и количество попыток
    n = int(input("Введите максимальное количество: "))
    k = int(input("Введите количество попыток: "))

    # Сгенерировать случайное число от 1 до N
    number = random.randint(1, n)
    logger.info(f"Сгенерированное число: {number}")
    file_handler.flush()

    # Пусть пользователь угадает число
    for i in range(k):
        guess = int(input("Введите свое предположение: "))
        logger.info(f"Попытка {i+1}: {guess}")
        file_handler.flush()
        if guess == number:
            print("Вы угадали!")
            logger.info("Угадал!")
            file_handler.flush()
            break
        elif guess < number:
            print("Число должно быть больше.")
            logger.info("Число должно быть больше.")
            file_handler.flush()
        else:
            print("Число должно быть меньше.")
            logger.info("Число должно быть меньше.")
            file_handler.flush()
    else:
        print("Попыток больше нет.")
        logger.info("Попыток больше нет.")
        file_handler.flush()

if __name__ == "__main__":
    main()
