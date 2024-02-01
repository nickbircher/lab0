from typing import List
from singleXOR import english_score


def shift_letters(text: str, shift: int) -> str:
    shifted_text = ''
    for char in text:
        shifted_text += chr((ord(char) - 97 - shift) % 26 + 97)
    return shifted_text

def find_key_length(ciphertext: str, max_key_length: int) -> int:
    best_score = 0
    best_key_length = 0

    for key_length in range(1, max_key_length + 1):
        blocks = [ciphertext[i::key_length] for i in range(key_length)]
        score = 0

        for block in blocks:
            for i in range(26):
                if (english_score(shift_letters(block, i)) < 50):
                    score += 1

        if score > best_score:
            best_score = score
            best_key_length = key_length

    return best_key_length


def find_key(ciphertext: str, key_length: int) -> List[int]:
    key = [0] * key_length

    for i in range(key_length):
        block = ciphertext[i::key_length]
        best_score = 100
        best_key = 0

        for k in range(26):  # Try all possible single-byte keys
            score = english_score(shift_letters(block, k))
            if score < best_score:
                    best_score = score
                    best_key = k

        key[i] = best_key

    return key


def decrypt(ciphertext: str, key: List[int]) -> str:
    plaintext = ''
    key_length = len(key)

    for i in range(len(ciphertext)):
        plaintext += shift_letters(ciphertext[i], key[i % key_length])

    return plaintext


def main():
    with open('Lab0.TaskII.D.txt', 'r') as file:
        lines = file.read()
        key_length = find_key_length(lines, 16)
        key = find_key(lines, key_length)

        print(decrypt(lines, key))


if __name__ == '__main__':
    main()