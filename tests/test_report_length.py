from lib.report_length import *
import pytest

def test_correct_length_returned_10():
    result = report_length("hammertime")

    assert result == "This string was 10 characters long."

def test_correct_length_returned_0():
    result = report_length("")

    assert result == "This string was 0 characters long."

def test_integer_input():
    with pytest.raises(TypeError):
        report_length(123)

def test_list_input():
    with pytest.raises(TypeError):
        report_length(['Portsmouth', 'Football', 'Club'])

def test_none_input():
    with pytest.raises(TypeError):
        report_length(None)


