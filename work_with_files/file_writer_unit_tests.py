import file_writer
import os.path
from tika import parser

def test_check_if_file_created():
    writer = file_writer.FileWriter()
    writer.write_pdf()
    assert os.path.isfile("default_file.pdf")

def test_check_if_file_wrote():
    writer_with_text = file_writer.FileWriter(content='test')
    writer_with_text.write_pdf()
    result = parser.from_file('default_file.pdf')['content']
    assert result.__contains__("test")
