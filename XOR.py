def xor_strings(input_string: bytes, key: bytes) -> str:
    key_length = len(key)
    input_length = len(input_string)

    repeated_key = key * (input_length // key_length) + key[:input_length % key_length]
    result = ''.join(chr(a ^ b) for a, b in zip(input_string, repeated_key))

    return result