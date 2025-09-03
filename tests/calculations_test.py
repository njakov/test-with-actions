# System Modules
import sys
import os

# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    n = 10
    result = get_nth_fibonacci(n)
    assert result == 55

def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    assert get_nth_fibonacci(0) == 0

def test_get_nth_fibonacci_one():
    """Test with n=1."""
    assert get_nth_fibonacci(1) == 1

def test_get_nth_fibonacci_negative():
    """Test with negative n raises ValueError."""
    try:
        get_nth_fibonacci(-1)
    except ValueError as e:
        assert str(e) == "n cannot be negative"
    else:
        assert False, "ValueError not raised for negative n"

def test_area_of_circle_positive():
    """Test area_of_circle with positive radius."""
    radius = 2
    expected = math.pi * radius ** 2
    assert area_of_circle(radius) == expected

def test_area_of_circle_zero():
    """Test area_of_circle with radius zero."""
    assert area_of_circle(0) == 0

def test_area_of_circle_negative():
    """Test area_of_circle with negative radius raises ValueError."""
    try:
        area_of_circle(-1)
    except ValueError as e:
        assert str(e) == "Radius cannot be negative"
    else:
        assert False, "ValueError not raised for negative radius"