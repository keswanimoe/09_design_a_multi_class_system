from lib.contact_info import ContactInfo

contact = ContactInfo("John Doe", "12345678910")

# Instanstiate Contacts class
def test_instantiate_contact():
    assert isinstance(contact, ContactInfo)

# Each contact should contain a name and mobile number
def test_initialises_with_name_and_number():
    name_result = contact.name
    name_expected = "John Doe"

    number_result = contact.number
    number_expected = "12345678910"

    assert name_result == name_expected
    assert number_result == number_expected

# Format contact info
def test_format_contact():
    result = contact.format()
    expected = "John Doe: 12345678910"
    assert result == expected

# Ability to update contact 
def test_update_contact():
    contact.update("Jane Doe", "11111111111")

    name_result = contact.name
    name_expected = "Jane Doe"

    number_result = contact.number
    number_expected = "11111111111"

    assert name_result == name_expected
    assert number_result == number_expected
