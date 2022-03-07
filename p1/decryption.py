import string
import nltk
from nltk.corpus import words

nltk.download('words')


def is_english_word(word):
    return word in words.words()


def preprocess_cipher(cipher_text):
    return cipher_text.replace(' ', '').replace('\n', '')


class DecryptText:
    def __init__(self, cipher_text):
        self.cipher = cipher_text
        self.uppercase_list = list(string.ascii_uppercase)
        self.uppercase_list.append(' ')
        self.key = None
        self.plain = ''

    def is_plain(self, founded_word_rate=0.8):
        true_records = 0
        words_list = self.plain.split(' ')
        for w in words_list:
            if is_english_word(w):
                true_records += 1
        if true_records / len(words_list) > founded_word_rate:
            return True
        return False

    def find_plain_with_key(self, key):
        res = ''
        for c in self.cipher:
            new_index = (self.uppercase_list.index(c) + key) % 26
            res += self.uppercase_list[new_index]
        return res

    def decrypt(self):
        for test_key in range(26):
            self.plain = self.find_plain_with_key(test_key)
            if self.is_plain():
                self.key = test_key
                return self.plain
        return "Couldn't find plain text!"


if __name__ == '__main__':
    input_text = open('sc_p1_input.txt').read()
    preprocessed_text = preprocess_cipher(input_text)
    decrypt_text = DecryptText(preprocessed_text)
    plain_text = decrypt_text.decrypt()
    print(plain_text)
    with open('sc_p1_output.txt', 'w') as output_file:
        output_file.write(plain_text)
