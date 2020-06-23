import unittest
import caesar_cipher


class MyTestCase(unittest.TestCase):

    cipher = caesar_cipher.CaesarCipher()

    def test_cipher_for_message(self):
        self.assertEqual(self.cipher.get_ciphered_text("abc", 1), "bcd")
    def test_cipher_for_message_with_spaces(self):
        self.assertEqual(self.cipher.get_ciphered_text("a bc", 1), "b cd")
    def test_cipher_for_message_with_symbols(self):
        self.assertEqual(self.cipher.get_ciphered_text("a\nbc", 1), "b\ncd")
    def test_cipher_for_message_with_symbols_and_spaces(self):
        self.assertEqual(self.cipher.get_ciphered_text("a\nb c", 1), "b\nc d")
    def test_cipher_for_message_with_overlimited_index(self):
        self.assertEqual(self.cipher.get_ciphered_text("xyz", 1), "yza")
    def test_cipher_for_message_with_uppercase_letters(self):
            self.assertEqual(self.cipher.get_ciphered_text("ABC", 1), "BCD")
    def test_cipher_for_message_with_overlimited_index(self):
                self.assertEqual(self.cipher.get_ciphered_text("aBc", 1), "bCd")


if __name__ == '__main__':
    unittest.main()
