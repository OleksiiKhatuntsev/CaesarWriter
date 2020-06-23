def get_ciphered_letter(alphabet, letter, shift_value=0):
    index = alphabet.index(ord(letter))
    if index + shift_value >= len(alphabet):
        result_letter = alphabet[index + shift_value - len(alphabet)]
    else:
        result_letter = alphabet[index + shift_value]
    return result_letter


class CaesarCipher():

    def __init__(self):
        self.LOW_LETTERS = [letter for letter in range(ord('a'), ord('z') + 1)]
        self.BIG_LETTERS = [letter for letter in range(ord('A'), ord('Z') + 1)]
        self.SPECIAL_SYMBOLS = ['\n', '\a', '\b', '\f', '\r', '\t']

    def get_ciphered_text(self, text = "", shift_value = 0):
        result_text = ""
        for letter in text:
            if letter in self.SPECIAL_SYMBOLS:
                result_text += letter
            elif letter.isupper():
                result_text += chr(get_ciphered_letter(self.BIG_LETTERS, letter, shift_value))
            elif letter.islower():
                result_text += chr(get_ciphered_letter(self.LOW_LETTERS, letter, shift_value))
        return result_text
