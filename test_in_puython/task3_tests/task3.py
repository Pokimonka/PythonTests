documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

def get_name(doc_number):
    name_person = ""
    for doc in documents:
        if doc["number"] == doc_number:
            name_person = doc["name"]
    if name_person == "":
        return "Документ не найден"
    return name_person


def get_directory(doc_number):
    for value in directories:
        if directories[value].count(doc_number) > 0:
            return value
    return "Полки с таким документом не найдено"



def add(document_type, number, name, shelf_number):
    document = {}
    document["type"] = document_type
    document["number"] = number
    document["name"] = name
    documents.append(document)

    if shelf_number in directories and directories[str(shelf_number)]:
        directories[str(shelf_number)].append(number)
    else:
        directories[str(shelf_number)] = [number]

if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))