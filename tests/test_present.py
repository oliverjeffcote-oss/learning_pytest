from lib.present import *
import pytest

def test_wrap_one_present():
    present = Present()
    present.wrap("Bike")
    assert present.contents == "Bike", "Should return Bike as the wrapped present"

def test_try_to_wrap_more_than_one_present():
    present = Present()
    present.wrap("New Bike")
    with pytest.raises(Exception) as err:
        present.wrap("Scooter")
    assert str(err.value) == "A contents has already been wrapped."

def test_unwrap_one_existing_present():
    present = Present()
    present.wrap("Bike")
    present.unwrap()
    assert present.contents == "Bike", "Should return Bike as the unwrapped present"

def test_unwrap_with_no_wrapped_presents():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    assert str(err.value) == "No contents have been wrapped."

def test_wrapping_already_wrapped_preserves_value():
    present = Present()
    present.wrap("Bike")
    with pytest.raises(Exception) as err:
        present.wrap("Scooter")
    assert present.unwrap() == "Bike"
