import os
import math
import telebot
from dotenv import load_dotenv
import dbworker


load_dotenv()
TOKEN = os.environ.get('TOKEN')


def get_roots(a, b, c):
    result = []

    # Частный случай квадратного уравнения
    if a == 0.0:
        if b != 0.0:
            root = - c / b
            if root > 0:
                result.extend((math.sqrt(root), -math.sqrt(root)))
            if c == 0:
                result.append(0)
        return result

    # Общий случай решения биквадратного уравнения
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


def calc_result(chat_id):
    # Загрузка коэффициентов из БД
    a = float(dbworker.get(dbworker.make_key(chat_id, dbworker.States.STATE_COEFFICIENT_A.value)))
    b = float(dbworker.get(dbworker.make_key(chat_id, dbworker.States.STATE_COEFFICIENT_B.value)))
    c = float(dbworker.get(dbworker.make_key(chat_id, dbworker.States.STATE_COEFFICIENT_C.value)))

    # Составить биквадратное уравнение
    result = 'Биквадратное уравнение: '
    if a:
        result += str(a).rstrip('0').rstrip('.') + 'x⁴'
    if b:
        if b > 0 and a:
            result += '+'
        result += str(b).rstrip('0').rstrip('.') + 'x²'
    if c:
        if c > 0 and (a or b):
            result += '+'
        result += str(c).rstrip('0').rstrip('.')
    elif not a and not b:
        result += '0'
    result += '=0\n'

    # Вычисление корней
    roots = get_roots(a, b, c)

    # Дописать решение
    match len(roots):
        case 0:
            result += 'Не имеет корней'
        case 1:
            result += 'Имеет один корень:\n{}'.format(*roots)
        case 2:
            result += 'Имеет два корня:\n{}\n{}'.format(*roots)
        case 3:
            result += 'Имеет три корня:\n{}\n{}\n{}'.format(*roots)
        case 4:
            result += 'Имеет четыре корня:\n{}\n{}\n{}\n{}'.format(*roots)

    return result


# Создание бота
bot = telebot.TeleBot(TOKEN)


# Начало диалога
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, 'Я решаю биквадратные уравнения!\nОни выглядят вот так: Ax⁴+Bx²+C=0')
    current_state = dbworker.States.STATE_COEFFICIENT_A
    dbworker.set(dbworker.make_key(message.chat.id, dbworker.CURRENT_STATE), current_state.value)
    bot.send_message(message.chat.id, f'Введите коэффициент {chr(current_state.value + 65)}')


# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=['reset'])
def cmd_reset(message):
    bot.send_message(message.chat.id, 'Сбрасываем результаты предыдущего ввода.')
    current_state = dbworker.States.STATE_COEFFICIENT_A
    dbworker.set(dbworker.make_key(message.chat.id, dbworker.CURRENT_STATE), current_state.value)
    bot.send_message(message.chat.id, f'Введите коэффициент {chr(current_state.value + 65)}')


# Считывание коэффициента
@bot.message_handler()
def coefficient(message):
    # Получаем текущее состояние
    current_state = dbworker.States(int(dbworker.get(dbworker.make_key(message.chat.id, dbworker.CURRENT_STATE))))

    text = message.text
    if not text.lstrip("-").isdigit():
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Пожалуйста введите число!')
        return

    # Сохраняем полученное значение
    # bot.send_message(message.chat.id, f'Вы ввели коэффициент {chr(current_state.value + 65)}')
    dbworker.set(dbworker.make_key(message.chat.id, current_state.value), text)

    # Если есть все три коэффициента, то решаем биквадратное уравнение
    try:
        current_state = next(current_state)
    except StopIteration:
        bot.send_message(message.chat.id, calc_result(message.chat.id))
        current_state = dbworker.States.STATE_COEFFICIENT_A

    # Переходим к следующему состоянию
    dbworker.set(dbworker.make_key(message.chat.id, dbworker.CURRENT_STATE), current_state.value)
    bot.send_message(message.chat.id, f'Введите коэффициент {chr(current_state.value + 65)}')


if __name__ == '__main__':
    bot.infinity_polling()
