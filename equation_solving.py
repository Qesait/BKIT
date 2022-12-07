import math


def get_roots(a, b, c):
    result = []

    # Частный случай квадратного уравнения
    if a == 0.0:
        if b != 0.0:
            root = - c / b
            if root > 0:
                result.extend((math.sqrt(root), -math.sqrt(root)))
            if c == 0:
                result.append(0)
        return result

    # Общий случай решения биквадратного уравнения
    D = b * b - 4 * a * c

    if c == 0:
        result.append(0)

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


def calc_result(a, b, c):
    # Составить биквадратное уравнение
    result = 'Биквадратное уравнение: '
    if a:
        result += str(a).rstrip('0').rstrip('.') + 'x⁴'
    if b:
        if b > 0 and a:
            result += '+'
        result += str(b).rstrip('0').rstrip('.') + 'x²'
    if c:
        if c > 0 and (a or b):
            result += '+'
        result += str(c).rstrip('0').rstrip('.')
    elif not a and not b:
        result += '0'
    result += '=0\n'

    # Вычисление корней
    roots = get_roots(a, b, c)

    # Дописать решение
    match len(roots):
        case 0:
            result += 'Не имеет корней'
        case 1:
            result += 'Имеет один корень:\n{}'.format(*roots)
        case 2:
            result += 'Имеет два корня:\n{}\n{}'.format(*roots)
        case 3:
            result += 'Имеет три корня:\n{}\n{}\n{}'.format(*roots)
        case 4:
            result += 'Имеет четыре корня:\n{}\n{}\n{}\n{}'.format(*roots)

    return result
