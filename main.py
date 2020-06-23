from caesar_cipher.caesar_cipher import CaesarCipher
from work_with_files.file_reader import FileReader
from work_with_files.file_writer import FileWriter

if __name__ == "__main__":

    cipher = CaesarCipher()
    reader = FileReader()

    not_safe_text = reader.read_file()

    safe_text = cipher.get_ciphered_text(not_safe_text, 10)

    writer = FileWriter(safe_text)
    writer.write_pdf()