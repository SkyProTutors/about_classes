import random

MAX_TASKS_NUMBER = 8


# этот класс умеет помнить имя Храброго Студента, назначать ему номер задачки и печатать данные
class BraveStudent:
    def __init__(self, name: str):
        self.name: str = name
        self.__task_number: int = 0
        self.__score: int = 5               # 5 by default ;-)

    def set_task_number(self, number: int):
        """setter for __task_number"""
        self.__task_number = number

    def __str__(self):
        return f"{self.__class__.__name__} {self.name} берет задание {self.__task_number}"


# А вот этот класс не наследует класс Храбрых Студентов, но активно его использует
# это не наследование, это композиция
# обратите внимание на typehints - если они есть pyCharm знает о методах применяемых к объектам
class Roulette:
    def __init__(self):
        self.students_list = []

    def set_students_list(self, names4roulette: tuple):
        """
        create new BraveStudents with names from names4roulette
        :param names4roulette: list of names like as ["Bill Gates", "Jeff Bezos", "Ilon Mask"]
        """
        self.students_list = [BraveStudent(names4roulette[i]) for i in range(0, len(names4roulette))]
        # добавляем на лету создавая наши объекты, передавая им имена из списка

    def set_task_for_each_students(self, task_list: list[int]):
        """
        this function change all BraveStudent in self.students_list
        also it change the task_list (it remove task's numbers which will be use)
        :param task_list: list in format [1,2,3... N]  
        """""
        if len(task_list) >= len(self.students_list):
            for student in self.students_list:
                shot = random.randint(0, len(task_list) - 1)
                student.set_task_number(task_list.pop(shot))  # волшебная строка. делает много ;-)

    def print_all_information(self):
        """just print all elements of self.students_list"""
        for student in self.students_list:
            print(student)


if __name__ == '__main__':
    # список с именами, из которых создадим Храбрых Студентов
    names_for_roulette: tuple = ("Дима А", "Галина", "Денис")

    # герератор списка с номерами заданий
    tasks_in_list: list[int] = [i for i in range(MAX_TASKS_NUMBER)]

    roulette = Roulette()                                # создали экземпляр рулетки
    roulette.set_students_list(names_for_roulette)       # заполнили набором Храбрых Студентов
    roulette.set_task_for_each_students(tasks_in_list)   # распределили номера задач
    roulette.print_all_information()                     # напечатали

