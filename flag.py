binary_code = "010001100110110001100001011001110111101101100101011101000011000001011111011011000110010101100111011010110011000001111101"


n = 8
binary_values = [binary_code[i:i+n] for i in range(0, len(binary_code), n)]


decoded_chars = [chr(int(bv, 2)) for bv in binary_values]


decoded_string = ''.join(decoded_chars)

print(f"Decoded string: {decoded_string}")