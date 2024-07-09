from lib.task import Task

class TodoList:
    def __init__(self):
        self.to_do_list = []

    def add(self, task):
        if isinstance(task, Task):
            self.to_do_list.append(task)

    def incomplete(self):
        #   A list of Todo instances representing the todos that are not complete
        return [task for task in self.to_do_list if task.complete == False]

    def complete(self):
        #   A list of Todo instances representing the todos that are complete
        return [task for task in self.to_do_list if task.complete == True]

    def give_up(self):
        #   Marks all todos as complete
        for task in self.to_do_list:
            if task.complete == False:
                task.complete = True