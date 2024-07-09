class Diary:
    
    def __init__(self):
        self.diary = []
        self.todo = []

    def add(self, entry):
        self.diary.append(entry)

    def all(self):
        return self.diary