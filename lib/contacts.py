class Contacts:
    
    def __init__(self):
        self.contacts_list = []

    def add(self, contact):
        self.contacts_list.append(contact)

    def view(self):
        all = ""
        for contact in self.contacts_list:
                all += f"{contact.format()}\n"
        return all.strip()