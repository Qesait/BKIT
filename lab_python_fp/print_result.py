def print_result(func):
    original_func = func

    def new_func(*args, **kwargs):
        print(original_func.__name__)
        result = original_func(*args, **kwargs)
        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, item in result.items():
                print(f'{key} = {item}')
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


@print_result
def double_int(x):
    return x * 2


@print_result
def multiply_list(l, k=2):
    return l * k


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
    double_int(5)
    multiply_list([1, 2], k=3)
