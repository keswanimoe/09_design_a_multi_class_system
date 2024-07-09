from lib.todo_list import TodoList

# Instantiate Todo class
def test_todo_list_can_be_instantiated():
    my_list = TodoList()
    assert isinstance(my_list, TodoList)
    
# Initalises with an empty list of tasks
def test_initialise_a_todo_list():
    my_list = TodoList()
    result = my_list.to_do_list
    expected = []
    assert result == expected

# Inital list of incomplete tasks should be empty 
def test_initially_incomplete_list_is_empty():
    my_list = TodoList()
    result = my_list.incomplete()
    expected = []
    assert result == expected
    
# Inital list of complete tasks should be empty 
def test_initially_complete_list_is_empty():
    my_list = TodoList()
    result = my_list.complete()
    expected = []
    assert result == expected
    