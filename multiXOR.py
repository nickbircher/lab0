import base64
from itertools import product
from XOR import xor_strings
from common import hex_to_bytes
from singleXOR import english_score, expected_frequency

def find_key_length(ciphertext: bytes, max_key_length: int) -> int:
    best_score = 0
    best_key_length = 0

    for key_length in range(1, max_key_length + 1):
        blocks = [ciphertext[i::key_length] for i in range(key_length)]
        score = 0

        for block in blocks:
            for key in range(256):  # Try all possible single-byte keys
                plaintext = xor_strings(block, bytes([key]))
                if english_score(plaintext) < 50:
                    score += 1

        if score > best_score:
            best_score = score
            best_key_length = key_length

    return best_key_length


def decrypt(ciphertext: bytes, key_length: int):
    keys = [list() for _ in range(key_length)]

    for i in range(key_length):
        block = ciphertext[i::key_length]

        for k in range(256):  # Try all possible single-byte keys
            plaintext = xor_strings(block, bytes([k]))
            score = english_score(plaintext)
            if score < 50:
                    keys[i].append(k)
    for key in product(*keys):
        print(xor_strings(ciphertext, bytes(key)))


def main():
    with open('Lab0.TaskII.C.txt', 'r') as file:
        lines = file.read()
        lines = base64.b64decode(lines)
        key_length = find_key_length(lines, 10)
        decrypt(lines, key_length)


if __name__ == '__main__':
    main()