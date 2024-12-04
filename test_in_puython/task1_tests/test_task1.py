import pytest

from task1_tests.task1 import discriminant, solution


@pytest.mark.parametrize(
    'a,b,c,result',
    (
            (1, 8, 15, 4),
            (1, -13, 12, 121),
            (-4, 28, -49, 0),
            (1, 1, 1, -3),
            (-2,-3,-4, -23),
            (2.4, 5.6, -7.8, 106.24)
    )
)
def test_discriminant(a,b,c,result):
    check = discriminant(a, b, c)
    assert check == result


def test_zero_discriminant():
    a = 0
    b = 0
    c = 0
    check = discriminant(a, b, c)
    assert isinstance(check, str), 'нет проверки на существование уравнения и деления на 0'


@pytest.mark.parametrize(
    'a,b,c',
    (
            ('one','eight','fifteen'),
            (None, None, None),
            ('four', 28, -49),
            (1, -13, 12)

    )
)
def test_invalid_args_discriminant(a,b,c):
    check = None
    try:
        check = discriminant(a, b, c)
    except TypeError:
        assert isinstance(check, str), 'нет проверки на входные данные'


@pytest.mark.parametrize(
    'a,b,c,result',
    (
            (1, 8, 15, '-3.0 -5.0'),
            (1, -13, 12, '12.0 1.0'),
            (1, 1.5, -13.5, '3.0 -4.5')
    )
)
def test_solution(a,b,c,result):
    check = solution(a, b, c)
    assert check == result


@pytest.mark.parametrize(
    'a,b,c,result',
    (
            (1, 1, 1, 'корней нет'),
            (-2,-3,-4, 'корней нет')
    )
)
def test_not_answer_solution(a,b,c,result):
    check = solution(a, b, c)
    assert check == result


@pytest.mark.xfail
def test_one_answer_solution(a,b,c,result):
    a = 0
    b = 0
    c = 0
    result = '3.5 3.5'
    check = solution(a, b, c)
    assert check == result

