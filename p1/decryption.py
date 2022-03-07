import string


def preprocess_cipher(cipher_text):
    return cipher_text.replace(' ', '').replace('\n', '')


def normalize_dictionary(d):
    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

    d_min = min(d.values())
    d_max = max(d.values())
    for k in d:
        d[k] = (d[k] - d_min) / (d_max - d_min)
    return d


class DecryptText:
    def __init__(self, cipher_text):
        self.cipher = cipher_text
        self.uppercase_list = list(string.ascii_uppercase)
        self.key = {}
        self.plain = ''
        self.cipher_frequency = {}
        self.english_frequency = {
            'E': 12000,
            'T': 9000,
            'A': 8000,
            'I': 8000,
            'N': 8000,
            'O': 8000,
            'S': 8000,
            'H': 6400,
            'R': 6200,
            'D': 4400,
            'L': 4000,
            'U': 3400,
            'C': 3000,
            'M': 3000,
            'F': 2500,
            'W': 2000,
            'Y': 2000,
            'G': 1700,
            'P': 1700,
            'B': 1600,
            'V': 1200,
            'K': 800,
            'Q': 500,
            'J': 400,
            'X': 400,
            'Z': 200
        }

    def find_frequencies(self):
        for c in self.uppercase_list:
            self.cipher_frequency[c] = 0
        for c in self.cipher:
            self.cipher_frequency[c] += 1

    def find_plain_with_key(self):
        for c in self.cipher:
            self.plain += self.key[c]
        return self.plain

    def find_key(self):
        self.find_frequencies()
        self.english_frequency = normalize_dictionary(self.english_frequency)
        self.cipher_frequency = normalize_dictionary(self.cipher_frequency)

        temp = list(self.english_frequency.keys())
        for i, c in enumerate(self.cipher_frequency.keys()):
            self.key[c] = temp[i]

    def decrypt(self):
        self.find_key()
        self.find_plain_with_key()
        return self.plain


if __name__ == '__main__':
    input_text = open('sc_p1_input.txt').read()
    preprocessed_text = preprocess_cipher(input_text)
    decrypt_text = DecryptText(preprocessed_text)
    plain_text = decrypt_text.decrypt()
    print(plain_text)
    with open('sc_p1_output.txt', 'w') as output_file:
        output_file.write(plain_text)
