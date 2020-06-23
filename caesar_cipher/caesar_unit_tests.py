import caesar_cipher

cipher = caesar_cipher.CaesarCipher()

def test_cipher_for_message():
    assert cipher.get_ciphered_text("abc", 1) == "bcd"
def test_cipher_for_message_with_spaces():
    assert cipher.get_ciphered_text("a bc", 1) == "b cd"
def test_cipher_for_message_with_symbols():
    assert cipher.get_ciphered_text("a\nbc", 1) == "b\ncd"
def test_cipher_for_message_with_symbols_and_spaces():
    assert cipher.get_ciphered_text("a\nb c", 1) == "b\nc d"
def test_cipher_for_message_with_overlimited_index():
    assert cipher.get_ciphered_text("xyz", 1) == "yza"
def test_cipher_for_message_with_uppercase_letters():
    assert cipher.get_ciphered_text("ABC", 1) == "BCD"
def test_cipher_for_message_with_upper_and_lower_case_letters():
    assert cipher.get_ciphered_text("aBc", 1) == "bCd"

