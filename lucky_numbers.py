from itertools import count, islice


def lucky_numbers():
    """
    Генератор счастливых чисел\n
    https://oeis.org/A000959
    """
    yield 1
    sequence = []
    for i in count(3, 2):
        for divider in sequence:
            divider[1] += 1
            if divider[1] % divider[0] == 0:
                break
        else:
            yield i
            sequence.append([i, len(sequence) + 2])
