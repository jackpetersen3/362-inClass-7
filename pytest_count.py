import pytest
import word_count
from io import StringIO

def test_2(monkeypatch):
    usr_input = StringIO(u'hello world\n')
    monkeypatch.setattr('sys.stdin', usr_input)
    assert word_count.wordCount() == 2
def test_5(monkeypatch):
    usr_input = StringIO(u'hello world goodbye today tomorrow\n')
    monkeypatch.setattr('sys.stdin', usr_input)
    assert word_count.wordCount() == 5
def test_fail(monkeypatch): 
    usr_input = StringIO(u'hello world goodbye today tomorrow\n')
    monkeypatch.setattr('sys.stdin', usr_input)
    assert word_count.wordCount() == 1
def test_empty(monkeypatch):
    usr_input = StringIO(u'\n')
    monkeypatch.setattr('sys.stdin', usr_input)
    assert word_count.wordCount() == 0