from lib.counter import *

def test_initial_count_is_0():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far", "Should count 0"

def test_returns_correct_count_3():
    counter = Counter()
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 3 so far", "Should count 3"

def test_returns_correct_count_10():
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 10 so far", "Should count 10"

def test_add_two_numbers_to_counter():
    counter = Counter()
    counter.add(5)
    counter.add(10)
    assert counter.report() == "Counted to 15 so far"

def test_adding_minus_numbers():
    counter = Counter()
    counter.add(-1)
    counter.add(-4)
    assert counter.report() == "Counted to -5 so far"

