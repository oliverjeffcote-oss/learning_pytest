from lib.gratitudes import *

def test_initial_output_empty():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

def test_one_gratitude_added_is_returned():
    gratitudes = Gratitudes()
    gratitudes.add("My loving family")
    assert gratitudes.format() == "Be grateful for: My loving family"

def test_three_gratitudes_given_are_returned():
    gratitudes = Gratitudes()
    gratitudes.add("My loving family")
    gratitudes.add("The nice weather today")
    gratitudes.add("Cats")
    assert gratitudes.format() == "Be grateful for: My loving family, The nice weather today, Cats"