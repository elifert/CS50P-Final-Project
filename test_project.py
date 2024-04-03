from project import get_climate, return_crop, quit_or_continue, list_crops
from unittest.mock import patch
import builtins


def test_get_climate():
    assert get_climate("New York,USA") == "Cfa"
    assert get_climate("Massachusetts,USA") == "Dfb"
    assert get_climate("Kocaeli,Turkey") == None  # not defined 
    assert get_climate("Istanbul,Turkey") == "Csa"
    assert get_climate("Paris,France") == "Cfb"
    assert get_climate("Berlin,Germany") == "Cfb"


def test_return_crop():
    assert return_crop("abc") == None
    assert return_crop("csa") == ["wheat", "beet", "corn", "barley"]
    assert return_crop("bs") == ["sunflower", "barley"]


def test_quit_or_continue():
    with patch.object(builtins, "input", lambda _: "y"): # replacing input method for testing
        assert quit_or_continue() == True
    with patch.object(builtins, "input", lambda _: "Y"):
        assert quit_or_continue() == True
    with patch.object(builtins, "input", lambda _: "n"):
        assert quit_or_continue() == False
    with patch.object(builtins, "input", lambda _: "N"):
        assert quit_or_continue() == False


def test_list_crops():
    assert list_crops() == "wheat, beet, corn, sunflower, barley"
