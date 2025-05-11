import argparse
import sys
from json import dumps
from typing import Dict, List


def parser_creation():
    # Создание экземпляра парсера, который извлекает аргументы из командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    parser.add_argument("--report", "-r", default="payout")

    return parser


def file_reader(file):
    with open(rf"{file}", "r") as f:

        # Превращение .CSV файла во вложенный по строкам список
        file_structure: List[List[...],] = [row.rstrip("\n").split(",") for row in f]

        # Получение значения процентной ставки
        rate_index: int = [
            file_structure[0].index(value)
            for value in file_structure[0]
            if value == "hourly_rate" or value == "rate" or value == "salary"
        ][0]

        # Получение значений остальных необходимых параметров
        variables: Dict[str:int] = {
            "name": 0,
            "department": 0,
            "hours_worked": 0,
        }
        for index in range(len(file_structure[0])):
            for key in variables:
                if file_structure[0][index] == key:
                    variables[key] = file_structure[0].index(key)

        # Словарь, в котором ключ - название департамента, значение - заработная плата
        data = dict()

        department_index = variables["department"]
        hours_worked_index = variables["hours_worked"]

        for row in file_structure[1:]:
            if row[department_index] not in data:
                data[row[department_index]] = int(row[hours_worked_index]) * int(
                    row[rate_index]
                )
            else:
                data[row[department_index]] += int(row[hours_worked_index]) * int(
                    row[5]
                )
        return data


if __name__ == "__main__":
    parser = parser_creation()

    # Извлечение информации из команды запуска скрипта
    namespace = parser.parse_args(sys.argv[1:])

    # Разновидность вывода, когда ключ - название отчёта,
    # значение - список из данных разных файлов
    #
    # В списке из данных разных файлов содержатся словари
    # Ключ словаря - название департамента,
    # Значение - заработная плата сотрудников департаментов
    #
    # Иголка в яйце, яйцо в утке, утка в зайце, заяц в сундуке !
    #
    # Значения ЗП между одинаковыми департаментами в разных файлах не суммируются
    report = {
        namespace.report: [],
    }

    for file in namespace.files:
        file_data: Dict[str:int, ...] = file_reader(file)
        report[namespace.report].append(file_data)

    print(dumps(report))
