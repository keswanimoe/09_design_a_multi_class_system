from lib.diary import Diary
from lib.diary_entry import DiaryEntry
import pytest

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

# return word count for ALL entries in diary list
def test_returns_word_count_for_all_entries():
    my_diary = Diary()
    entry1 = DiaryEntry('My Title', 'These are the contents')
    entry2 = DiaryEntry('A Title', 'This is the contents')
    my_diary.add(entry1)
    my_diary.add(entry2)
    actual = my_diary.count_words()
    expected = 8
    assert actual == expected
    
# return estimate reading time 
def test_returns_estimate_reading_time():
    my_diary = Diary()
    entry1 = DiaryEntry('My Title', 'These are the contents')
    entry2 = DiaryEntry('A Title', 'This is the contents')
    my_diary.add(entry1)
    my_diary.add(entry2)
    actual = my_diary.reading_time(4)
    expected = 2
    assert actual == expected
    
# select the best entry suited for user's reading speed
def test_find_best_reading_time_given_reading_speed():
    my_diary = Diary()
    entry1 = DiaryEntry('My Title', 'These are the contents of my diary which I write')
    entry2 = DiaryEntry('A Title', 'This is the contents of my diary entry which I believe is fiften words long')
    my_diary.add(entry1)
    my_diary.add(entry2)
    actual = my_diary.find_best_entry_for_reading_time(13, 1)
    expected = entry1
    assert actual == expected
    
# second test to select the best entry suited for user's reading speed
def test_find_best_reading_time_given_reading_speed_again():
    my_diary = Diary()
    entry1 = DiaryEntry('My Title', 'These are the contents of my diary which I write')
    entry2 = DiaryEntry('A Title', 'This is the contents of my diary entry which I believe is fiften words long')
    my_diary.add(entry1)
    my_diary.add(entry2)
    actual = my_diary.find_best_entry_for_reading_time(16, 1)
    expected = entry2
    assert actual == expected
    
# raise exception if there is no suitable best entry
def test_best_reading_time_does_not_exist():
    my_diary = Diary()
    entry1 = DiaryEntry('My Title', 'These are the contents of my diary which I write')
    entry2 = DiaryEntry('A Title', 'This is the contents of my diary entry which I believe is fiften words long')
    my_diary.add(entry1)
    my_diary.add(entry2)
    with pytest.raises(Exception) as e: 
        my_diary.find_best_entry_for_reading_time(8, 1)
    error_message = str(e.value) 
    expected = "No entries can be read"
    assert error_message == expected