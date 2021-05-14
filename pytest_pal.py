import pytest
import palindrome
from io import StringIO

def test_yes(monkeypatch):
    usr_input = StringIO(u'racecar\n')
    monkeypatch.setattr('sys.stdin', usr_input)
    assert palindrome.check_pal() == "yes"
def test_no(monkeypatch):
    usr_input = StringIO(u'hello\n')
    monkeypatch.setattr('sys.stdin', usr_input)
    assert palindrome.check_pal() == "no"
def test_empty(monkeypatch):
    usr_input = StringIO(u'\n')
    monkeypatch.setattr('sys.stdin', usr_input)
    assert palindrome.check_pal() == "empty"