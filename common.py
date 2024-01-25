def bytes_to_hex(byte_string):
    hex_string = byte_string.hex()
    return hex_string

def hex_to_bytes(hex_string):
    byte_string = bytes.fromhex(hex_string)
    return byte_string
