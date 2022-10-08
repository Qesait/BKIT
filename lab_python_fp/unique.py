class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.iter = iter(items)
        self.used = set()

    def __next__(self):
        for current in self.iter:
            if self.ignore_case:
                try:
                    current = current.lower()
                except AttributeError:
                    pass
            if current not in self.used:
                self.used.add(current)
                return current
        raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    data = [
        [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
        range(1, 10),
        ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    ]
    for one in data:
        print(list(Unique(one)))
    for one in data:
        print(list(Unique(one, ignore_case=True)))
