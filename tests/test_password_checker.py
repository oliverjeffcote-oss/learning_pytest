from lib.password_checker import *
import pytest

def test_valid_password_entered():
    password_checker = PasswordChecker()
    assert password_checker.check("thisisavalidpassword") == True

def test_invalid_password_entered():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("123")
    assert str(e.value) == "Invalid password, must be 8+ characters"