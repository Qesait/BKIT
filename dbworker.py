from enum import Enum
from vedis import Vedis


# Файл базы данных Vedis
db_file = "db.vdb"
# Ключ записи в БД для текущего состояния
CURRENT_STATE = "CURRENT_STATE"


class States(Enum):
    """Состояния автомата"""
    STATE_COEFFICIENT_A = 0
    STATE_COEFFICIENT_B = 1
    STATE_COEFFICIENT_C = 2

    def __next__(self):
        try:
            return States(self.value + 1)
        except ValueError:
            raise StopIteration


def get(key):
    """Чтение значения"""
    with Vedis(db_file) as db:
        try:
            return db[key].decode()
        except KeyError:
            # в случае ошибки значение по умолчанию - начало диалога
            return States(0)


def set(key, value):
    """Запись значения"""
    with Vedis(db_file) as db:
        try:
            db[key] = value
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False


def make_key(chatid, keyid):
    """Создание ключа для записи и чтения"""
    res = str(chatid) + '__' + str(keyid)
    return res
