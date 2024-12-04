def discriminant(a, b, c):
    result = b ** 2 - 4 * a * c
    return result

def solution(a, b, c):
    discr = discriminant(a, b, c)
    if discr > 0:
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a)
        return f"{x1} {x2}"
    elif discr < 0:
        return "корней нет"
    else:
        x = (-b + discr ** 0.5) / (2 * a)
        return x

if __name__ == '__main__':
    # solution(1, 8, 15)
    # solution(1, -13, 12)
    # solution(-4, 28, -49)
    # solution(1, 1, 1)
    # solution(None, None, None)
    try:
        check = discriminant('one','eight','fifteen')
    except TypeError:
        print('нет проверки на входные данные')