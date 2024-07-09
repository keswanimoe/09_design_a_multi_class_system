from lib.diary_entry import DiaryEntry

entry = DiaryEntry('My Title', 'These are the contents')

# Instantiate DiaryEntry class 
def test_entry_can_be_instantiated():
    assert isinstance(entry, DiaryEntry)

# Initialises with title and contents
def test_initialises_with_title_and_contents():
    actual_title = entry.title
    actual_contents = entry.contents
    
    expected_title = 'My Title'
    expected_comtents = 'These are the contents'
    
    assert actual_title == expected_title
    assert actual_contents == expected_comtents

def test_returns_formatted_diary_entry():    
    actual = entry.format()
    expected = "My Title: These are the contents"
    
    assert actual == expected