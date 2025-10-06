from lib.string_builder import *

def test_initial_output_is_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

def test_initial_size_is_zero():
    string_builder = StringBuilder()
    assert string_builder.size() == 0

def test_string_length_given_one_string():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.size() == 5

def test_string_length_given_three_strings():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add(" ")
    string_builder.add("world")
    assert string_builder.size() == 11

def test_string_output_given_one_string():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.output() == "hello"

def test_string_output_given_three_strings():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add(" ")
    string_builder.add("world")
    assert string_builder.output() == "hello world"

