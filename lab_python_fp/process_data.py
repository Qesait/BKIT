import json
import sys
from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1


path = r'C:\Users\kuzva\PycharmProjects\BKIT\data_light.json'


with open(path, encoding='UTF-8') as f:
    data = json.load(f)


# @print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True), key=lambda s: s.lower())


# @print_result
def f2(arg):
    return list(filter(lambda s: s[:11].lower() == 'программист', arg))


# @print_result
def f3(arg):
    return list(map(lambda s: s + 'с опытом Python', arg))


@print_result
def f4(arg):
    return [f'{prof}, зарплата {salary} руб' for prof, salary in zip(arg, gen_random(len(arg), 100000, 200000))]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
