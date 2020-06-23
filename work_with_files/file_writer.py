import pdfkit

class FileWriter():
    """
    Class to write pdf using pdfkit
    :param content: all content you wanna to write to the file
    :param path: path to new or existing (will be replaced) file
    """
    def __init__(self, content = "", path="default_file.pdf"):
        self.path = path
        self.content = content

    def write_pdf(self):
        """
        Write pdf using pdfkit
        :return:
        """
        pdfkit.from_string(self.content, self.path)