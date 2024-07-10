class ContactInfo:
    
    def __init__(self, name, number):
        self.name = name 
        self.number = number

    def format(self):
        return f"{self.name}: {self.number}"
    
    def update(self, new_name, new_number):
        self.name = new_name
        self.number = new_number