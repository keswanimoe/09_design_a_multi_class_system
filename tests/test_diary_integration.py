from lib.diary import Diary
from lib.diary_entry import DiaryEntry

# an instance of DiaryEntry can be added to Diary
def test_add_an_entry_to_diary():
    my_diary = Diary()
    entry = DiaryEntry('My Title', 'These are the contents')
    my_diary.add(entry)
    actual = my_diary.diary
    expected = [entry]
    assert actual == expected

# multiple entries can be added and are returned as a list
def test_returns_list_of_entries():
    my_diary = Diary()
    entry1 = DiaryEntry('My Title', 'These are the contents')
    entry2 = DiaryEntry('A Title', 'This is the contents')
    my_diary.add(entry1)
    my_diary.add(entry2)
    actual = my_diary.all()
    expected = [entry1, entry2]
    assert actual == expected