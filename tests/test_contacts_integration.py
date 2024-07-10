from lib.contacts import Contacts
from lib.contact_info import ContactInfo

contacts = Contacts()
john = ContactInfo("John Doe", "12345678910")

# an instance of ContactInfo can be added to Contacts
def test_add_a_contact_to_contact():
    contacts.add(john)

    result = contacts.contacts_list
    expected = [john]
    assert result == expected

# multiple contacts can be added to list of contacts
def test_add_multiple_contacts():
    jane = ContactInfo("Jane Doe", "11111111111")
    contacts.add(jane)

    result = contacts.contacts_list
    expected = [john, jane]
    assert result == expected

# view all contacts neatly
def test_view_contacts_list():
    result = contacts.view()
    expected = "John Doe: 12345678910\nJane Doe: 11111111111"
    assert result == expected