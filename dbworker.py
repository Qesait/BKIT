from vedis import Vedis
from enum import Enum


# Файл базы данных Vedis
db_file = "db.vdb"
# Ключ записи в БД для текущего состояния
CURRENT_STATE = "CURRENT_STATE"


# Состояния автомата
class States(Enum):  # Начало нового диалога
    STATE_COEFFICIENT_A = 0
    STATE_COEFFICIENT_B = 1
    STATE_COEFFICIENT_C = 2

    def __next__(self):
        try:
            return States(self.value + 1)
        except ValueError:
            raise StopIteration


# Чтение значения
def get(key):
    with Vedis(db_file) as db:
        try:
            return db[key].decode()
        except KeyError:
            # в случае ошибки значение по умолчанию - начало диалога
            return States.next_state()


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







if __name__ == '__main__':
    s = States.STATE_COEFFICIENT_A
    print(s)
    s = next(s)
    print(s)
    print(chr(s.value + 65))
    s2 = States(s.value)
    print(s2)
