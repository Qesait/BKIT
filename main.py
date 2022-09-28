import sys
import math


def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        coef_str = input(prompt)

    while True:
        try:
            coef = float(coef_str)
            break
        except:
            print('Неверное значение, повторите попытку')
            coef_str = input(prompt)

    return coef


def get_roots(a, b, c):
    result = []

    if a == 0.0:
        if b != 0.0:
            root = - c / b
            if root > 0:
                result.extend((math.sqrt(root), -math.sqrt(root)))
        return result

    D = b * b - 4 * a * c

    if D == 0.0:
        root = -b / (2.0 * a)
        if root > 0:
            result.extend((math.sqrt(root), -math.sqrt(root)))
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 > 0:
            result.extend((math.sqrt(root1), -math.sqrt(root1)))
        if root2 > 0:
            result.extend((math.sqrt(root2), -math.sqrt(root2)))
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А: ')
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')
    roots = get_roots(a, b, c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(*roots))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {}, {}'.format(*roots))


if __name__ == "__main__":
    main()