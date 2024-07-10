from lib.contacts import Contacts

# Instanstiate Contacts class
def test_instantiate_contacts():
    contacts = Contacts()
    assert isinstance(contacts, Contacts)

# Initially list of contacts is empty
def test_initially_contacts_empty():
    contacts = Contacts()
    result = contacts.contacts_list
    expected = []
    assert result == expected
