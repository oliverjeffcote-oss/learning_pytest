from lib.check_codeword import *

def test_correct_codeword():
    result = check_codeword("horse")

    assert result == "Correct! Come in."

def test_first_and_last_letter_correct():
    result = check_codeword("house")

    assert result == "Close, but nope."

def test_wrong_codeword():
    result = check_codeword("apple")

    assert result == "WRONG!"

def test_first_letter_correct():
    result = check_codeword("harvest")

    assert result == "WRONG!"

def test_last_letter_correct():
    result = check_codeword("mouse")

    assert result == "WRONG!"