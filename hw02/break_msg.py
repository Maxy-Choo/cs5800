def fastExp(x, y, N): # x^y mod p
    if y == 0:
        return 1
    if y == 1:
        return x
    
    half = y // 2
    rem = y % 2
    sp = fastExp(x, half, N)
    val = (sp * sp) % N
    if rem == 1:
        val = (val * x) % N
    return val

def break_msg(encoded_msg, e, N, bit_len):
    for i in range(1 << bit_len):
        if fastExp(i, e, N) == encoded_msg:
            return i
    return -1

if __name__ == "__main__":
    encoded_msg = 74904
    N, e = 252167, 11
    bit_len = N.bit_length()
    decoded_msg = break_msg(encoded_msg, e, N, bit_len)
    if decoded_msg != -1:
        print(f"Decoded message: {decoded_msg}")
    else:
        print("Failed to decode the message.")