import string
import nltk
from nltk.corpus import words
nltk.download('words')


def is_english_word(word):
    return word in words.words()


class DecryptText:
    def __init__(self, cipher_text):
        self.cipher = cipher_text
        self.uppercase_list = list(string.ascii_uppercase)
        self.uppercase_list.append(' ')
        self.key = None
        self.plain = ''

    def is_plain(self):
        true_records = 0
        words_list = self.plain.split(' ')
        for w in words_list:
            if is_english_word(w):
                true_records += 1
        if true_records/len(words_list)>0.8:
            return True
        return False

    def plain_with_key(self, a, b):
        res = ''
        for c in self.cipher:
            new_index = (a * self.uppercase_list.index(c) + b) % 27
            res += self.uppercase_list[new_index]
        return res

    def decrypt(self):
        for test_key in range(27):
            self.plain = self.plain_with_key(test_key)
            if self.is_plain():
                return self.plain
        return "Can't find plain text!"


if __name__ == '__main__':
    input_text = open('sc_p1_input.txt').read()
    preprocessed_text = input_text.replace(' ', '').replace('\n', '')
    decrypt_text = DecryptText(input_text)
    print(decrypt_text.decrypt())
    # with open('sc_p1_output.txt', 'w') as output_file:
    #     output_file.write(cipher_text)

# def find_duplicates(text):
#     words = text.split(' ')
#     s = set()
#     duplicates = []
#     for word in words:
#         if word in s:
#             duplicates.append(word)
#         else:
#             s.add(word)
#     return duplicates
