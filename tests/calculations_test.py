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
   # Arrange
   n = 10

   # Act
   result = get_nth_fibonacci(n)

   # Assert
   assert result == 55