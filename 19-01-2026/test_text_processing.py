import pytest
from text_processing import Text

def test_clean_text_removes_special_chars():
    assert Text.clean_text(" John@#$ ") == "John@"

def test_valid_email():
    assert Text.is_valid_email("user@gmail.com")

def test_invalid_email():
    assert not Text.is_valid_email("user@@gmail.com")

def test_valid_phone():
    assert Text.is_valid_phone("9123456789")

def test_invalid_phone():
    assert not Text.is_valid_phone("5123456789")

