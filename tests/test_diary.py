from lib.diary import Diary

# Instantiate Diary class 
def test_diary_can_be_instantiated():
    my_diary = Diary()
    assert isinstance(my_diary, Diary)

# Diary is an empty list with no entries
def test_initialise_diary_is_empty_list():
    my_diary = Diary()
    actual = my_diary.diary
    expected = []
    assert actual == expected

# Todo is an empty list with no tasks
def test_initialise_diary_is_empty_list():
    my_diary = Diary()
    actual = my_diary.todo
    expected = []
    assert actual == expected