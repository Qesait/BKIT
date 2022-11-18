def print_result(func):
    original_func = func

    def new_func(*args, **kwargs):
        print(original_func.__name__)
        result = original_func(*args, **kwargs)
        if isinstance(result, dict):
            for key, item in result.items():
                print(f'{key} = {item}')
        elif isinstance(result, list):
            for item in result:
                print(item)
        else:
            print(result)
        return result
    return new_func


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
