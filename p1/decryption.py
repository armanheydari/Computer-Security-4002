import string
import nltk
from nltk.corpus import words
import math

nltk.download('words')


class DecryptText:
    def __init__(self, cipher_text):
        self.cipher = cipher_text.replace(' ', '').replace('\n', '')
        self.uppercase_list = list(string.ascii_uppercase)
        self.key = (0, 0)
        self.plain = ''
        self.words = []
        self.english_words_set = set(words.words())

    def find_plain_with_key(self, a, b):
        self.plain = ''
        for c in self.cipher:
            index = self.uppercase_list.index(c)
            for i in range(30):
                temp = ((index + i*26 - b)/a)
                if temp.is_integer():
                    index = int(temp)
                    break
            self.plain += self.uppercase_list[index]

    def find_words(self, max_depth=15):
        word_first_index = 0
        words = []
        while word_first_index < len(self.plain):
            word_last_index = word_first_index
            for j in range(max_depth):
                if self.plain[word_first_index:word_first_index + j + 1].lower() in self.english_words_set:
                    word_last_index = word_first_index + j + 1
            words.append(self.plain[word_first_index:word_last_index])
            word_first_index = word_last_index
        return words

    def decrypt(self):
        print("decryption started...")
        for a in range(1, 26):
            if math.gcd(a, 26) == 1:
                for b in range(1, 26):
                    self.find_plain_with_key(a, b)
                    words = self.find_words()
                    if len(self.cipher) > 2 * len(words):
                        self.words = words
                        self.key = (a, b)
                        break

            if len(self.words) > 0:
                print("done with a,b:", self.key)
                break


if __name__ == '__main__':
    input_text = open('sc_p1_input.txt').read()
    decrypt_text = DecryptText(input_text)
    decrypt_text.decrypt()
    with open('sc_p1_output.txt', 'w') as output_file:
        output_file.write(' '.join(decrypt_text.words))
    print("you can see the plain text in sc_p1_output.txt!")
