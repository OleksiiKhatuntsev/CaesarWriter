import unittest
import file_reader

reader = file_reader.FileReader()

def test_read_from_default_file():
    value = reader.read_file()
    assert value == "default_text\nhere"