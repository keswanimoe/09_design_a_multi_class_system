class Diary:
    
    def __init__(self):
        self.diary = []
        self.words = []
        self.todo = []

    def add(self, entry):
        self.diary.append(entry)

    def all(self):
        return self.diary  

# filter Entries by how much time and reading speed
# method: get entry word count 
# method: reading time using word count + user's reading ability by wpm  
# method: filter method using the reading time and entry word count methods
    
    def count_words(self):
        for entry in self.diary:
            self.words.append(entry.count_words())
        return sum(self.words)
    
    def reading_time(self, wpm):
        mins = self.count_words()/wpm
        return int(mins)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        self.count_words()
        readable = wpm*minutes
        can_read = [x for x in self.words if x < readable]
        # [expression for item in iterable if condition]
        
        if can_read == []:
            raise Exception(f"No entries can be read")
        else:
        # find the index of the diary entry with the most words in can_read
            return self.diary[self.words.index(max(can_read))]