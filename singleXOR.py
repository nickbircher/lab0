from XOR import xor_strings
from common import hex_to_bytes


expected_frequency = {
    'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 13.0, 'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.2, 'k': 0.8, 'l': 4.0,
    'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9, 'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8, 'v': 1.0, 'w': 2.4, 'x': 0.2,
    'y': 2.0, 'z': 0.1
}


def english_score(text: str) -> int:
    text = text.lower()
    text_length = len(text)

    return sum(abs(expected_frequency[letter] - (text.count(letter) / text_length * 100)) for letter in expected_frequency)


def main():
    with open('Lab0.TaskII.B.txt', 'r') as file:
        lines = file.read().splitlines()

    for line in lines:
        for key in range(256):
            key = bytes([key])
            result = xor_strings(hex_to_bytes(line), key)
            if english_score(result) < 50:
                print(result)


if __name__ == '__main__':
    main()