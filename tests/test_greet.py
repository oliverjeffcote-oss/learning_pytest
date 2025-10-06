from lib.greet import *

def test_return_name():
    result = greet("Ollie")

    assert result == "Hello, Ollie!"