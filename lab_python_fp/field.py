def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for item in items:
            value = item.get(args[0])
            if value is not None:
                yield value
        return
    for item in items:
        selected = {}
        for key in args:
            value = item.get(key)
            if value is not None:
                selected[key] = value
        yield selected


if __name__ == '__main__':
    pass
