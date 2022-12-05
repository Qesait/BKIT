import os
import math
import telebot
from dotenv import load_dotenv
import dbworker


load_dotenv()
TOKEN = os.environ.get('TOKEN')


def get_roots(a, b, c):
    result = []

    if a == 0.0:
        if b != 0.0:
            root = - c / b
            if root > 0:
                result.extend((math.sqrt(root), -math.sqrt(root)))
            if c == 0:
                result.append(0)
        return result

    D = b * b - 4 * a * c

    if c == 0:
        result.append(0)

    if D == 0.0:
        root = -b / (2.0 * a)
        if root > 0:
            result.extend((math.sqrt(root), -math.sqrt(root)))
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 > 0:
            result.extend((math.sqrt(root1), -math.sqrt(root1)))
        if root2 > 0:
            result.extend((math.sqrt(root2), -math.sqrt(root2)))
    return result


# Создание бота
bot = telebot.TeleBot(TOKEN)


# Начало диалога
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, 'Я биквадратные уравнения!')
    dbworker.set(dbworker.make_key(message.chat.id, dbworker.CURRENT_STATE),
                 dbworker.States.STATE_FIRST_COEFFICIENT.value)
    bot.send_message(message.chat.id, 'Введите первый коэффициент')


# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=['reset'])
def cmd_reset(message):
    bot.send_message(message.chat.id, 'Сбрасываем результаты предыдущего ввода.')
    dbworker.set(dbworker.make_key(message.chat.id, dbworker.CURRENT_STATE),
                 dbworker.States.STATE_FIRST_COEFFICIENT.value)
    bot.send_message(message.chat.id, 'Введите первый коэффициент')


# Обработка первого коэффициента
@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, dbworker.CURRENT_STATE)) == dbworker.States.STATE_FIRST_COEFFICIENT.value)
def first_num(message):
    text = message.text
    if not text.lstrip("-").isdigit():
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Пожалуйста введите число!')
        return
    else:
        bot.send_message(message.chat.id, f'Вы ввели первый коэффициент {text}')
        # Меняем текущее состояние
        dbworker.set(dbworker.make_key(message.chat.id, dbworker.CURRENT_STATE),
                     dbworker.States.STATE_SECOND_COEFFICIENT.value)
        # Сохраняем первое число
        dbworker.set(dbworker.make_key(message.chat.id, dbworker.States.STATE_FIRST_COEFFICIENT.value), text)
        bot.send_message(message.chat.id, 'Введите второй коэффициент')


# Обработка второго коэффициента
@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, dbworker.CURRENT_STATE)) == dbworker.States.STATE_SECOND_COEFFICIENT.value)
def second_num(message):
    text = message.text
    if not text.lstrip("-").isdigit():
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Пожалуйста введите число!')
        return
    else:
        bot.send_message(message.chat.id, f'Вы ввели второй коэффициент {text}')
        # Меняем текущее состояние
        dbworker.set(dbworker.make_key(message.chat.id, dbworker.CURRENT_STATE),
                     dbworker.States.STATE_THIRD_COEFFICIENT.value)
        # Сохраняем первое число
        dbworker.set(dbworker.make_key(message.chat.id, dbworker.States.STATE_SECOND_COEFFICIENT.value), text)
        bot.send_message(message.chat.id, 'Введите третий коэффициент')


# Обработка третьего коэффициента
@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, dbworker.CURRENT_STATE)) == dbworker.States.STATE_THIRD_COEFFICIENT.value)
def second_num(message):
    text = message.text
    if not text.lstrip("-").isdigit():
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Пожалуйста введите число!')
        return
    else:
        bot.send_message(message.chat.id, f'Вы ввели третий коэффициент {text}')

        a = float(dbworker.get(dbworker.make_key(message.chat.id, dbworker.States.STATE_FIRST_COEFFICIENT.value)))
        b = float(dbworker.get(dbworker.make_key(message.chat.id, dbworker.States.STATE_SECOND_COEFFICIENT.value)))
        c = float(text)

        roots = get_roots(a, b, c)
        result = 'Нет корней'
        match len(roots):
            case 1:
                result = 'Один корень:\n{}'.format(*roots)
            case 2:
                result = 'Два корня:\n{}\n{}'.format(*roots)
            case 4:
                result = 'Четыре корня:\n{}\n{}\n{}\n{}'.format(*roots)

        bot.send_message(message.chat.id, result)

        # Меняем текущее состояние
        dbworker.set(dbworker.make_key(message.chat.id, dbworker.CURRENT_STATE),
                     dbworker.States.STATE_FIRST_COEFFICIENT.value)
        # Выводим сообщение
        bot.send_message(message.chat.id, 'Введите первый коэффициент')


if __name__ == '__main__':
    bot.infinity_polling()