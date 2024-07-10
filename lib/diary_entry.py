from lib.contacts import Contacts

class DiaryEntry:   
    
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        return f"{self.title}: {self.contents}"
    
    def count_words(self):
        return len(self.contents.split(" "))
    
    def contacts_list(self, contacts):
        return contacts.contacts_list
    
    def view_contacts(self, contacts):
        return contacts.view()