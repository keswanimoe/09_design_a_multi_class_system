from lib.diary_entry import DiaryEntry
from lib.contacts import Contacts
from lib.contact_info import ContactInfo

# an instance of Contacts can be added to DiaryEntry
def test_contact_list_in_diary_entry():
    entry = DiaryEntry('My Title', 'These are the contents')

    contacts = Contacts()

    result = entry.contacts_list(contacts)
    expected = []
    assert result == expected

# see list of contacts in diary entry
def test_contact_list_in_diary_entry():
    entry = DiaryEntry('My Title', 'These are the contents')

    contacts = Contacts()
    john = ContactInfo("John Doe", "12345678910")
    jane = ContactInfo("Jane Doe", "11111111111")
    contacts.add(john)
    contacts.add(jane)

    result = entry.contacts_list(contacts)
    expected = [john, jane]
    assert result == expected

# ability to reformat list 
def test_contact_list_in_diary_entry():
    entry = DiaryEntry('My Title', 'These are the contents')

    contacts = Contacts()
    john = ContactInfo("John Doe", "12345678910")
    jane = ContactInfo("Jane Doe", "11111111111")
    contacts.add(john)
    contacts.add(jane)

    result = entry.view_contacts(contacts)
    expected = "John Doe: 12345678910\nJane Doe: 11111111111"
    assert result == expected