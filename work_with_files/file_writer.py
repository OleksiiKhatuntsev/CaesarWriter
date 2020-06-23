import pdfkit

class FileWriter():

    def __init__(self, content, path="default_file.pdf"):
        self.path = path
        self.content = content

    def write_pdf(self):
        pdfkit.from_string(self.content, self.path)