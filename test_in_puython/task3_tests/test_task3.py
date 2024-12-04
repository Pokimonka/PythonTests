import pytest

from task3_tests.task3 import get_name, documents, directories, add, get_directory


@pytest.mark.parametrize(
    'doc_number, result',
    (
        ("10006", 'Аристарх Павлов'),
        ("11-2", "Геннадий Покемонов")

    )
)
def test_get_name(doc_number, result):
    check = get_name(doc_number)
    assert check == result

@pytest.mark.parametrize(
    'doc_number, result',
    (
        ("101", 'Документ не найден'),
        ("yjkl", 'Документ не найден')

    )
)
def test_not_found_get_name(doc_number, result):
    check = get_name(doc_number)
    assert check == result


@pytest.mark.parametrize(
    'document_type, number, name, shelf_number',
    (
            ("international passport", '311 020203', 'Александр Пушкин', '3'),
            ("passport", '454647', 'Елена Прекрасная', '3')

    )
)
def test_add_doc(document_type, number, name, shelf_number):
    add(document_type, number, name, shelf_number)
    assert {"type": document_type,
             "number": number, "name": name}  in documents
    assert number in directories[shelf_number]

@pytest.mark.parametrize(
    'doc_number, result',
    (
        ('10006', '2'),
        ("11-2", '1'),
        ('311 020203', '3')

    )
)
def test_get_directory(doc_number, result):
    check = get_directory(doc_number)
    assert check == result


@pytest.mark.parametrize(
    'doc_number, result',
    (
        ('8790', 'Полки с таким документом не найдено'),
        ("j,hg", 'Полки с таким документом не найдено')

    )
)
def test_not_found_get_directory(doc_number, result):
    check = get_directory(doc_number)
    assert check == result





