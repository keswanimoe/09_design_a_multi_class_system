from lib.task import Task

# Instanstiate Task class
def test_Task_can_be_instanstiated():
    to_do = Task("My Task")
    assert isinstance(to_do, Task) == True

# Checking that task property is set
def test_task_property_is_set():
    to_do = Task("My Task")
    actual = to_do.task
    expected = "My Task"
    assert actual == expected

# All Task initially are set to incomplete  
def test_initially_complete_property_set_to_false():
    to_do = Task("My Task")
    actual = to_do.complete
    expected = False
    assert actual == expected
    
# Checking mark_complete method is working 
def test_mark_complete_sets_complete_to_true():
    to_do = Task("My Task")
    actual = to_do.mark_complete()
    actual = to_do.complete
    expected = True
    assert actual == expected