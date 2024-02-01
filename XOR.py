def xor_strings(input_string: bytes, key: bytes) -> str:
    result = b''

    for i in range(len(input_string)):
        result += bytes([input_string[i] ^ key[i % len(key)]])

    return str(result)