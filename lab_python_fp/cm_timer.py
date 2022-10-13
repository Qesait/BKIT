from time import perf_counter, sleep
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = perf_counter()

    def __exit__(self, exp_type, exp_value, traceback):
        print('time: {:.3f}'.format(perf_counter() - self.start))


@contextmanager
def cm_timer_2():
    start = perf_counter()
    yield
    print('time: {:.3f}'.format(perf_counter() - start))


if __name__ == '__main__':
    with cm_timer_1():
        sleep(1.5)
    with cm_timer_2():
        sleep(1.5)
