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


if __name__ == '__main__':
    a = list(islice(lucky_numbers(), 10))
    print(' '.join(map(str, a)))
