class FileReader():

    def __init__(self, path = "../default_file.txt"):
        self.path = path

    def read_file(self):
        with open(self.path, 'r') as reader:
            result = reader.read()
        return result

reader = FileReader()
print(reader.read_file())