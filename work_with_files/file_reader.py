class FileReader():
    """
    Class for read from txt file
    :param path: path to file on your local machine
    """
    def __init__(self, path = "default_file.txt"):
        self.path = path

    def read_file(self):
        """
        Read all text from your file
        :return: text from your file
        """
        with open(self.path, 'r') as reader:
            result = reader.read()
        return result