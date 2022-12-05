from vedis import Vedis
from enum import Enum


# Файл базы данных Vedis
db_file = "db.vdb"
# Ключ записи в БД для текущего состояния
CURRENT_STATE = "CURRENT_STATE"


# Состояния автомата
class States(Enum):
    STATE_START = "STATE_START"  # Начало нового диалога
    STATE_FIRST_COEFFICIENT = "STATE_FIRST_COEFFICIENT"
    STATE_SECOND_COEFFICIENT = "STATE_SECOND_COEFFICIENT"
    STATE_THIRD_COEFFICIENT = "STATE_THIRD_COEFFICIENT"


# Чтение значения
def get(key):
    with Vedis(db_file) as db:
        try:
            return db[key].decode()
        except KeyError:
            # в случае ошибки значение по умолчанию - начало диалога
            return States.S_START.value


# Запись значения
def set(key, value):
    with Vedis(db_file) as db:
        try:
            db[key] = value
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False


# Создание ключа для записи и чтения
def make_key(chatid, keyid):
    res = str(chatid) + '__' + str(keyid)
    return res
