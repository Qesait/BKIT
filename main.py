import os
import telebot
from dotenv import load_dotenv
import dbworker
from equation_solving import calc_result


load_dotenv()
TOKEN = os.environ.get('TOKEN')


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
        a = float(dbworker.get(dbworker.make_key(message.chat.id, dbworker.States.STATE_COEFFICIENT_A.value)))
        b = float(dbworker.get(dbworker.make_key(message.chat.id, dbworker.States.STATE_COEFFICIENT_B.value)))
        c = float(text)
        bot.send_message(message.chat.id, calc_result(a, b, c))
        current_state = dbworker.States.STATE_COEFFICIENT_A

    # Переходим к следующему состоянию
    dbworker.set(dbworker.make_key(message.chat.id, dbworker.CURRENT_STATE), current_state.value)
    bot.send_message(message.chat.id, f'Введите коэффициент {chr(current_state.value + 65)}')


if __name__ == '__main__':
    bot.infinity_polling()
